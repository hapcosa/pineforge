# 📒 Catálogo Maestro — BudAI Capital®

> Inventario real, leído archivo por archivo. Sin adornos, sin promesas de winrate.
> Última reorganización: 2026-06-03. Marca: **BudAI Capital®** (revertida desde PythonissAI).

---

## 🗂️ Estructura de carpetas

```
01_BudAI/                         ← NUESTROS indicadores
  00_Suite_Nucleo/                ← lo último (8 piezas, marca BudAI, código limpio)
  SMC/                            ← nuestros SMC y estructura (7)
  Osciladores/
    Nivel_1_Base/                 ← estándar / ladrillos (11)
    Nivel_2_Avanzados/            ← híbridos / pro (10)
    Nivel_3_Institucionales/      ← motores de confluencia (12)
      BudAI_Oscillator_Pro/       ← variantes de onda del motor estructural
      SIGNALS/                    ← pack Pythonissa (overlay + oscilador)
  _Experimentos/                  ← borradores (2)
02_Referencias/                   ← NO son nuestros (estudio)
  Osciladores/                    ← CryptoProofit, LuxAlgo, Artemis, Ehlers, ICT…
  SMC_Sistemas/                   ← BigBeluga, Julio Nacci, SMC Elite, ICT, Gaussian…
03_Documentacion/                 ← manuales, prompts, informes
```

**Regla:** lo de `02_Referencias` es material ajeno para aprender. NUNCA copiar literal ni publicar como propio. Lo de `01_BudAI` es nuestro.

---

## 🎚️ Escala de calidad (realista)

| Nivel | Significado honesto |
|---|---|
| 🟢 **Básico** | Indicador estándar bien hecho (RSI, TSI, StochRSI…). Valor: limpieza y estética, no originalidad. |
| 🔵 **Pro** | Híbrido con lógica propia combinando 2-4 primitivas. Original en presentación, sólido. |
| 🟣 **Institucional** | Motor de confluencia multi-módulo con veredicto. Ambicioso y vistoso — **pero sin validación estadística** (no hay backtest serio detrás). "Institucional" = complejidad, NO rentabilidad probada. |

> ⚠️ **Honestidad brutal:** ninguno de estos está validado con backtest robusto. Son herramientas de *lectura* y *confluencia*, no garantías. El edge real lo pone el operador, la gestión de riesgo y el contexto — no el indicador.

---

## 🧱 01 · SUITE NÚCLEO (lo último — la cara de BudAI)

| Archivo | Familia | Qué hace | Nivel |
|---|---|---|---|
| `BudAI_SmartMarketStructure_v2` | Estructura/SMC | **Buque insignia.** OB volumétricos (fondo + franja buy/sell + métrica %), FVG/IFVG recortados, BOS/CHoCH, raids `$` + nodo glow. Código propio. | 🟣 |
| `BudAI_Aether_Regime` | Régimen | AlphaTrend + clasificador TENDENCIA/RANGO (ER/ADX). Filtro de contexto. | 🔵 |
| `BudAI_Kairos_Volatility` | Volatilidad | Squeeze BB/KC + Donchian, nodo de ruptura solo tras compresión. | 🔵 |
| `BudAI_Oraculo_Divergence` | Divergencias | RSI/MFI/MACD, divergencias regulares + ocultas, onda gradiente. | 🔵 |
| `BudAI_Ancla_VWAP` | Liquidez | VWAP anclado + Volume Profile (POC/VAH/VAL). | 🔵 |
| `BudAI_Conclave_Confluence` | Meta | Lee los conectores de la suite y vota LONG/SHORT/NO TRADE. | 🟣 |
| `BudAI_Maya_CRT` | Estructura | Candle Range Theory (acumulación/manipulación/distribución). | 🔵 |
| `BudAI_Maya_Oscillator` | Ciclo | Posición en rango 0-100, onda gradiente, nodos. | 🟢 |

**Estos están conectados** (conn_* vía `input.source`) → el Cónclave los une. Es la suite vendible/presentable.

---

## 🏛️ 02 · SMC (carpeta `SMC/`)

| Archivo | Qué hace | Nivel | Nota honesta |
|---|---|---|---|
| `budai_orderblocks` | OB volumétricos atados a BOS/CHoCH, mitigación, breakers, overlap | 🟣 | Sólido |
| `budai_smc` | SMC máquina de estados: BOS/CHoCH·OB·FVG·Sweeps | 🟣 | **Solapa** con structure y SMS v2 |
| `budai_structure` | SMC + EQH/EQL + premium/descuento | 🟣 | **Solapa** con budai_smc |
| `budai_liquidity` | Zonas de liquidez | 🔵 | Revisar header (sin descripción) |
| `budai_trend` | **SuperTrend ATR + Range Filter + EMA cloud** | 🔵 | ⚠️ Esto NO es SMC, es Tendencia. Cubre el "hueco Supertrend+EMA". |
| `budai_signals` | Motor señales: confirmación+contrarian+exit+trail | 🔵 | Genérico |
| `budai_marketwaves` | Smart Bands adaptativas + señales rechazo | 🔵 | Genérico |

🔴 **Redundancia crítica:** `budai_smc` + `budai_structure` + `SMS v2` = **tres SMC** que hacen casi lo mismo. Recomendación: **SMS v2 es el oficial**; archivar o fusionar los otros dos.

---

## 〰️ 03 · OSCILADORES

### 🟢 Nivel 1 — Base (ladrillos estándar, 11)
`tsi` (True Strength) · `stochrsi` (Stoch RSI) · `squeeze` (Squeeze Momentum) · `momentum3d` · `moneyflow` (Smart Money Flow) · `slope` (regresión) · `tidal` · `helix` (wave) · `panic` (Vix/euforia) · `coil` (compresión) · `reversalcloud` (overlay).
→ Bien hechos pero **son primitivas conocidas**. Su valor es estética + base para combinar.

### 🔵 Nivel 2 — Avanzados (híbridos, 10)
`athenea` (WT+Slope+COG+Squeeze+VixFix — **el mejor del nivel**) · `hybrid` (Apex Confluence) · `confluence` (Confluence Matrix) · `pulse` (Pulse Flow) · `abyss` (wave) · `oceanus` (wave) · `omni` · `orderflow` (Delta) · `orderflow_pure` · `moneyflow_tide`.
→ Lógica propia real. Athenea es el referente estético de toda la marca.

### 🟣 Nivel 3 — Institucionales (motores de confluencia, 12)
| Archivo | Qué hace de verdad |
|---|---|
| `siddharta` | **Oscilador maestro:** 4 módulos (WT+MF+Tendencia+COG) + 2 filtros (Volatilidad+ER) → LONG/SHORT/NO TRADE |
| `atlas` | Detector de régimen TENDENCIA/RANGO/VOLÁTIL (ER+ADX+BBW). Filtro de contexto |
| `aion` | Confluencia MTF en 3 temporalidades → tabla semáforo |
| `eureka` | Caza-trampas: barridos de liquidez + rechazo + WaveTrend |
| `nirvana` | Reversión por z-score + agotamiento de delta |
| `dharma` | Flujo institucional solo en sesiones London/NY |
| `nexus` | Como Siddharta pero **lee tu SMC** (BOS/CHoCH) vía input.source |
| `oscillator_pro_hibrido/fusion/wtstoch` | Mismo motor estructural, **3 variantes de onda** |
| `pythonissa_oscillator` | Cerebro del pack Pythonissa (onda+flujo+divergencias) |
| `pythonissa_signals` | Overlay del pack: trail multinube, premium/discount, TP/SL, dashboard |

🔴 **Redundancia crítica:** `siddharta` + `nexus` + `oscillator_pro_*` (×3) + `pythonissa_oscillator` = **6 versiones del mismo motor de confluencia** (estructura+flujo+régimen → LONG/SHORT/NO TRADE). Difieren en la onda y en si leen SMC externo. **Elegir UNO como insignia.**

---

## 🏆 Los mejores (mi selección honesta)

1. **SMS v2** — el SMC propio, lo más pulido y útil.
2. **Athenea Oscillator** — el mejor oscilador híbrido, sello estético de la marca.
3. **Siddharta** — el mejor "todo-en-uno" de panel (si eliges un solo motor de confluencia).
4. **budai_orderblocks** — OB volumétricos serios.
5. **Aether + Kairos + Ancla** — el trío de contexto (régimen/volatilidad/liquidez) limpio.

---

## 🔗 Combinaciones recomendadas (cómo se usan juntos)

| Setup | Piezas | Para qué |
|---|---|---|
| **Núcleo Swing** | Aether (régimen) → SMS v2 (estructura/OB) → Ancla (VWAP) → Cónclave (veredicto) | Swing/posición con confluencia |
| **Scalp liquidez** | Dharma (sesión) → Eureka (sweep) → SMS v2 (OB) | Entradas en trampa, intradía |
| **Reversión** | Nirvana (z-score) + Oráculo (divergencia) + Ancla (VAH/VAL) | Giros por sobreextensión |
| **Tendencia pura** | budai_trend (SuperTrend+EMA) + Athenea + volumen | Day trading direccional |
| **Pack Pythonissa** | pythonissa_signals (overlay) + pythonissa_oscillator (panel) | Sistema cerrado tipo Neptune |

---

## 📊 Cuadro comparativo vs otros creadores

| Capacidad | BudAI | BigBeluga | LuxAlgo | LazyBear | AlgoAlpha/Mishy | Kivanç |
|---|---|---|---|---|---|---|
| SMC / Order Blocks volumétricos | ✅ SMS v2 | ✅ (referente) | ✅ | — | — | — |
| Oscilador híbrido (WT/COG) | ✅ Athenea | ~ | ✅ | ✅ WaveTrend | ✅ | — |
| Squeeze / Volatilidad | ✅ Kairos | ✅ | ✅ | ✅ (autor) | ✅ | — |
| Confluencia → veredicto | ✅ Siddharta/Cónclave | — | ✅ (referente) | — | ✅ | — |
| SuperTrend / Tendencia | ✅ budai_trend/Aether | ✅ | ✅ | — | ✅ (autor) | ✅ AlphaTrend |
| Régimen / contexto | ✅ Atlas/Aether | ~ | ✅ | — | — | — |
| **ML / Lorentzian** | ❌ **HUECO** | — | ~ | — | ✅ (referente) | — |
| Validación estadística (backtest) | ❌ | ❌ | ~ | — | ~ | — |

**Lectura honesta:** en cobertura y estética estás **a la altura** de BigBeluga/LuxAlgo. Tus dos debilidades reales son: (1) **no tienes nada de ML/Lorentzian** (lo único moderno que te falta), y (2) **ninguna pieza está validada con backtest** — igual que la mayoría del mercado retail, pero conviene no olvidarlo.

---

## ✅ Acciones pendientes sugeridas (orden)

1. **Resolver redundancia SMC:** declarar SMS v2 oficial; archivar `budai_smc` y `budai_structure` (o fusionar sus extras —EQH/EQL, premium/discount— en SMS v2).
2. **Resolver redundancia confluencia:** elegir UNO entre Siddharta/Nexus/OscPro×3/Pythonissa como insignia; el resto a `_Experimentos` o archivo.
3. **Definir set FREE (5-7) vs PREMIUM (1-2).**
4. **Construir el hueco:** motor ML/Lorentzian + Money Flow (único diferenciador que falta).
5. `budai_trend` está mal ubicado en `SMC/` → debería ir a una futura carpeta `Tendencia/`.
```
```
> Generado leyendo cada cabecera. Para un audit línea-por-línea de cualquier pieza puntual, pídelo y entro a fondo.
