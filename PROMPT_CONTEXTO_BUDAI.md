# PROMPT DE CONTEXTO — Proyecto BudAI Capital® (Suite de indicadores Pine Script)

> Copia y pega este bloque completo a la otra IA para que continúe el trabajo
> exactamente con nuestros parámetros, estética y reglas. No improvisar fuera de esto.

---

## QUIÉN SOY / QUÉ HACEMOS
Estoy creando **BudAI Capital®** (alias "BudAI Cripto"), mi propia marca de indicadores
de trading en **Pine Script v6** para TradingView. El objetivo es recrear desde cero (lógica
propia, sin copiar código ajeno) los mejores indicadores de LuxAlgo, BigBeluga, LazyBear, etc.,
dándoles un **sello visual e identidad únicos**, para luego combinarlos en sistemas de confluencia.

Trabajamos **uno por uno**, yo reviso cada `.pine` en TradingView y doy feedback visual
(mando capturas). La IA corrige hasta que quede perfecto, luego pasamos al siguiente.

---

## REGLAS DE ORO (innegociables)
1. **Pine Script v6** siempre. Respetar TODAS las reglas del archivo `CLAUDE.md` del repo:
   - Sin ternario/if multilínea sin paréntesis.
   - `request.security` con `lookahead=barmerge.lookahead_off`; NUNCA ternario sobre tuplas.
   - Funciones de dibujo (plot/bgcolor) en scope global.
   - `not na(pivote)` antes de usarlo; limpiar boxes/lines antes de reasignar.
   - Verificar `array.size()` antes de acceder.
   - Las funciones NO pueden reasignar variables `var` globales (usar valores de retorno o arrays).
2. **No dejar rastro** de autores originales (BigBeluga, Artemis/a_jabbaroff, LuxAlgo). Recrear
   la LÓGICA, no el código. Nada de licencias MPL ni nombres de autor ajenos en el archivo.
3. Cada indicador es un `.pine` nuevo independiente. No tocar los que ya funcionan.

---

## NUESTRA ESTÉTICA (la "base BudAI" — aplicar a TODO)
- **Header ASCII obligatorio** al inicio de cada `.pine` (logo en bloque):
```
//@version=6
// ██████╗ ██╗   ██╗██████╗  █████╗ ██╗
// ██╔══██╗██║   ██║██╔══██╗██╔══██╗██║
// ██████╔╝██║   ██║██║  ██║███████║██║
// ██╔══██╗██║   ██║██║  ██║██╔══██║██║
// ██████╔╝╚██████╔╝██████╔╝██║  ██║██║
// ╚═════╝  ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝
//         C R I P T O   ·   T R A D I N G   C A P I T A L
// ────────────────────────────────────────────────────────────────────────────
//  BudAI Capital® - [Nombre del indicador]
//  [descripción corta de 2-3 líneas]
//  (c) BudAI Capital® — Pine v6
// ────────────────────────────────────────────────────────────────────────────
```
- **Nombre del indicador**: `indicator("BudAI Capital® - [Nombre Completo]", shorttitle="BudAI Capital® - [Nombre Completo]", ...)`.
  El shorttitle DEBE ser el nombre completo (no abreviado). Nombres en inglés, descriptivos,
  con sinónimos creativos (ej: "Volatility Squeeze Momentum", "Abyss Wave Oscillator").
- **Marca de agua** en el chart: tabla 1×1 con `₿ BudAI Cripto`, color `#b6f400` (verde lima,
  transparencia ~35), posición configurable (default Inferior Derecha), fondo transparente.
  Grupo de inputs "✦ Marca de agua" con showWM/wmPos/wmCol.
- **Paleta cyberpunk neón** (electric/flúor). Según el indicador:
  - Verde `#00e676` / Rojo `#ff1744` (bull/bear clásico).
  - Celeste `#00e5ff` / Magenta `#ff1e6e` o Morado `#b388ff` (alternativa).
  - Celeste `#00bcd4` / Naranja `#ff9800` (otra combinación cyberpunk).
  - Amarillo flúor `#ffea00` o `#ffff00` y gris `#9e9e9e` para señales secundarias.
  - Dorado `#ffb300` para líneas de equilibrio/EQ.
- **Onda con sombra degradada** (estilo Neptune/BigBeluga): línea blanca recorriendo la onda
  + `fill()` degradado hacia el centro (verde si arriba/rojo si abajo), `top_color`/`bottom_color`
  con transparencias distintas para el efecto difuminado. NUNCA histograma de barras si se puede onda.
- **Glow neón**: capa(s) extra de `plot` o `fill` semitransparente alrededor de la línea (profundidad).
- **Líneas finas** (linewidth 1-2). Líneas de referencia con transparencia alta.
- **Señales = círculos MUY pequeños**: usar `plotchar(cond, "•", location.absolute, ...)` con
  `size=size.tiny` (NO plotshape circle, que sale gigante). Colores neón flúor que se distingan.
  Para señales fuertes vs simples: círculo "•" vs "×".
- **Divergencias** = círculos tiny amarillo (alcista) / gris (bajista), SIN líneas de trazo
  conectoras (las quité porque saturaban).
- **Dashboard minimalista tiny**: `table` 2 columnas, TODO `text_size=size.tiny`, fondo
  `color.new(#0b0e16, 14)`, frame del color de acento. Clave izq gris `#90a4ae` / valor der coloreado.
  Función helper `f_cell(t, r, k, v, vc)`. Título con fondo `#1b2030`.
- **Sin backgrounds que "manchen"** el chart. Nada de `bgcolor` saturado.
- **NO escribir "(Paso X · Fase Y)"** ni referencias al plan dentro del `.pine` (queda feo).

---

## CONVENCIONES DE CÓDIGO QUE USAMOS
- Inputs agrupados con emojis numerados: `G_CORE = "① Núcleo"`, etc. + grupo "✦ Marca de agua".
- Funciones helper estándar al final: `f_pos(s)` (posición dashboard), `f_wmPos(s)` (posición marca agua),
  `f_cell(...)` (celda dashboard).
- Señales confirmadas a cierre con `barstate.isconfirmed` (no repaint).
- MTF con `request.security(..., lookahead=barmerge.lookahead_off)`.
- Para osciladores: normalización 0-100 o ±100, niveles OB/OS configurables, fibo 0.382/0.5/0.618.
- UDT (`type`) para objetos complejos (OB, FVG, sesiones, etc.).

---

## LO QUE YA ESTÁ HECHO (no rehacer salvo que yo lo pida)
**Carpeta `Osciladores/`:**
- `budai_squeeze.pine` — "Volatility Squeeze Momentum" (BB vs Keltner + momentum onda).
- `budai_coil.pine` — "Compression Coil" (squeeze, onda degradada).
- `budai_abyss.pine` — "Abyss Wave Oscillator" (WaveTrend, círculos OB/OS, celeste/naranja).
- `budai_slope.pine` — "Regression Slope Engine" (pendiente regresión, onda verde/rojo).
- `budai_helix.pine` — "Helix Wave Pro" (WaveTrend+HyperWave, sombras Nautilus).
- `budai_pulse.pine` — "Pulse Flow Oscillator" (WaveTrend+COG+MoneyFlow+MTF).
- `budai_panic.pine` — "Panic & Euphoria Radar" (Williams Vix Fix, onda difuminada).

**Raíz (overlay/estructura):**
- `budai_structure.pine` — "Smart Market Structure" (BOS/CHoCH/OB/FVG/EQH-EQL).
- `budai_orderblocks.pine` — "Volumetric Order Blocks" (OB con máquina de estados).
- `budai_smc.pine` — "Smart Money Matrix" (SMC completo con máquina de estados + sweeps). ← más reciente.
- `ict_ny_scalper.pine` + `ict_nyc_oscilator.pine` — sistema ICT sesión NY (anterior, ya funcional).

---

## CLAVE TÉCNICA APRENDIDA (Order Blocks / Estructura)
El error común: crear OB en CADA pivote → cajas por todos lados. La forma CORRECTA (BigBeluga):
- **Máquina de estados** con `var int trend`, niveles vivos `bosHi`/`bosLo` que se actualizan al
  último swing. Ruptura confirmada por CIERRE (`close > bosHi`).
- BOS = ruptura a favor de la tendencia; CHoCH = ruptura en contra (cambio de carácter).
- **OB = la vela extrema del impulso** previo a la ruptura (buscar con loop `f_findExtreme`),
  NO la vela del pivote. Demanda en el mínimo, oferta en el máximo.
- **Sweep** = la mecha cruza el nivel pero el cierre NO confirma (trampa de liquidez), marca "x".
- Mitigación por Close/Wick/Avg. Ocultar OB solapados.

---

## PLAN GENERAL (orden de re-creación)
**Fase 1 — Osciladores** ✅ COMPLETA (7 listos, ver arriba).
**Fase 2 — Estructura SMC** (en curso): Smart Market Structure ✅, Order Blocks ✅, SMC Matrix ✅.
  Falta opcional: Liquidity dedicado (BSL/SSL, PDH/PDL, barridos).
**Fase 3 — Tendencia + señales**: motor tipo "Signals & Overlays" (confirmation/contrarian/exit),
  SuperTrend/Trend Catcher, Range Filter, Market Waves (▲▼ en bandas).
**Fase 4 — Combinación**: indicador "Confluence" que une oscilador + estructura + tendencia en un
  score, alertas combinadas, presets por activo.

Indicadores de referencia a recrear (lógica, no código): WaveTrend, Squeeze Momentum (LazyBear);
Nautilus, Regression Slope, Equilibrium Shift, Market Waves, SMC (BigBeluga); Signals&Overlays,
Oscillator Matrix, SMC, Signal Forge (LuxAlgo); Williams Vix Fix (ChrisMoody); Order Blocks,
Harmonic (LonesomeTheBlue); SuperTrend, Range Filter (DonovanWall).

---

## CÓMO TRABAJAR CONMIGO
- Hacer UN indicador a la vez, esperar mi feedback visual (mando capturas del chart).
- Verificar siempre que no haya errores de compilación reales (el linter del IDE da falsos
  positivos con emojis/acentos en comentarios — ignorar esos, lo que importa es que compile en TV).
- Si subo un indicador de referencia, adaptarlo a nuestra estética/sello, sin rastro del original.
- Preguntarme antes de avanzar de paso. Mantener todo lo ya trabajado intacto.
- Hablar en español. Ser directo, sin relleno.
```
