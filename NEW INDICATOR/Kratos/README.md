# BudAI Capital® — Kratos · workspace de emulación

Carpeta aislada para **recrear el indicador comercial "Neptune® - Signals™ [2.5]"**
(caja negra, sin fuente) como producto propio **BudAI Capital® - Kratos**, pieza por
pieza. Aquí solo vive el estudio/emulación; el ensamblaje final llega al cierre.

> "Neptune" = nombre del producto ajeno → **prohibido en el código final** (regla #6).
> Solo se usa como referencia entre paréntesis para rastrear qué emula cada pieza.

## Estado

Orden de trabajo (alfabético, overlays): **Kumo → Line → Reversal Zones → Trend Catcher
→ Trend Tracer** → luego motor de señales, TP/SL, dashboard → ensamblaje final.

| Pieza | Archivo | Estado |
|---|---|---|
| 1 · Trail | `BudAI_Kratos_Trail.pine` | **CERRADA** ✅ — kernel rational-quadratic + banda ATR + glow Athenea. Match visual en 15m y 1h. Params: h15 · r1 · win50 · atr9 · bMult1.5 · cloudW1.2 · nube al precio. |
| 2 · Kumo | `BudAI_Kratos_Kumo.pine` | **v0.2 — casi cerrado** (nube entre 2 MAs suaves; Ichimoku clásico DESCARTADO). Familia correcta, cerca. EMA·fast7·slow21. Overlay opcional. |
| 3 · Line | `BudAI_Kratos_Line.pine` | **v0.1 — en cotejo** (MA suave + MTF). Hipótesis "centro del kernel" DESCARTADA: Neptune Line es MA lenta/laggy (probar EMA·~50+). Pendiente length final. |
| 4 · Reversal Zones | `BudAI_Kratos_ReversalZones.pine` | **CERRADA** ✅ — bandas de volatilidad onduladas + borde brillante + degradado glow. Bollinger-extreme: StdDev·100·**factor 2.3** (= "1.4" de la referencia)·SMA20·zoneW1. Overlay opcional. |

| 5 · Trend Catcher | `BudAI_Kratos_TrendCatcher.pine` | **CERRADA** ✅ — SuperTrend ATR verde/rojo (escalonado confirmado) + región en degradado. factor 5. Overlay opcional. |
| 6 · Trend Tracer | `BudAI_Kratos_TrendTracer.pine` | **CERRADA** ✅ — mismo SuperTrend que el Catcher, azul/naranja, factor 3.1. Overlay opcional. |
| 7 · Motor de señales | `BudAI_Kratos_Signals.pine` | **v0.1 — en construcción** (oscilador WaveTrend → flechas entrada/salida; modos Oscillator / Confirmation+Exits; Sensitivity/Tuner). El núcleo del pack. |

> **Estándar estético (v glow-fading):** todas las piezas usan ahora relleno en **degradado**
> (`fill` con top_value/bottom_value, núcleo opaco → fade) + **glow multicapa**. Aplicado a
> Trail, Kumo, Line y Reversal Zones.

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
