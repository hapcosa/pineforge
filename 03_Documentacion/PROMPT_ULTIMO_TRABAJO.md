# PROMPT — Continuar lo ÚLTIMO de BudAI Capital® (Omni + motores nuevos)

> Pega este bloque en el chat nuevo. Resume exactamente dónde quedamos y qué sigue.

---

## CONTEXTO RÁPIDO
Soy **BudAI Capital®** ("BudAI Cripto"), creo osciladores Pine Script v6 para TradingView
con estética propia. Trabajamos uno a la vez; reviso en TV y mando capturas. Español,
directo, estricto, meticuloso, crítico visualmente. Repo:
`c:\Users\Lenovo\OneDrive\Desktop\pinescript indicadores\pineforge` (osciladores en `Osciladores/`).

⚠️ ANTES DE EMPEZAR: leer también `PROMPT_NUEVO_CHAT_BUDAI.md` y `BUDAI_OSCILADORES_GUIA.md`
en el repo — tienen la estética completa, paletas y errores prohibidos. Este archivo es
el "dónde quedamos" más reciente.

---

## LO ÚLTIMO QUE ESTÁBAMOS HACIENDO

### 1. Omni Oscillator (`Osciladores/budai_omni.pine`) — RECIÉN TERMINADO
Es el oscilador definitivo. Estado actual:
- **Selector de motor**: WaveTrend · Slope · MoneyFlow · Squeeze · RSI (dropdown).
- **COG (Ehlers)** opcional mezclado 75/25 para reducir lag.
- **Hyper Wave** (2ª onda de presión) con **Kernel 1 (0.8) / Kernel 2 (0.3)**.
- **Money Flow** de fondo (CMF) en columnas.
- **Nodos blancos con glow** en cada cruce osc×trigger (en location.absolute con el valor).
- **Señales** doble-glow (amarillo/rosa neón) en cruce + zona extrema + flujo a favor.
- **12 colores configurables** + grosor de línea + degradado dual opcional
  (celeste→naranja alcista / fucsia→morado bajista vía color.from_gradient).
- Estética Athenea: onda + glow fading + línea blanca brillante + fibo morados + dashboard tiny.
- 251 líneas, compila OK (ignorar hints/falsos positivos del linter del IDE).

PENDIENTE de feedback: el usuario iba a probar en TV los motores y los degradados duales.
Si reporta algo visual, corregir manteniendo estética Athenea.

### 2. Decisiones estéticas confirmadas en esta sesión
- Volvimos DEFINITIVAMENTE a estética **Athenea** (dejamos el estilo Nautilus de lado
  porque las barras/ribbons daban problemas — `▰` grueso, líneas gruesas).
- **Bull = celeste `#00e5ff` / naranja `#ff9100`** · **Bear = rojo `#ff1744` / morado
  `#b388ff` / fucsia `#ff1e6e`**. Señales amarillo `#ffff00` / rosa `#ff007f`. Todo neón.
- Líneas finas (linewidth 1-2), glow capa aparte, círculos `plotchar "•"` tiny doble-glow.
- Nodos de cruce = círculo blanco con glow, FINO, que caiga exacto en el cruce.
- TODO color debe ser configurable (input.color), nada hardcodeado fijo.

---

## SUITE ACTUAL — 13 osciladores (NO rehacer)
squeeze · coil · abyss · slope · helix · pulse · panic · **athenea ⭐(estética ref)** ·
tidal · moneyflow · moneyflow_tide · **omni ⭐(definitivo, selector)**.
(SMC/tendencia/overlay en la raíz están pausados, a pulir después.)

---

## QUÉ SIGUE — MOTORES NUEVOS (objetivo del chat nuevo)
Crear osciladores con motores que aún NO tenemos, estética Athenea, uno por uno:

1. **Volume Delta / Order Flow** ⭐ PRIORIDAD — presión real compra vs venta (delta
   acumulado intrabar) en columnas grandes verde/rojo. Lo más institucional que falta.
2. **Reversal Cloud** (tipo Zeiierman) — nube que cambia de color + señales de agotamiento.
3. **Stoch RSI Pro** — RSI + estocástico fusionado, timing fino, bandas dinámicas.
4. **Momentum Wave 3D** — momentum multi-capa con efecto profundidad.
5. **TSI (True Strength Index)** — doble suavizado de momentum.
6. Opcionales: Fisher Transform, Schaff Trend Cycle, Ultimate RSI.

Referencias (consultar lógica, no copiar): LuxAlgo (Oscillator Matrix), BigBeluga
(Nautilus), LazyBear (WaveTrend/Squeeze), Zeiierman (Reversal), AlgoAlpha/QuantVue.

---

## CÓMO ARRANCAR
Empezar por **Volume Delta / Order Flow** con estética Athenea. Plan corto (qué mide,
cómo se ve), confirmar conmigo, ejecutar. Un indicador a la vez, esperar mis capturas,
corregir hasta premium. Mantener todo lo hecho intacto. No dejar rastro de autores
externos. No "(Paso/Fase)" en el código. Marca de agua `₿ BudAI Cripto` siempre.
```
