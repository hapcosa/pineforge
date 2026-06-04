# PROMPT MAESTRO — Continuar proyecto BudAI Capital® (chat nuevo)

> Copia y pega TODO este bloque al iniciar el chat nuevo. Reúne contexto, estética,
> parámetros, lo hecho y lo que falta. Objetivo del nuevo chat: crear MOTORES NUEVOS
> de osciladores con nuestra estética ya definida, sin repetir errores.

---

## 0 · QUIÉN SOY / QUÉ HACEMOS
Construyo **BudAI Capital®** (alias "BudAI Cripto"), mi marca propia de indicadores de
trading en **Pine Script v6** para TradingView. Recreo desde cero (lógica propia, sin
copiar código) los mejores indicadores de LuxAlgo, BigBeluga, LazyBear, Zeiierman, etc.,
con un sello visual e identidad únicos, para luego combinarlos en sistemas de confluencia.

Soy obsesivo con la estética. Reviso cada `.pine` en TradingView y mando capturas como
feedback. La IA corrige hasta que quede premium, luego pasamos al siguiente. Hablar
español, directo, sin relleno. Ser estricto, meticuloso y crítico visualmente.

Carpeta del repo: `c:\Users\Lenovo\OneDrive\Desktop\pinescript indicadores\pineforge`
Los osciladores van en la subcarpeta `Osciladores/`.

---

## 1 · ESTÉTICA OFICIAL "ATHENEA" (la base — NO desviarse)
Mi estética favorita es la del archivo `Osciladores/budai_athenea_oscillator.pine` y
`budai_omni.pine`. Replicar SIEMPRE este estilo:

- **Onda única** principal: línea coloreada (linewidth 1-2) + **línea blanca brillante**
  encima (linewidth 1) que resalta la cresta.
- **Glow fading**: `fill(pOsc, pMid, top_value=100, bottom_value=50, top_color=alpha55,
  bottom_color=alpha100)` → degradado que se desvanece hacia el centro 50. Institucional.
- **Trigger** (línea de señal) blanca tenue (alpha 35).
- **Money Flow de fondo**: `plot.style_columns` histbase=50, alpha 76-80.
- **Fibo sutiles**: hline 0.382/0.5/0.618 en morado `#9d6cff`/`#b06aff` alpha 70-86.
- **Señales** = doble `plotchar "•"`: grande alpha 65 (glow) + pequeño sólido size.tiny.
- **Nodos de cruce** = doble `plotchar "•"` blanco (grande alpha 70 + pequeño sólido),
  dibujados en `location.absolute` con el VALOR del oscilador (caen exacto en el cruce).
- **Hyper Wave** opcional: 2ª onda de presión doble-suavizada con kernels (0.8 / 0.3).
- **Dashboard tiny** (2 columnas, todo size.tiny, fondo `#0b0e16` alpha 12-14, helper f_cell).
- **TODO color configurable** vía input.color (líneas, trigger, brillo, señales, nodos, fibo).

### PALETA NEÓN (bull = celeste/naranja · bear = rojo/morado/fucsia)
- Alcista celeste `#00e5ff` · Alcista 2 naranja `#ff9100`
- Bajista fucsia `#ff1e6e` · Bajista 2 morado `#b388ff` · rojo `#ff1744`
- Señal alcista amarillo neón `#ffff00` · Señal bajista rosa neón `#ff007f`
- Verde `#00e676` · Amarillo flúor `#ffea00` · Blanco brillo `#ffffff`
- Marca de agua verde lima `#b6f400` · Fondo dashboard `#0b0e16` · título `#1b2030`
- Opción degradado dual con `color.from_gradient` (celeste→naranja / fucsia→morado).

---

## 2 · ERRORES PROHIBIDOS (ya cometidos, NO repetir)
1. **Ribbons/barras Nautilus**: NUNCA `▰` (bloque sólido) en cada barra → franja gruesa
   pesada. USAR `▬` cada 2 barras (`bar_index % 2 == 0`). Segmentos finos espaciados.
2. **Líneas**: NUNCA linewidth > 2 en la principal. Glow = capa aparte (plot alpha 80-84
   grosor 3). Las líneas Nautilus van en linewidth 1.
3. **Círculos**: NUNCA `plotshape(shape.circle)` → sale gigante. SIEMPRE `plotchar "•"`
   size.tiny. Glow = doble plotchar.
4. **Nodos**: deben caer EN el cruce (usar el valor del oscilador en location.absolute).
5. **No saturar**: un solo panel, sin backgrounds que manchen, difuminados 55-100 transp.
6. **No dejar rastro**: jamás escribir nombres de autores externos (BigBeluga, Nautilus,
   Artemis, a_jabbaroff, LuxAlgo, Neptune) ni licencias MPL en el código. Recrear lógica.
7. **No escribir "(Paso X · Fase Y)"** dentro del .pine.

---

## 3 · REGLAS PINE v6 (de CLAUDE.md del repo)
- Sin ternario/if multilínea sin paréntesis. Sin ternario sobre tuplas.
- `request.security(..., lookahead=barmerge.lookahead_off)`.
- Funciones de dibujo (plot/bgcolor/fill) en scope global.
- `not na(pivote)` antes de usar. Verificar `array.size()` antes de acceder.
- Las funciones NO reasignan variables `var` globales (usar retorno o arrays por referencia).
- Iteradores de 1 letra OK como locales PERO no `f` (colisiona con funciones f_). Usar fz, ob, o.
- `input.source(hlc3,...)` da FALSO POSITIVO en el linter del IDE pero compila en TV. Ignorar.
- El linter del IDE colapsa archivos con emojis/acentos (falso positivo). Lo que importa
  es que compile en TradingView. Si hay error REAL, el usuario manda texto + línea exacta.

---

## 4 · ESTRUCTURA ESTÁNDAR DE CADA .pine
```
//@version=6
// [HEADER ASCII BudAI — bloque de 6 líneas + "CRIPTO · TRADING CAPITAL"]
// ────────────────────────────────────────────────────────────────────
//  BudAI Capital® - [Nombre]
//  [descripción 2-3 líneas]
//  (c) BudAI Capital® — Pine v6
// ────────────────────────────────────────────────────────────────────
indicator("BudAI Capital® - [Nombre Completo]", shorttitle="BudAI Capital® - [Nombre Completo]", overlay=false, ...)

// GRUPOS con emoji: G_CORE="① ...", ... , G_VIS="④ Estética", G_WM="✦ Marca de agua"
// INPUTS (núcleo · señales · niveles · estética todo configurable · marca de agua)
// CÁLCULO (f_norm 0..100, motores)
// NIVELES (hline fibo + OB/OS)
// PLOTS (money flow fondo + glow fading + onda + brillo blanco + cuerpo)
// SEÑALES + NODOS (plotchar "•" doble glow)
// DASHBOARD tiny (f_pos, f_cell)
// MARCA DE AGUA (f_wmPos, tabla 1×1 "₿ BudAI Cripto" #b6f400 inferior derecha)
// ALERTAS (alertcondition)
```
Nombres en inglés, sinónimos creativos (no genéricos).

---

## 5 · LO QUE YA ESTÁ HECHO (NO rehacer)

### Osciladores (carpeta `Osciladores/`) — 13
| Archivo | Nombre | Motor |
|---|---|---|
| budai_squeeze | Volatility Squeeze Momentum | BB/KC squeeze |
| budai_coil | Compression Coil | squeeze onda |
| budai_abyss | Abyss Wave Oscillator | WaveTrend |
| budai_slope | Regression Slope Engine | pendiente |
| budai_helix | Helix Wave Pro | WaveTrend+HyperWave |
| budai_pulse | Pulse Flow Oscillator | WaveTrend+COG+MoneyFlow |
| budai_panic | Panic & Euphoria Radar | Williams Vix Fix |
| budai_athenea_oscillator | Athenea Oscillator ⭐ | híbrido (WT+Slope+COG+Sqz+Vix) — ESTÉTICA REFERENCIA |
| budai_tidal | Tidal Oscillator | doble WaveTrend (Nautilus) |
| budai_moneyflow | Smart Money Flow | MFI+CMF+Delta (Athenea) |
| budai_moneyflow_tide | Smart Money Flow Tide | doble MFI (Nautilus) |
| budai_omni | Omni Oscillator ⭐ | SELECTOR: WaveTrend/Slope/MoneyFlow/Squeeze/RSI + COG + HyperWave |

### Overlay / SMC / tendencia (raíz) — pausados, dejan que desear (pulir después)
budai_structure, budai_orderblocks, budai_smc, budai_trend, budai_signals,
budai_marketwaves, budai_confluence, ict_ny_scalper, ict_nyc_oscilator.

### Docs en el repo
- `BUDAI_OSCILADORES_GUIA.md` — capacidades + paletas + prompt anti-fallas + checklist.
- `PROMPT_CONTEXTO_BUDAI.md` — contexto general.
- `smcbb.pine` — referencia BigBeluga SMC (solo lógica, no copiar).

---

## 6 · LO QUE FALTA — MOTORES NUEVOS (objetivo del chat nuevo)
Crear estos osciladores con motores que aún NO tenemos, estética Athenea, uno por uno:

1. **Volume Delta / Order Flow** ⭐ (prioridad) — presión real compra vs venta en columnas
   grandes (delta acumulado intrabar). El más institucional que falta.
2. **Reversal Cloud** — nube de reversión (tipo Zeiierman): banda que cambia de color +
   señales de agotamiento.
3. **Stoch RSI Pro** — RSI + estocástico fusionado para timing fino, bandas dinámicas.
4. **Momentum Wave 3D** — momentum multi-capa con efecto profundidad (varias ondas).
5. **TSI / True Strength** — índice de fuerza verdadera, doble suavizado.
6. (Opcional) **Fisher Transform**, **Schaff Trend Cycle**, **Ultimate RSI**.

### Top 5 fuentes de referencia (consultar lógica)
LuxAlgo (Oscillator Matrix), BigBeluga (Nautilus), LazyBear (WaveTrend/Squeeze),
Zeiierman (Reversal/Trend), AlgoAlpha/QuantVue (multi-motor).

### Después de los motores
- **Combinar** osciladores en sistemas de confluencia (volver a Fase 4 pero bien).
- **Pulir** la suite SMC/tendencia/overlay (Fase 2 y 3) que quedó a medias.
- Manual final de uso + presets por activo (BTC, NASDAQ, EURUSD).

---

## 7 · CÓMO ARRANCAR EL CHAT NUEVO
Empezar por el **Volume Delta / Order Flow** con estética Athenea. Confirmar conmigo
el plan corto (qué mide, cómo se ve) y ejecutar. Un indicador a la vez, esperar mis
capturas, corregir hasta premium. Mantener TODO lo ya hecho intacto.
```
