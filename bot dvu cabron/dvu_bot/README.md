# DVU COMPROBANTES BOT

Automatiza el procesamiento de comprobantes de transferencia enviados al grupo **COMPROBANTES TRANSF.** de WhatsApp y genera un Excel profesional listo para cobranza.

## Flujo

```
chat.txt (WhatsApp export) + input/media/*.jpg
            │
            ▼
   Parser WhatsApp  ───►  OCR (EasyOCR)  ───►  Extractor (regex)
            │
            ▼
   Validador (estados + duplicados)
            │
            ▼
   output/comprobantes_dvu.xlsx
```

## Instalación (Windows)

1. Instala **Python 3.11+** desde python.org (marca *Add to PATH*).
2. Abre `PowerShell` en la carpeta `dvu_bot/`.
3. Crea entorno virtual e instala dependencias:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
```

> La primera ejecución de EasyOCR descarga modelos (~100 MB). Demora unos minutos.

## Uso

### 1. Exporta el chat de WhatsApp

En la app WhatsApp → grupo **COMPROBANTES TRANSF.** → *Más opciones* → *Exportar chat* → **Incluir archivos**.

Recibirás un `.zip` con:
- `_chat.txt` (o similar)
- múltiples imágenes `IMG-*.jpg`

### 2. Coloca los archivos

```
dvu_bot/
  input/
    chat.txt          ← renombra el export a chat.txt
    media/
      IMG-20250315-WA0001.jpg
      IMG-20250315-WA0002.jpg
      ...
```

### 3. Ejecuta

```powershell
python main.py
```

### 4. Revisa el resultado

`output/comprobantes_dvu.xlsx`

## Columnas del Excel

| Campo | Fuente |
|---|---|
| Fecha / Hora Mensaje | WhatsApp |
| Vendedor | WhatsApp (remitente) |
| Cliente Detectado | Texto del vendedor |
| Factura(s) | Texto del vendedor |
| Monto Transferido | OCR imagen |
| Banco | OCR imagen |
| Cuenta Origen / Destino | OCR imagen |
| RUT | OCR imagen |
| Fecha / Hora Transferencia | OCR imagen |
| N° Operación | OCR imagen |
| Detalle Vendedor | Texto completo WhatsApp |
| Texto OCR | OCR bruto (auditoría) |
| Archivo Imagen | Nombre del JPG |
| Estado | Automático |
| Observación | Automático |

## Estados y colores

| Estado | Color |
|---|---|
| LISTO PARA INGRESAR | Verde |
| FALTA MONTO / FALTA FACTURA / FALTA CLIENTE / FALTA DATO | Amarillo |
| DUPLICADO POSIBLE | Rojo |
| ABONO PARCIAL | Azul |
| REVISAR OCR | Gris |

## Estructura del proyecto

```
dvu_bot/
  main.py                 # entrada
  config.py               # rutas, regex, constantes
  ocr.py                  # EasyOCR + preprocesado OpenCV
  parser_whatsapp.py      # parseo chat.txt
  extractor.py            # regex para facturas, montos, RUT, bancos, etc.
  validator.py            # estados + detección de duplicados
  excel.py                # Excel con formato condicional
  requirements.txt
  README.md
  logs/dvu_bot.log
  input/chat.txt
  input/media/
  output/comprobantes_dvu.xlsx
```

## Logs

Todas las ejecuciones se registran en `logs/dvu_bot.log` (no se rota automáticamente; borra si crece).

## Reglas de negocio

- **Montos**: formatos `$510.459`, `510.459`, `510 459`, `510459`. Rango válido 500 → 999.999.999.
- **Facturas**: `factura 33780`, `facturas 33135 y 33134`, `F33780`, `Fac: 33780`. Múltiples separadas por coma.
- **Abonos**: detecta `abono`, `saldo`, `parcial`, `parte`, `cuota`, `adelanto`, `anticipo`.
- **Duplicados**: misma tripleta (N° operación, monto, fecha transferencia).
- **Sin invento**: si un dato no se lee con confianza, queda vacío + Estado **FALTA ...** o **REVISAR**.

## Extensión futura

- Integración con WhatsApp Business API (reemplazar `parser_whatsapp.py` por webhook).
- RPA de ingreso al ERP (leer Excel y empujar al sistema de cobranza).
- GPU para OCR: `OCR_GPU = True` en `config.py` si tienes CUDA.
- Fuzzy matching cliente contra base de clientes del ERP.

## Troubleshooting

- **`ModuleNotFoundError: easyocr`** → activaste el venv? `pip install -r requirements.txt`.
- **OCR muy lento** → primera corrida descarga modelos. Luego ~2–4 s por imagen en CPU.
- **No detecta adjuntos** → verifica que `chat.txt` tiene líneas `<adjunto: IMG-...>` o `IMG-...jpg (archivo adjunto)`.
- **Encoding raro en chat.txt** → abre con Notepad → *Guardar como* → UTF-8.
