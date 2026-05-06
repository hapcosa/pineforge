"""
DVU COMPROBANTES BOT — punto de entrada.

Flujo:
    1. Parsea chat.txt de WhatsApp.
    2. Empareja cada mensaje con su imagen adjunta en input/media/.
    3. Aplica OCR a cada imagen.
    4. Extrae entidades (texto + OCR).
    5. Valida y marca estado.
    6. Genera Excel profesional.
"""

from __future__ import annotations

import logging
import sys
import argparse
from pathlib import Path
from typing import Dict, List, Optional

try:
    from .config import (
        CHAT_FILE,
        LOG_DIR,
        LOG_FILE,
        MEDIA_DIR,
        MEDIA_EXTENSIONS,
        OUTPUT_XLSX,
    )
    from .excel import write_excel
    from .extractor import extract_from_ocr, extract_from_whatsapp
    from .ocr import extract_text
    from .parser_whatsapp import WhatsAppMessage, parse_chat
    from .validator import validate_records
except ImportError:  # Permite ejecutar python dvu_bot/main.py
    from config import (
        CHAT_FILE,
        LOG_DIR,
        LOG_FILE,
        MEDIA_DIR,
        MEDIA_EXTENSIONS,
        OUTPUT_XLSX,
    )
    from excel import write_excel
    from extractor import extract_from_ocr, extract_from_whatsapp
    from ocr import extract_text
    from parser_whatsapp import WhatsAppMessage, parse_chat
    from validator import validate_records


# ─── LOGGING ───────────────────────────────────────────────────

def setup_logging() -> None:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    fmt = "%(asctime)s [%(levelname)s] %(name)s — %(message)s"
    logging.basicConfig(
        level=logging.INFO,
        format=fmt,
        handlers=[
            logging.FileHandler(LOG_FILE, encoding="utf-8"),
            logging.StreamHandler(sys.stdout),
        ],
    )


logger = logging.getLogger("dvu_bot")


# ─── EMPAREJAMIENTO MENSAJE ↔ IMAGEN ───────────────────────────

def _index_media(media_dir: Path) -> Dict[str, Path]:
    """Devuelve {nombre_archivo_lower: ruta} para busqueda rapida."""
    idx: Dict[str, Path] = {}
    if not media_dir.exists():
        return idx
    for p in media_dir.iterdir():
        if p.is_file() and p.suffix.lower() in MEDIA_EXTENSIONS:
            idx[p.name.lower()] = p
    return idx


def _resolve_attachment(msg: WhatsAppMessage, media_idx: Dict[str, Path]) -> Optional[Path]:
    if not msg.attachment:
        return None
    name = msg.attachment.strip().lower()
    if name in media_idx:
        return media_idx[name]
    # Busqueda parcial (algunas exportaciones truncan o alteran)
    for fname, path in media_idx.items():
        if name in fname or fname in name:
            return path
    return None


# ─── PIPELINE ──────────────────────────────────────────────────

def build_records(messages: List[WhatsAppMessage], media_dir: Path) -> List[Dict]:
    media_idx = _index_media(media_dir)
    orphan_images = set(media_idx.values())
    records: List[Dict] = []

    logger.info(
        f"Procesando {len(messages)} mensajes y {len(media_idx)} adjuntos..."
    )

    for msg in messages:
        # Ignorar mensajes de sistema / sin contenido util
        if not msg.sender:
            continue

        wa = extract_from_whatsapp(msg.body)
        img_path = _resolve_attachment(msg, media_idx)

        ocr_text = ""
        ocr_data = {
            "monto": None, "banco": "", "rut": "", "n_operacion": "",
            "cuenta_origen": "", "cuenta_destino": "", "fecha_tx": "", "hora_tx": "",
        }

        if img_path is not None:
            orphan_images.discard(img_path)
            logger.info(f"Extrayendo texto → {img_path.name}")
            ocr_text = extract_text(img_path)
            if ocr_text:
                ocr_data = extract_from_ocr(ocr_text)

        records.append({
            "Fecha Mensaje": msg.date,
            "Hora Mensaje": msg.time,
            "Vendedor": msg.sender,
            "Cliente Detectado": wa["cliente"] or "REVISAR",
            "Factura(s)": ", ".join(wa["facturas"]),
            "Monto Transferido": ocr_data["monto"] if ocr_data["monto"] else "",
            "Banco": ocr_data["banco"],
            "Cuenta Origen": ocr_data["cuenta_origen"],
            "Cuenta Destino": ocr_data["cuenta_destino"],
            "RUT": ocr_data["rut"],
            "Fecha Transferencia": ocr_data["fecha_tx"],
            "Hora Transferencia": ocr_data["hora_tx"],
            "N° Operación": ocr_data["n_operacion"],
            "Detalle Vendedor": wa["detalle"],
            "Texto OCR": ocr_text,
            "Archivo Imagen": img_path.name if img_path else "",
            "Estado": "",
            "Observación": "",
            "_es_abono": wa["es_abono"],
        })

    # Adjuntos huerfanos (sin mensaje asociado): se incluyen como filas sueltas
    for orphan in orphan_images:
        logger.info(f"Texto huerfano → {orphan.name}")
        ocr_text = extract_text(orphan)
        ocr_data = extract_from_ocr(ocr_text) if ocr_text else {
            "monto": None, "banco": "", "rut": "", "n_operacion": "",
            "cuenta_origen": "", "cuenta_destino": "", "fecha_tx": "", "hora_tx": "",
        }
        records.append({
            "Fecha Mensaje": "",
            "Hora Mensaje": "",
            "Vendedor": "",
            "Cliente Detectado": "REVISAR",
            "Factura(s)": "",
            "Monto Transferido": ocr_data["monto"] if ocr_data["monto"] else "",
            "Banco": ocr_data["banco"],
            "Cuenta Origen": ocr_data["cuenta_origen"],
            "Cuenta Destino": ocr_data["cuenta_destino"],
            "RUT": ocr_data["rut"],
            "Fecha Transferencia": ocr_data["fecha_tx"],
            "Hora Transferencia": ocr_data["hora_tx"],
            "N° Operación": ocr_data["n_operacion"],
            "Detalle Vendedor": "(imagen sin mensaje asociado)",
            "Texto OCR": ocr_text,
            "Archivo Imagen": orphan.name,
            "Estado": "",
            "Observación": "",
            "_es_abono": False,
        })

    return records


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Procesa comprobantes DVU desde WhatsApp.")
    parser.add_argument(
        "--reconciliar",
        action="store_true",
        help="Al terminar el bot, cruza comprobantes contra input/cartola.xlsx.",
    )
    args = parser.parse_args(argv)

    setup_logging()
    logger.info("═══ DVU COMPROBANTES BOT ═══")

    if not CHAT_FILE.exists() and not any(MEDIA_DIR.glob("*")):
        logger.error(
            f"No hay entrada. Coloca chat.txt en {CHAT_FILE} e imagenes en {MEDIA_DIR}"
        )
        return 1

    try:
        messages = parse_chat(CHAT_FILE)
    except Exception as e:
        logger.error(f"Error parseando chat: {e}")
        messages = []

    try:
        records = build_records(messages, MEDIA_DIR)
    except Exception as e:
        logger.exception(f"Error construyendo registros: {e}")
        return 2

    if not records:
        logger.warning("No se generaron registros. Revisa input/.")
        return 0

    records = validate_records(records)

    try:
        write_excel(records, OUTPUT_XLSX)
    except Exception as e:
        logger.exception(f"Error escribiendo Excel: {e}")
        return 3

    # Resumen
    from collections import Counter
    counts = Counter(r["Estado"] for r in records)
    logger.info("── Resumen de estados ──")
    for estado, n in counts.most_common():
        logger.info(f"  {estado}: {n}")

    logger.info(f"Listo. Excel en: {OUTPUT_XLSX}")

    if args.reconciliar:
        try:
            try:
                from .reconciliar import reconciliar
            except ImportError:
                from reconciliar import reconciliar

            output_path = reconciliar()
            logger.info(f"Reconciliacion lista en: {output_path}")
        except Exception as e:
            logger.exception(f"Error ejecutando reconciliacion: {e}")
            return 4

    return 0


if __name__ == "__main__":
    sys.exit(main())
