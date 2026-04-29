# CLAUDE.md

## Proyecto: DVU COMPROBANTES BOT

Actúa como un ingeniero senior full-stack experto en Python, OCR, automatización empresarial, procesamiento documental, WhatsApp parsing, Excel automation y RPA.

Tu tarea es construir completamente un sistema funcional llamado:

**DVU COMPROBANTES BOT**

No entregues teoría. Construye el proyecto con código real, modular, funcional y listo para ejecutar en Windows.

---

## Contexto

DVU Spa es una empresa familiar distribuidora de artículos de ferretería.

Existe un grupo de WhatsApp llamado:

**COMPROBANTES TRANSF.**

En este grupo, vendedores en terreno envían pagos de clientes. Cada mensaje puede contener:

- Screenshot del comprobante de transferencia.
- Nombre del cliente.
- Número(s) de factura.
- Detalle del pago.
- Abonos parciales.
- Pagos de varias facturas juntas.

Ejemplos reales:

```text
Pago Facturas 33135 y 33134 MARES DEL SUR
Evelin Soledad Bergmann Gallardo, factura: 33780

Los comprobantes bancarios suelen contener:

Monto transferido.
Banco.
RUT.
Fecha.
Hora.
Número de operación.
Cuenta origen.
Cuenta destino.
Objetivo del MVP

Crear un sistema local en Python que:

Lea un archivo exportado de WhatsApp .txt.
Lea una carpeta con imágenes de comprobantes.
Aplique OCR.
Extraiga datos relevantes desde texto e imagen.
Cruce la información.
Genere un Excel profesional para cobranza.
Stack obligatorio

Usar Python 3.11+.

Librerías:

pandas
openpyxl
easyocr
opencv-python
pillow
regex
pathlib
logging
Estructura obligatoria

Crear esta estructura:

dvu_bot/
  main.py
  config.py
  ocr.py
  parser_whatsapp.py
  extractor.py
  excel.py
  validator.py
  requirements.txt
  README.md

  logs/

  input/
    chat.txt
    media/

  output/
Datos a extraer desde WhatsApp

Desde el texto del mensaje:

Fecha mensaje.
Hora mensaje.
Nombre vendedor.
Cliente.
Factura(s).
Comentario original.
Archivo adjunto asociado, si existe.
Datos a extraer desde imagen del comprobante

Desde OCR:

Monto transferido.
Banco.
Fecha transferencia.
Hora transferencia.
Cuenta origen.
Cuenta destino.
RUT.
Número de operación.
Texto OCR completo.
Excel final

Generar un archivo:

output/comprobantes_dvu.xlsx

Columnas obligatorias:

Fecha Mensaje
Hora Mensaje
Vendedor
Cliente Detectado
Factura(s)
Monto Transferido
Banco
Cuenta Origen
Cuenta Destino
RUT
Fecha Transferencia
Hora Transferencia
N° Operación
Detalle Vendedor
Texto OCR
Archivo Imagen
Estado
Observación
Estados automáticos

El sistema debe asignar estados:

LISTO PARA INGRESAR
FALTA DATO
FALTA MONTO
FALTA FACTURA
FALTA CLIENTE
DUPLICADO POSIBLE
ABONO PARCIAL
REVISAR OCR
Colores en Excel

Aplicar color por estado:

Verde: LISTO PARA INGRESAR
Amarillo: FALTA DATO, FALTA FACTURA, FALTA CLIENTE, FALTA MONTO
Rojo: DUPLICADO POSIBLE
Azul: ABONO PARCIAL
Gris: REVISAR OCR
Reglas de extracción
Montos

Detectar formatos como:

$510.459
510459
$ 162.792
68.282

Normalizar a número entero chileno.

Facturas

Detectar formatos como:

factura 33780
facturas 33135 y 33134
F33780
Fac: 33780
Factura: 33780

Si hay varias facturas, guardarlas separadas por coma.

Cliente

Detectar el cliente desde el texto del vendedor.

Si no se puede detectar con confianza:

REVISAR
Abonos

Detectar palabras como:

abono
saldo
parcial
parte
cuota

Y marcar estado:

ABONO PARCIAL
Duplicados

Detectar posibles duplicados usando:

Número de operación.
Monto.
Fecha transferencia.
Cliente.
Factura.

Si existe coincidencia fuerte:

DUPLICADO POSIBLE
Comportamiento del sistema

El sistema debe ejecutarse con:

python main.py

Debe leer por defecto:

input/chat.txt
input/media/

Debe guardar:

output/comprobantes_dvu.xlsx
logs/dvu_bot.log
Requisitos de calidad
No inventar datos.
Si un dato no se puede leer, marcar REVISAR.
Mantener texto OCR completo para auditoría.
No borrar archivos originales.
Guardar logs.
Código limpio y comentado.
Separar responsabilidades por archivo.
Manejar errores sin romper ejecución.
Compatible con Windows.
Preparado para futura integración con WhatsApp Business API o RPA.
Entregables

Debes crear:

main.py
config.py
ocr.py
parser_whatsapp.py
extractor.py
validator.py
excel.py
requirements.txt
README.md

Cada archivo debe tener código completo, no pseudocódigo.

Instrucción final

Construye ahora el proyecto completo.

Primero crea la estructura de carpetas.

Luego genera cada archivo con código funcional.

Finalmente entrega instrucciones de instalación y uso para Windows.
