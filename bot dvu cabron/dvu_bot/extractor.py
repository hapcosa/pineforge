"""
Extractor de entidades (texto WhatsApp + texto OCR).
Todo metodo devuelve str/None/listas — nunca lanza.
"""

from __future__ import annotations

import logging
import re
import unicodedata
from dataclasses import dataclass, field
from typing import List, Optional

from config import (
    ABONO_KEYWORDS,
    BANCOS_CL,
    KEYWORDS_MONTO,
    KEYWORDS_OPERACION,
    KEYWORDS_RUT,
    KEYWORDS_ORIGEN,
    KEYWORDS_DESTINO,
)

logger = logging.getLogger(__name__)


# ─── REGEX ─────────────────────────────────────────────────────

# Facturas: "factura 33780", "facturas 33135 y 33134", "F33780", "Fac: 33780"
RE_FACTURA = re.compile(
    r"(?:fac(?:tura)?s?\.?|f|n[°º]?\s*fac(?:tura)?)\s*[:\-]?\s*"
    r"(?P<nums>[\d]{3,8}(?:\s*(?:,|y|e)\s*[\d]{3,8})*)",
    re.IGNORECASE,
)
RE_FACTURA_NUMBER = re.compile(r"\d{3,8}")

# Monto: "$510.459", "510.459", "$ 162.792", "68282"
RE_MONTO = re.compile(
    r"(?:\$\s*)?(?P<num>\d{1,3}(?:[.\s]\d{3}){1,3}|\d{4,9})(?!\d)"
)

# RUT chileno: 12.345.678-9 / 12345678-9 / 7.654.321-K
RE_RUT = re.compile(
    r"\b(?P<rut>\d{1,2}(?:[.\s]?\d{3}){2}\s*[-–]\s*[\dkK])\b"
)

# Numero operacion (6-12 digitos cerca de keyword)
RE_OP_NUM = re.compile(r"\b(\d{6,12})\b")

# Fecha formato chileno: 15/03/2025, 15-03-25
RE_FECHA = re.compile(
    r"\b(\d{1,2}[/\-.]\d{1,2}[/\-.]\d{2,4})\b"
)

# Hora: 14:35, 09:12:45, 2:30 PM
RE_HORA = re.compile(
    r"\b(\d{1,2}:\d{2}(?::\d{2})?\s*(?:[ap]\.?\s*m\.?)?)\b",
    re.IGNORECASE,
)

# Cuenta bancaria (4+ digitos, a menudo con guiones)
RE_CUENTA = re.compile(r"\b(\d{4,}[\-\s]?\d{2,}(?:[\-\s]?\d+)*)\b")


# ─── DATACLASS DE RESULTADO ────────────────────────────────────

@dataclass
class ExtractedData:
    # WhatsApp
    fecha_msg: str = ""
    hora_msg: str = ""
    vendedor: str = ""
    cliente: str = ""
    facturas: List[str] = field(default_factory=list)
    detalle_vendedor: str = ""
    es_abono: bool = False

    # OCR
    monto: Optional[int] = None
    banco: str = ""
    cuenta_origen: str = ""
    cuenta_destino: str = ""
    rut: str = ""
    fecha_tx: str = ""
    hora_tx: str = ""
    n_operacion: str = ""
    texto_ocr: str = ""
    archivo_imagen: str = ""

    # Metadata
    ocr_valido: bool = True


# ─── UTILIDADES ────────────────────────────────────────────────

def _strip_accents(s: str) -> str:
    return "".join(
        c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c)
    )


def _normalize(s: str) -> str:
    return _strip_accents(s or "").lower()


# ─── EXTRACCION DESDE TEXTO WHATSAPP ───────────────────────────

def extract_facturas(text: str) -> List[str]:
    """Devuelve lista de numeros de factura encontrados (orden, unicos)."""
    if not text:
        return []
    found: List[str] = []
    seen = set()
    for m in RE_FACTURA.finditer(text):
        nums = m.group("nums")
        for n in RE_FACTURA_NUMBER.findall(nums):
            if n not in seen:
                seen.add(n)
                found.append(n)
    # Fallback: buscar patrones aislados con "F" + digitos
    if not found:
        for m in re.finditer(r"\bF\s*(\d{3,8})\b", text, re.IGNORECASE):
            n = m.group(1)
            if n not in seen:
                seen.add(n)
                found.append(n)
    return found


def extract_cliente(body: str, facturas: List[str]) -> str:
    """
    Heuristica: busca un nombre propio (palabras con mayusculas) en el body
    excluyendo numeros de factura y palabras clave.
    """
    if not body:
        return ""

    # Quitar menciones de factura
    clean = re.sub(
        r"(?:fac(?:tura)?s?\.?|f)\s*[:\-]?\s*\d{3,8}(?:\s*(?:,|y|e)\s*\d{3,8})*",
        "",
        body,
        flags=re.IGNORECASE,
    )
    # Quitar numeros aislados
    clean = re.sub(r"\b\d{3,}\b", "", clean)
    # Quitar palabras tipicas
    stop = {
        "pago", "pagos", "factura", "facturas", "abono", "saldo", "parcial",
        "transferencia", "transferencias", "por", "de", "del", "la", "el",
        "y", "e", "cliente", "señor", "senor", "sra", "sr", "comprobante",
    }
    tokens = [t for t in re.split(r"\s+", clean.strip()) if t]
    filtered = [t for t in tokens if _normalize(t) not in stop and len(t) > 1]

    # Tomar secuencia de palabras con primera letra mayuscula (nombre propio)
    # o en mayusculas completas
    name_tokens: List[str] = []
    for t in filtered:
        clean_t = re.sub(r"[^\wÁÉÍÓÚÜÑáéíóúüñ]", "", t)
        if not clean_t:
            continue
        if clean_t[0].isupper() or clean_t.isupper():
            name_tokens.append(clean_t)

    if name_tokens:
        name = " ".join(name_tokens[:6]).strip()
        return name.title() if name.isupper() else name
    return ""


def is_abono(body: str) -> bool:
    if not body:
        return False
    n = _normalize(body)
    return any(k in n for k in ABONO_KEYWORDS)


# ─── EXTRACCION DESDE TEXTO OCR ────────────────────────────────

def _parse_monto_str(s: str) -> Optional[int]:
    """Normaliza '510.459' o '510 459' o '68282' a int."""
    if not s:
        return None
    clean = s.replace(".", "").replace(" ", "").replace(",", "")
    if clean.isdigit():
        val = int(clean)
        # Filtro de rango razonable (evita numeros de operacion o RUT)
        if 500 <= val <= 999_999_999:
            return val
    return None


def extract_monto(ocr_text: str) -> Optional[int]:
    """
    Busca el monto principal:
    1. Lineas con keyword (monto/total/transferido) — mayor prioridad.
    2. Si no hay, elige el numero con formato de miles ($ o puntos).
    """
    if not ocr_text:
        return None

    lines = ocr_text.splitlines()
    candidatos: List[int] = []

    # Pasada 1: lineas con keyword
    for ln in lines:
        n = _normalize(ln)
        if any(k in n for k in KEYWORDS_MONTO):
            # Priorizar matches con $ o punto de miles
            for m in RE_MONTO.finditer(ln):
                val = _parse_monto_str(m.group("num"))
                if val is not None:
                    candidatos.append(val)
    if candidatos:
        return max(candidatos)

    # Pasada 2: numeros con formato de miles ($xxx.xxx)
    for m in re.finditer(r"\$\s*(\d{1,3}(?:[.\s]\d{3}){1,3})", ocr_text):
        val = _parse_monto_str(m.group(1))
        if val is not None:
            candidatos.append(val)
    if candidatos:
        return max(candidatos)

    # Pasada 3: cualquier formato con punto de miles
    for m in re.finditer(r"\b(\d{1,3}(?:[.\s]\d{3}){1,3})\b", ocr_text):
        val = _parse_monto_str(m.group(1))
        if val is not None:
            candidatos.append(val)
    if candidatos:
        return max(candidatos)

    return None


def extract_banco(ocr_text: str) -> str:
    if not ocr_text:
        return ""
    n = _normalize(ocr_text)
    for banco in BANCOS_CL:
        if _normalize(banco) in n:
            return banco.title() if banco.isupper() else banco
    return ""


def extract_rut(ocr_text: str) -> str:
    if not ocr_text:
        return ""
    m = RE_RUT.search(ocr_text)
    if m:
        rut = m.group("rut").replace(" ", "")
        return rut.upper()
    return ""


def _extract_near_keyword(lines: List[str], keywords: List[str], pattern: re.Pattern) -> str:
    """Busca pattern en la misma linea que un keyword o en la siguiente."""
    for i, ln in enumerate(lines):
        n = _normalize(ln)
        if any(k in n for k in keywords):
            # Misma linea
            m = pattern.search(ln)
            if m:
                return m.group(1) if m.groups() else m.group(0)
            # Siguiente linea
            if i + 1 < len(lines):
                m = pattern.search(lines[i + 1])
                if m:
                    return m.group(1) if m.groups() else m.group(0)
    return ""


def extract_operacion(ocr_text: str) -> str:
    if not ocr_text:
        return ""
    lines = ocr_text.splitlines()
    op = _extract_near_keyword(lines, KEYWORDS_OPERACION, RE_OP_NUM)
    return op


def extract_cuentas(ocr_text: str) -> (str, str):
    """Devuelve (origen, destino)."""
    if not ocr_text:
        return "", ""
    lines = ocr_text.splitlines()
    origen = _extract_near_keyword(lines, KEYWORDS_ORIGEN, RE_CUENTA)
    destino = _extract_near_keyword(lines, KEYWORDS_DESTINO, RE_CUENTA)
    return origen, destino


def extract_fecha_hora(ocr_text: str) -> (str, str):
    if not ocr_text:
        return "", ""
    f = RE_FECHA.search(ocr_text)
    h = RE_HORA.search(ocr_text)
    return (f.group(1) if f else ""), (h.group(1) if h else "")


# ─── ORQUESTADOR ───────────────────────────────────────────────

def extract_from_whatsapp(msg_body: str) -> dict:
    facturas = extract_facturas(msg_body)
    cliente = extract_cliente(msg_body, facturas)
    return {
        "cliente": cliente,
        "facturas": facturas,
        "es_abono": is_abono(msg_body),
        "detalle": msg_body.strip(),
    }


def extract_from_ocr(ocr_text: str) -> dict:
    fecha, hora = extract_fecha_hora(ocr_text)
    origen, destino = extract_cuentas(ocr_text)
    return {
        "monto": extract_monto(ocr_text),
        "banco": extract_banco(ocr_text),
        "rut": extract_rut(ocr_text),
        "n_operacion": extract_operacion(ocr_text),
        "cuenta_origen": origen,
        "cuenta_destino": destino,
        "fecha_tx": fecha,
        "hora_tx": hora,
    }
