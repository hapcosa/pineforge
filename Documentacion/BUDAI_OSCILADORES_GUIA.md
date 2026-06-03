# BudAI Capital® — Guía de Osciladores + Prompt anti-fallas

> Documento maestro: qué podemos construir, los bloques reutilizables, y el prompt
> para que cualquier IA continúe SIN repetir los errores que ya detectamos.

---

## PARTE 1 — QUÉ PODEMOS HACER (capacidades)

### Bloques de construcción (motores) que ya dominamos
| Motor | Qué mide | Archivo de referencia |
|---|---|---|
| **WaveTrend** | ciclo/momentum (centro gravedad cíclico) | abyss, athenea, tidal |
| **COG Ehlers** | giro suavizado con menos lag | athenea, pulse |
| **Regression Slope** | pendiente/fuerza de tendencia | slope, athenea |
| **Squeeze (BB/KC)** | compresión de volatilidad → breakout | squeeze, coil |
| **Williams Vix Fix** | pánico/euforia (proxy VIX) | panic, athenea |
| **Money Flow (MFI+CMF+Delta)** | dinero institucional acum/dist | moneyflow, moneyflow_tide |

### Recursos visuales (la "caja de herramientas" estética)
- **Onda única** (Athenea): línea coloreada + línea blanca brillante encima + glow fading a 50.
- **Doble onda** (Nautilus/Tide): 2 líneas finas cruzadas + fill bicolor entre ellas.
- **Glow**: `plot` semitransparente (alpha 80-84) grosor 3 detrás de la línea fina (linewidth 1).
- **Fill degradado fading**: `fill(p, pMid, top_value, bottom_value, top_color, bottom_color)`
  con una transparencia al 55 y la otra al 100 → difuminado institucional.
- **Money Flow de fondo**: `plot.style_area` o `style_columns` con histbase=50, alpha alto.
- **Ribbons** (barras Nautilus): `plotchar "▬"` cada 2 barras (NO `▰` sólido), arriba y abajo.
- **Nodos de cruce**: doble `plotchar "•"` blanco (grande alpha 70 + pequeño sólido).
- **Señales**: doble `plotchar "•"` (glow grande + sólido pequeño), amarillo/rosa/verde neón.
- **Fibo sutiles**: `hline` 0.382/0.5/0.618 en morado `#9d6cff` alpha 86.
- **Dashboard tiny** + **marca de agua** `₿ BudAI Cripto`.

### Osciladores ya creados (12)
Squeeze · Coil · Abyss · Slope · Helix · Pulse · Panic · **Athenea** (híbrido top) ·
Tidal · Money Flow · Money Flow Tide. (+ Confluence Matrix en panel).

### Lo que aún podemos crear
- RSI + Stoch RSI Pro · Volume Delta/Order Flow · Reversal Cloud · Momentum Wave 3D.
- **Omni Oscillator**: selector de motor (WaveTrend/Slope/MoneyFlow/Squeeze/RSI) en uno solo.

---

## PARTE 2 — PALETAS OFICIALES

### Athenea (preferida)
- Alcista celeste `#00e5ff` · Bajista fucsia `#ff1e6e`
- Señal alcista amarillo neón `#ffff00` · Señal bajista rosa neón `#ff007f`
- Línea blanca brillante `#ffffff` · Fibo morado `#9d6cff` / `#b06aff`

### Nautilus (marina)
- Rápida azul `#2196f3` · Lenta roja `#f23645`
- Fill acumulación verde `#00e676` · distribución fucsia `#e040fb`
- Señal OS verde `#00e676` · OB amarillo `#ffeb00`

### Comunes
- Verde `#00e676` · Rojo `#ff1744` · Amarillo flúor `#ffea00`
- Marca de agua verde lima `#b6f400` · Fondo dashboard `#0b0e16`

---

## PARTE 3 — PROMPT ANTI-FALLAS (pegar a la IA)

```
Trabajo en BudAI Capital®, suite de osciladores Pine Script v6 para TradingView.
Continúa con MI estética y SIN repetir estos errores ya cometidos:

ERRORES PROHIBIDOS (NO repetir):
1. Barras/ribbons Nautilus: NUNCA usar "▰" (bloque sólido) en cada barra → crea
   franja gruesa pesada. USAR "▬" (segmento fino) cada 2 barras (bar_index % 2 == 0).
2. Líneas: NUNCA linewidth > 2. Las líneas principales van en linewidth 1.
   El glow es una capa aparte: plot semitransparente (alpha 80-84) grosor 3.
3. Círculos/señales: NUNCA plotshape(shape.circle) → sale gigante. SIEMPRE
   plotchar(cond, "•", ..., size=size.tiny). Para glow: doble plotchar (grande
   alpha 60-70 + pequeño sólido size.tiny).
4. Nodos de cruce: agregar círculo blanco con glow (doble plotchar "•" blanco)
   en CADA cruce de líneas. Fino, no invasivo.
5. NO saturar: un solo panel, sin backgrounds que manchen, difuminados al ~55-100
   de transparencia (degradado fading), no rellenos opacos.
6. NO escribir "(Paso X/Fase Y)" ni nombres de autores externos (BigBeluga,
   Nautilus, Artemis, LuxAlgo) en el código. Recrear lógica, no copiar.

REGLAS PINE v6 (CLAUDE.md):
- Sin ternario sobre tuplas. request.security con lookahead_off.
- Funciones de dibujo en scope global. not na(pivote) antes de usar.
- Variables de 1 letra como iterador local OK, pero NO "f" (colisiona). Usar fz, ob, etc.
- input.source(hlc3,...) da falso positivo en el linter del IDE pero compila en TV. Ignorar.

ESTÉTICA OBLIGATORIA (cada .pine):
- Header ASCII BudAI + "© BudAI Capital®".
- indicator("BudAI Capital® - [Nombre]", shorttitle = nombre completo, ...).
- Marca de agua: tabla 1×1 "₿ BudAI Cripto" color #b6f400, inferior derecha.
- Dashboard tiny (2 col, size.tiny, fondo #0b0e16, helper f_cell).
- Grupos de inputs con emoji ① ② ③ + grupo "✦ Marca de agua".
- Nombres en inglés con sinónimos creativos.

FLUJO DE TRABAJO:
- Un indicador a la vez. Esperar feedback visual (capturas) antes de seguir.
- Ser estricto, meticuloso, crítico visualmente. Buscar SIEMPRE los mejores parámetros.
- Español, directo, sin relleno.
```

---

## PARTE 4 — CHECKLIST VISUAL (antes de entregar cualquier oscilador)
- [ ] Líneas finas (linewidth 1), glow capa aparte sutil
- [ ] Ribbons = "▬" segmentado cada 2 barras (no "▰" sólido)
- [ ] Nodo blanco con glow en cruces
- [ ] Señales = plotchar "•" tiny doble-glow, colores neón
- [ ] Difuminado fading (no opaco), un solo panel
- [ ] Header + marca de agua + dashboard tiny
- [ ] Sin rastro de autores externos, sin "(Paso/Fase)"
- [ ] Compila en TradingView (ignorar falsos positivos del linter)
```
