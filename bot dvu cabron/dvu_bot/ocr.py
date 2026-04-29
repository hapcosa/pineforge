"""
Modulo OCR — usa EasyOCR con preprocesado OpenCV para comprobantes bancarios.
Instancia unica del reader (costoso inicializar).
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import List, Optional

import cv2
import numpy as np

from config import OCR_GPU, OCR_LANGUAGES

logger = logging.getLogger(__name__)

_READER = None


def get_reader():
    """Devuelve una instancia singleton de EasyOCR Reader."""
    global _READER
    if _READER is None:
        try:
            import easyocr
            logger.info("Inicializando EasyOCR (puede tardar en la primera ejecucion)...")
            _READER = easyocr.Reader(OCR_LANGUAGES, gpu=OCR_GPU, verbose=False)
        except Exception as e:
            logger.error(f"No se pudo inicializar EasyOCR: {e}")
            raise
    return _READER


def preprocess_image(image_path: Path) -> Optional[np.ndarray]:
    """
    Preprocesa imagen para mejorar OCR:
    - Lee la imagen
    - Convierte a escala de grises
    - Aplica denoise y threshold adaptativo
    """
    try:
        img = cv2.imdecode(
            np.fromfile(str(image_path), dtype=np.uint8), cv2.IMREAD_COLOR
        )
        if img is None:
            logger.warning(f"No se pudo leer imagen: {image_path}")
            return None

        # Redimensionar si es muy pequena (mejora OCR)
        h, w = img.shape[:2]
        if max(h, w) < 1000:
            scale = 1500 / max(h, w)
            img = cv2.resize(img, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)

        # Escala de grises
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Denoise
        gray = cv2.fastNlMeansDenoising(gray, None, 10, 7, 21)

        return gray
    except Exception as e:
        logger.error(f"Error preprocesando {image_path}: {e}")
        return None


def ocr_image(image_path: Path) -> str:
    """
    Aplica OCR a una imagen y devuelve el texto completo.
    Texto vacio si falla.
    """
    reader = get_reader()
    processed = preprocess_image(image_path)

    try:
        if processed is not None:
            results = reader.readtext(processed, detail=0, paragraph=True)
        else:
            # Fallback: leer directo
            results = reader.readtext(str(image_path), detail=0, paragraph=True)

        text = "\n".join(results) if results else ""
        return text.strip()
    except Exception as e:
        logger.error(f"Error en OCR de {image_path}: {e}")
        return ""


def ocr_image_lines(image_path: Path) -> List[str]:
    """Devuelve lineas individuales OCR, util para parseo por lineas."""
    text = ocr_image(image_path)
    return [ln.strip() for ln in text.splitlines() if ln.strip()]
