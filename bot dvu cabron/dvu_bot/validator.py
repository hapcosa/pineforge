"""
Validador — asigna Estado y Observacion a cada registro.
Tambien detecta duplicados sobre el dataset completo.
"""

from __future__ import annotations

import logging
from typing import Dict, List

logger = logging.getLogger(__name__)


def _base_state(row: Dict) -> (str, List[str]):
    """Calcula el estado base (sin deteccion de duplicados) y observaciones."""
    obs: List[str] = []

    monto = row.get("Monto Transferido")
    cliente = (row.get("Cliente Detectado") or "").strip()
    facturas = (row.get("Factura(s)") or "").strip()
    ocr_text = (row.get("Texto OCR") or "").strip()
    es_abono = bool(row.get("_es_abono"))
    tiene_imagen = bool((row.get("Archivo Imagen") or "").strip())

    faltantes = []

    if tiene_imagen and (not ocr_text or len(ocr_text) < 15):
        return "REVISAR OCR", ["OCR vacio o ilegible"]

    if not monto:
        faltantes.append("monto")
    if not cliente or cliente.upper() == "REVISAR":
        faltantes.append("cliente")
    if not facturas:
        faltantes.append("factura")

    if es_abono:
        if faltantes:
            obs.append("Faltan: " + ", ".join(faltantes))
        return "ABONO PARCIAL", obs

    if not faltantes:
        return "LISTO PARA INGRESAR", obs

    # Estados especificos si falta solo uno
    if faltantes == ["monto"]:
        return "FALTA MONTO", obs
    if faltantes == ["cliente"]:
        return "FALTA CLIENTE", obs
    if faltantes == ["factura"]:
        return "FALTA FACTURA", obs

    obs.append("Faltan: " + ", ".join(faltantes))
    return "FALTA DATO", obs


def _dup_key(row: Dict) -> tuple:
    """Clave para detectar duplicados."""
    return (
        str(row.get("N° Operación") or "").strip(),
        str(row.get("Monto Transferido") or ""),
        str(row.get("Fecha Transferencia") or "").strip(),
    )


def validate_records(records: List[Dict]) -> List[Dict]:
    """
    Aplica estado y deteccion de duplicados sobre todos los registros.
    Muta in-place y devuelve la misma lista.
    """
    # Primera pasada: estado base
    for r in records:
        state, obs = _base_state(r)
        r["Estado"] = state
        r["Observación"] = " | ".join(obs) if obs else ""

    # Segunda pasada: duplicados por N° operacion + monto + fecha.
    # Reenvios literales de la misma imagen no se marcan como duplicado.
    seen: Dict[tuple, List[int]] = {}
    for i, r in enumerate(records):
        key = _dup_key(r)
        # Ignorar claves muy vacias
        if not any(key) or not key[0]:
            continue
        seen.setdefault(key, []).append(i)

    for key, idxs in seen.items():
        archivos = {
            (records[idx].get("Archivo Imagen") or "").strip().lower()
            for idx in idxs
        }
        if len(archivos) <= 1:
            continue
        for idx in idxs:
            records[idx]["Estado"] = "DUPLICADO POSIBLE"
            prev = records[idx].get("Observación", "")
            dup_msg = f"Posible duplicado de N°op {key[0]}"
            records[idx]["Observación"] = (
                (prev + " | " + dup_msg).strip(" |") if prev else dup_msg
            )

    # Limpiar campos internos
    for r in records:
        r.pop("_es_abono", None)

    return records
