# BudAI Capital® — Kratos · workspace de emulación

Carpeta aislada para **recrear el indicador comercial "Neptune® - Signals™ [2.5]"**
(caja negra, sin fuente) como producto propio **BudAI Capital® - Kratos**, pieza por
pieza. Aquí solo vive el estudio/emulación; el ensamblaje final llega al cierre.

> "Neptune" = nombre del producto ajeno → **prohibido en el código final** (regla #6).
> Solo se usa como referencia entre paréntesis para rastrear qué emula cada pieza.

## Estado

| Pieza | Archivo | Estado |
|---|---|---|
| 1 · Trail | `BudAI_Kratos_Trail.pine` | **v0.3 — hipótesis** (kernel rational-quadratic + banda ATR + glow Athenea). Descartados SuperTrend (escalonado) y MA simple (no cuadró). Pendiente: igualar bandwidth `h`. |

> **Estética/regla #6:** el `.pine` lleva header ASCII BudAI + legend `BudAI Capital® - Kratos`
> + paleta Athenea + marca de agua. El nombre del producto de referencia **NO** aparece en
> el código (regla #6); solo aquí, como nota de rastreo de qué emula cada pieza.

## Cómo usar (cotejo visual = leer los parámetros reales)

1. En TradingView, **aísla el Neptune Trail**: Signal Mode `Ninguno`, ML Exit
   desmarcado, Present/Filters `Ninguno`, Candle Coloring `Ninguno`, TP/SL `Ninguno`,
   Smart Dashboard desmarcado, y en *Indicator Overlays* deja **solo Neptune Trail ✓**.
2. Añade **`BudAI_Kratos_Trail.pine`** al mismo gráfico (colores neón a propósito,
   para distinguirlo del azul/rojo de Neptune).
3. Ajusta en Kratos: **Sensitivity**, **ATR length**, **Grosor de la nube** hasta que
   la banda de Kratos **se solape** con la de Neptune (mismos flips, mismo despegue del
   precio).
4. Anota qué valores cuadraron → esos son los **parámetros reales** de la pieza.

## Test diagnóstico (qué familia matemática es)

Mueve la **Sensitivity** de Neptune (Pilot en `Manual`) de bajo a alto:
- La banda **se aleja proporcional** del precio → es **multiplicador ATR** (SuperTrend/Keltner ✔ hipótesis actual).
- Cambia la **suavidad/lag** sin alejarse → es **kernel/periodo** (habría que cambiar de familia).

## Doble destino (más adelante)

Cuando una pieza cuadre: gemelo Python en `KryptoLab/` + test de paridad, y al final
alertas con el **JSON canónico BudAI** (`side`+`symbol`+`risk{}`). La optimización
queda **aparcada** hasta tener el pack ensamblado.
