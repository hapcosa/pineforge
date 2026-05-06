"""
Parser del archivo exportado de WhatsApp (chat.txt).
Soporta los dos formatos de exportacion estandar (Android/iOS, 12h/24h).
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional

logger = logging.getLogger(__name__)


# Patron de linea de mensaje:
#   [dd/mm/yy, hh:mm:ss] Nombre: mensaje      (iOS)
#   dd/mm/yy, hh:mm - Nombre: mensaje         (Android)
#   dd-mm-yyyy hh:mm - Nombre: mensaje
RE_MSG_IOS = re.compile(
    r"^\[(?P<date>\d{1,2}[/\-.]\d{1,2}[/\-.]\d{2,4}),?\s+"
    r"(?P<time>\d{1,2}:\d{2}(?::\d{2})?(?:\s*[ap]\.?\s*m\.?)?)\]\s+"
    r"(?P<sender>[^:]+?):\s?(?P<body>.*)$",
    re.IGNORECASE,
)

RE_MSG_ANDROID = re.compile(
    r"^(?P<date>\d{1,2}[/\-.]\d{1,2}[/\-.]\d{2,4}),?\s+"
    r"(?P<time>\d{1,2}:\d{2}(?::\d{2})?(?:\s*[ap]\.?\s*m\.?)?)\s*[-–]\s*"
    r"(?P<sender>[^:]+?):\s?(?P<body>.*)$",
    re.IGNORECASE,
)

# Patron para detectar adjuntos en el mensaje
RE_ATTACHED_IOS = re.compile(r"<adjunto:\s*(?P<file>[^>]+)>", re.IGNORECASE)
RE_ATTACHED_GENERIC = re.compile(
    r"(?P<file>[\w\-\s\.()]+?\.(?:jpg|jpeg|png|webp|bmp|pdf|opus|mp4))",
    re.IGNORECASE,
)
RE_ATTACHMENT_EXPORT_LINE = re.compile(
    r"^\s*\u200e?.*?\.(?:jpg|jpeg|png|webp|bmp|pdf|opus|mp4)\s*"
    r"(?:\(archivo adjunto\))?\s*$",
    re.IGNORECASE,
)
RE_OMITTED = re.compile(
    r"(imagen omitida|<Media omitted>|<archivo adjunto:|image omitted|sticker omitido)",
    re.IGNORECASE,
)


@dataclass
class WhatsAppMessage:
    date: str = ""
    time: str = ""
    sender: str = ""
    body: str = ""
    attachment: Optional[str] = None
    has_media_omitted: bool = False
    raw_lines: List[str] = field(default_factory=list)


def _match_header(line: str):
    m = RE_MSG_IOS.match(line)
    if m:
        return m
    return RE_MSG_ANDROID.match(line)


def parse_chat(chat_path: Path) -> List[WhatsAppMessage]:
    """
    Lee chat.txt y devuelve lista de mensajes estructurados.
    Soporta mensajes multilinea (une lineas sin header al mensaje anterior).
    """
    if not chat_path.exists():
        logger.warning(f"Archivo chat no encontrado: {chat_path}")
        return []

    try:
        content = chat_path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        logger.error(f"No se pudo leer {chat_path}: {e}")
        return []

    messages: List[WhatsAppMessage] = []
    current: Optional[WhatsAppMessage] = None

    for raw in content.splitlines():
        line = raw.strip("﻿").rstrip()
        if not line:
            continue

        m = _match_header(line)
        if m:
            if current is not None:
                _finalize(current)
                messages.append(current)
            current = WhatsAppMessage(
                date=m.group("date").strip(),
                time=m.group("time").strip(),
                sender=m.group("sender").strip(),
                body=m.group("body").strip(),
            )
            current.raw_lines.append(line)
        else:
            # Continuacion del mensaje anterior
            if current is not None:
                current.body += "\n" + line
                current.raw_lines.append(line)

    if current is not None:
        _finalize(current)
        messages.append(current)

    logger.info(f"Parseados {len(messages)} mensajes desde WhatsApp.")
    return messages


def _finalize(msg: WhatsAppMessage) -> None:
    """Detecta adjuntos y medios omitidos en el cuerpo."""
    body = msg.body
    if RE_OMITTED.search(body):
        msg.has_media_omitted = True

    m = RE_ATTACHED_IOS.search(body)
    if m:
        msg.attachment = m.group("file").strip()

    if msg.attachment is None:
        m = RE_ATTACHED_GENERIC.search(body)
    if msg.attachment is None and m:
        msg.attachment = m.group("file").strip()

    if msg.attachment:
        msg.body = _remove_attachment_lines(body)


def _remove_attachment_lines(body: str) -> str:
    """Quita lineas de adjunto exportadas por WhatsApp antes de extraer cliente."""
    cleaned = []
    for line in body.splitlines():
        raw = line.strip()
        if not raw:
            continue
        if RE_ATTACHED_IOS.search(raw):
            continue
        if RE_ATTACHMENT_EXPORT_LINE.match(raw) or RE_ATTACHED_GENERIC.fullmatch(raw):
            continue
        cleaned.append(line)
    return "\n".join(cleaned).strip()
