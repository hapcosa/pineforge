"""
CLI para reconciliar comprobantes DVU contra cartola bancaria.
"""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

try:
    from .config import CARTOLA_XLSX, OUTPUT_XLSX, RECONCILIACION_XLSX
except ImportError:  # Permite ejecucion local no empaquetada
    from config import CARTOLA_XLSX, OUTPUT_XLSX, RECONCILIACION_XLSX


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Cruza comprobantes_dvu.xlsx contra cartola.xlsx.",
    )
    parser.add_argument(
        "--comprobantes",
        type=Path,
        default=OUTPUT_XLSX,
        help=f"Ruta al Excel de comprobantes. Default: {OUTPUT_XLSX}",
    )
    parser.add_argument(
        "--cartola",
        type=Path,
        default=CARTOLA_XLSX,
        help=f"Ruta a cartola bancaria. Default: {CARTOLA_XLSX}",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=RECONCILIACION_XLSX,
        help=f"Ruta de salida. Default: {RECONCILIACION_XLSX}",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    args = _build_parser().parse_args(argv)

    try:
        try:
            from .reconciliar import reconciliar
        except ImportError:
            from reconciliar import reconciliar
    except ImportError as exc:
        print(
            "Faltan dependencias para reconciliar. Ejecuta: "
            "pip install -r dvu_bot/requirements.txt",
            file=sys.stderr,
        )
        print(f"Detalle: {exc}", file=sys.stderr)
        return 2

    try:
        output_path = reconciliar(
            comprobantes_path=args.comprobantes,
            cartola_path=args.cartola,
            output_path=args.output,
        )
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    except Exception as exc:
        logging.exception("No se pudo generar la reconciliacion")
        print(f"Error: {exc}", file=sys.stderr)
        return 3

    print(f"Reconciliacion generada: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
