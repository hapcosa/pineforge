# Informe · Indicadores de referencia (LuxAlgo · BigBeluga · otros)
### Para recrear desde cero con BudAI Cripto — investigación real, may 2026

> Objetivo: saber qué indicadores existen, cuáles **generan señales** (buy/sell) y cómo se
> comportan, para recrearlos limpios y luego combinarlos. Foco en los que tienen entradas.

---

## 0 · Nota de método y legal
- LuxAlgo (~399 scripts) y BigBeluga (~177) tienen catálogos enormes; **la mayoría premium**
  (código cerrado). No se puede copiar su código — sí **re-crear la lógica** desde los conceptos
  públicos (eso es legal y es lo que haremos).
- Lo verificado abajo viene de sus páginas de TradingView / docs oficiales.

---

## 1 · LuxAlgo — los que importan

### 1.1 Signals & Overlays™ (el buque insignia · genera señales)
El más relevante para ti. Toolkit todo-en-uno. Tipos de señal:
- **Confirmation** (normal y *strong* con "+") → confirman tendencia.
- **Contrarian** → reversiones (normal/strong).
- **Exit** → marcas "x" para toma de ganancias.
- **Candle coloring** (verde/morado/rojo) según tendencia.
- Overlays: **Smart Trail, Reversal Zones, Trend Catcher, Trend Tracer**.
- AI Classifier (4 niveles continuación vs reversión), dashboard, autopilot.
**Comportamiento:** motor mezcla momentum + tendencia; las señales nacen de cruces filtrados
por un "trend engine". Recreable con WaveTrend/ROC + filtro de tendencia + zonas.

### 1.2 Oscillator Matrix™ (oscilador · señales)
- **Hyperwave** (oscilador de momentum tipo WaveTrend) + **Money Flow** + divergencias.
- Reversal signals en extremos, confluencia.
- → Es justo lo que ya empezaste con tu BUDAI oscilador. Recreable.

### 1.3 Price Action Concepts™ (estructura · semi-señales)
- Order Blocks, BOS/CHoCH, FVG, liquidez, premium/discount.
- No da buy/sell directo; da el **contexto** de la señal.

### 1.4 Open-source notables (estudiar el código real, legal)
- **Smart Money Concepts (SMC)** — el #1 gratis. BOS/CHoCH, OB, FVG, EQH/EQL, premium/discount.
- **Signal Forge** — motor modular: mezcla 11 filtros en una señal unificada + backtest. **Open**.
- Muchos osciladores sueltos (Ultimate RSI, etc.) open-source.

---

## 2 · BigBeluga — los que importan

### 2.1 Nautilus Oscillator (oscilador · señales claras)
- **Buy (OS):** triple línea verde bajo el oscilador (reversión desde sobreventa).
- **Sell (OB):** triple línea roja arriba; *Bearish Peak* marcado en máximos.
- Señales **fuertes = círculos** (en oscilador y chart), **simples = X**.
- → Mismo estilo de círculos que te gustó. Muy recreable.

### 2.2 Market Waves Pro™ (tendencia + señales)
- **Long ▲** en zona de sobreventa + Smart Bands verdes + Power Signal [+].
- **Short ▼** en rechazo de Smart Band en tendencia bajista.
- Entrada al cierre de la siguiente vela. Acumulación/estructura.

### 2.3 Regression Slope Oscillator (oscilador · reversión)
- **Bull reversal:** oscilador cruza arriba su señal estando bajo 0.
- **Bear reversal:** cruza abajo su señal estando sobre 0.
- Pendiente de regresión lineal = momentum. Recreable fácil.

### 2.4 Equilibrium Momentum Shift + Divergence (señales + divergencias)
- Cambios de momentum desde el equilibrio + divergencias automáticas.

### 2.5 Smart Money Concepts / Price Action SMC (estructura · contexto)
- FVG (imanes), doble techo/suelo, liquidez. Free el "Price Action SMC".

### 2.6 Market Core / Market Waves (todo-en-uno)
- Tendencia + acumulación + estructura.

---

## 3 · Otros autores clásicos (vale la pena conocer)

| Autor | Indicador clave | Tipo |
|---|---|---|
| **Zeiierman** | Smart Money Concepts (Expo/Premium), Trader's Indicator | SMC + señales |
| **QuantumAlgo** | Smart Money Concepts | estructura + señales |
| **ChrisMoody (CM)** | RSI/Stoch, Williams Vix Fix | osciladores clásicos open |
| **LonesomeTheBlue** | Order Blocks, Harmonic Patterns | estructura, open-source |
| **LazyBear** | WaveTrend, Squeeze Momentum, muchos osc | **osciladores open clásicos** |
| **TradingFinder / UAlgo** | SMC, FVG, liquidez | open, buena referencia |

> **LazyBear** es oro: su **WaveTrend** y **Squeeze Momentum** son la base de medio TradingView
> (incluido el motor que ya usas). Código abierto, ideal para estudiar.

---

## 4 · Clasificación por TIPO (qué recrear primero)

### A) Osciladores con señales (panel inferior) — TU FUERTE
1. WaveTrend (LazyBear) → base del LuxAlgo Oscillator y tu BUDAI ✅ ya empezado
2. Nautilus (BigBeluga) → círculos OB/OS
3. Regression Slope (BigBeluga) → reversión por pendiente
4. Squeeze Momentum (LazyBear) → compresión/expansión
5. Money Flow / Hyperwave → acum/dist

### B) Estructura SMC (overlay) — contexto
6. Smart Money Concepts (LuxAlgo free) → BOS/CHoCH/OB/FVG
7. Price Action SMC (BigBeluga free)
8. Liquidity / FVG / premium-discount

### C) Tendencia + señales (overlay)
9. Signals & Overlays (LuxAlgo) → confirmation/contrarian/exit
10. Market Waves (BigBeluga) → ▲▼ en bandas
11. Smart Trail / Trend Catcher → trailing de tendencia

---

## 5 · Cómo se comportan las señales (patrón común)
Casi todas siguen una de 3 mecánicas — útil para recrear y testear:

1. **Cruce filtrado** (oscilador × su media/señal, filtrado por tendencia o nivel).
   → Nautilus, Regression Slope, tu BUDAI.
2. **Reversión en extremo** (OB/OS + confirmación de giro).
   → Market Waves ▲▼, Nautilus círculos.
3. **Confirmación de estructura** (BOS/CHoCH + retest de OB/FVG).
   → SMC, Signals & Overlays confirmation.

**Las "strong" siempre = mecánica base + confluencia extra** (volumen, divergencia, multi-TF).

---

## 6 · Plan de re-creación sugerido (orden)
1. **Núcleo oscilador BUDAI** (ya hecho) — pulir señales tipo Nautilus (círculos OB/OS). ✅
2. **Squeeze Momentum** propio → mide compresión (genial pre-breakout).
3. **SMC estructural** propio (BOS/CHoCH/OB/FVG) — ya tienes piezas en Julio Nacci e ICT NYC.
4. **Motor de señales "Signals & Overlays"** propio: confirmation + contrarian + exit.
5. **Combinador / Confluence**: junta oscilador + estructura + tendencia en un score (como Signal Forge).

---

## 7 · Cómo combinarlos (la meta)
- **Oscilador (timing)** + **SMC (zona/contexto)** + **Tendencia (sesgo)** = entrada A+.
- Igual que ya hicimos con ICT NYC Scalper + Oscilator. Esa es la fórmula ganadora.
- Para testear: empezar con 1 mecánica por indicador, medir win-rate por separado, luego unir.

---

## Fuentes
- LuxAlgo Library — https://www.luxalgo.com/library/
- LuxAlgo perfil TV — https://www.tradingview.com/u/LuxAlgo/
- Signals & Overlays — https://www.tradingview.com/script/fYHlrAoz-LuxAlgo-Signals-Overlays/
- Signal Forge (open) — https://www.tradingview.com/script/HtOSLjaj-Signal-Forge-LuxAlgo/
- SMC (LuxAlgo) — https://www.tradingview.com/script/CnB3fSph-Smart-Money-Concepts-SMC-LuxAlgo/
- BigBeluga perfil TV — https://www.tradingview.com/u/BigBeluga/
- BigBeluga docs — https://docs.bigbeluga.com/
- Nautilus Oscillator — https://www.tradingview.com/script/1odom906-Nautilus-Oscillator-BigBeluga/
- Regression Slope Osc — https://www.tradingview.com/script/5W4FYJfC-Regression-Slope-Oscillator-BigBeluga/
- Market Waves signals — https://docs.bigbeluga.com/toolkits/market-waves-pro-tm/trend-signals
- Zeiierman SMC — https://docs.zeiierman.com/toolkit/smart-money-concepts
