"""
Configuracion global del DVU COMPROBANTES BOT.
Centraliza rutas, parametros OCR y constantes de negocio.
"""

from pathlib import Path

# ─── RUTAS BASE ────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent
INPUT_DIR = BASE_DIR / "input"
MEDIA_DIR = INPUT_DIR / "media"
CHAT_FILE = INPUT_DIR / "chat.txt"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_XLSX = OUTPUT_DIR / "comprobantes_dvu.xlsx"
LOG_DIR = BASE_DIR / "logs"
LOG_FILE = LOG_DIR / "dvu_bot.log"

# ─── OCR ───────────────────────────────────────────────────────
OCR_LANGUAGES = ["es", "en"]
OCR_GPU = False  # True si hay CUDA disponible

# Extensiones de imagen aceptadas
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".bmp"}

# ─── REGEX / PARSING ───────────────────────────────────────────
# Umbral de confianza para detectar cliente
CLIENT_MIN_LEN = 3

# Palabras que indican abono parcial
ABONO_KEYWORDS = [
    "abono", "abona", "saldo", "parcial", "parte", "cuota",
    "adelanto", "anticipo",
]

# Bancos chilenos comunes
BANCOS_CL = [
    "BANCO DE CHILE", "BANCO ESTADO", "BANCOESTADO", "BCI", "SANTANDER",
    "ITAU", "SCOTIABANK", "SECURITY", "FALABELLA", "RIPLEY", "CONSORCIO",
    "BICE", "INTERNACIONAL", "MERCADO PAGO", "TENPO", "MACH", "COPEC PAY",
    "BANCO EDWARDS",
]

# Palabras que indican campos en comprobantes bancarios
KEYWORDS_MONTO = ["monto", "total", "transferido", "transferencia", "pago", "importe"]
KEYWORDS_RUT = ["rut", "r.u.t"]
KEYWORDS_OPERACION = ["operacion", "operación", "n°", "numero", "número", "folio", "comprobante"]
KEYWORDS_ORIGEN = ["origen", "desde", "cuenta origen", "remitente", "de:"]
KEYWORDS_DESTINO = ["destino", "para", "cuenta destino", "destinatario", "a:"]

# ─── EXCEL ─────────────────────────────────────────────────────
EXCEL_COLUMNS = [
    "Fecha Mensaje", "Hora Mensaje", "Vendedor", "Cliente Detectado",
    "Factura(s)", "Monto Transferido", "Banco", "Cuenta Origen",
    "Cuenta Destino", "RUT", "Fecha Transferencia", "Hora Transferencia",
    "N° Operación", "Detalle Vendedor", "Texto OCR", "Archivo Imagen",
    "Estado", "Observación",
]

# Colores por estado (formato ARGB para openpyxl)
STATE_COLORS = {
    "LISTO PARA INGRESAR": "FF00C853",  # verde
    "FALTA DATO":          "FFFFEB3B",  # amarillo
    "FALTA MONTO":         "FFFFEB3B",
    "FALTA FACTURA":       "FFFFEB3B",
    "FALTA CLIENTE":       "FFFFEB3B",
    "DUPLICADO POSIBLE":   "FFEF5350",  # rojo
    "ABONO PARCIAL":       "FF42A5F5",  # azul
    "REVISAR OCR":         "FFBDBDBD",  # gris
}
