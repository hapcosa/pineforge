# 🐋 Informe BIGBELUGA — Auditoría .pine + Plan de Fusión Backtesteable

> Persona: **BigBeluga** (motor único, código limpio, kNN/volumétrico, estética neón).
> Leído código real: C1/C2/C3 + strategy + Lorentzian + catálogo/ranking previos.
> Fecha: 2026-06-04. Honestidad: ningún script "rinde" hasta que KryptoLab lo mida.

---

## 1. Inventario (103 .pine)

| Carpeta | N | Qué es |
|---|---|---|
| `01_BudAI/` | 53 | Propios (núcleo + osciladores N1/N2/N3 + SMC + Athenea) |
| `02_Referencias/` | 23 | Ajenos (BigBeluga, LuxAlgo, Artemis, ICT, Julio…) — estudio, NO publicar |
| `00_LOS_MEJORES_BudAI/` | 13 | Vitrina = **copias** de los mejores |
| `BACKTESTING/` | 7 | **Copias** de los que dan señal discreta |
| `Estrategias/` | 3 | C1/C2/C3 en `strategy()` (TP/SL parciales) |
| `best combinations/` | 3 | C1/C2/C3 en `indicator()` (chart) |
| `NEW INDICATOR/` | 1 | Lorentzian Flow |

**Únicos reales ≈ 53.** El resto = duplicados de presentación/backtest. Mucho de "103" es eco.

---

## 2. Clasificación (consolidada, por lo que el código HACE)

### 2.1 Por rol en un sistema (lo que importa para combinar)
| Rol | Piezas referente | Suplentes (archivar/variante) |
|---|---|---|
| **Régimen/contexto** | `Aether` (AlphaTrend+ER) | `atlas`, `aion` |
| **Tendencia overlay** | `budai_trend` (SuperTrend+EMA) | — (mal ubicado en SMC/) |
| **Gatillo cíclico** | `Athenea` (WT+Slope+COG+Squeeze+VixFix+MF) | `pulse`, `oceanus`, `abyss` (mismo núcleo WT) |
| **Volatilidad/ruptura** | `Kairos` (squeeze BB/KC + Donchian) | `budai_squeeze`, `coil` |
| **Flujo/liquidez** | `Ancla` (VWAP anclado + VolProfile) | `moneyflow`, `moneyflow_tide`, `orderflow` |
| **Divergencias** | `Oráculo` (RSI/MFI/MACD reg+ocultas) | `tsi`, `helix` |
| **Reversión** | `Nirvana` (z-score+agotamiento Δ) | `panic`, `tidal` |
| **Estructura/SMC** | `SMS v2` (OB volumétrico) | `budai_smc`, `budai_structure`, `orderblocks` |
| **ML** | `Lorentzian Flow` (kNN 5-feat) | — (único, el diferenciador) |
| **Cerebro/veredicto** | `Siddharta` / `Cónclave` | `nexus`, `oscillator_pro×3`, `pythonissa_osc` (6 gemelos) |

### 2.2 Por nivel
- 🟢 **Base (N1, 11):** tsi, stochrsi, squeeze, momentum3d, moneyflow, slope, tidal, helix, panic, coil, reversalcloud → **ingredientes, no productos**.
- 🔵 **Pro (N2, 10):** athenea, hybrid, confluence, pulse, abyss, oceanus, omni, orderflow(+pure), moneyflow_tide.
- 🟣 **Institucional (N3, 12):** siddharta, atlas, aion, eureka, nirvana, dharma, nexus, oscpro×3, pythonissa×2.

---

## 3. ¿Se pueden combinar? Veredicto

**Principio (Elder/LuxAlgo/ICT):** sistema = **Filtro tendencia + Gatillo + Confirmación flujo + Riesgo**.
NUNCA apilar 3 de la misma familia → eso es ruido, no confluencia.

### ✅ SÍ combinan (ya hechos, sólidos)
| Combo | Nombre compuesto | Contiene (rol) | Lógica grande | Viab. |
|---|---|---|---|:--:|
| **C1** | **BudAI Núcleo-Tendencial** | Aether(régimen)·Athenea(gatillo)·Ancla(VWAP+RVOL) | Triple pantalla Elder | 🟢 |
| **C2** | **BudAI Ruptura-Volátil** | Kairos(squeeze→Donchian)·Aether·Volumen | Squeeze LazyBear + filtro | 🟢 |
| **C3** | **BudAI Cognición-ML** | Lorentzian(kNN)·Aether·Ancla | Clasificación Dehorty + contexto | 🟢 |

### ❌ NO combinar (redundancia)
- Athenea + Pulse + Omni → 3× momentum cíclico = ensalada.
- Siddharta + Apex + Confluence Matrix → 3 cerebros votando lo mismo = falsa seguridad.
- Abyss/Oceanus/Pulse → mismo núcleo WaveTrend → elegir uno.

---

## 4. Hallazgos técnicos (las "mejores recomendaciones" — esto es lo nuevo)

> Esto no estaba en los informes previos. Es lo que falta para que la fusión sea backtesteable de verdad.

### 🔴 R1 — Contrato de alerta ROTO en C1/C2/C3 (bloqueante para producción)
Los 3 combos emiten:
```pine
alertcondition(longSig, "C1 · LONG", "BudAI C1 Núcleo · LONG {{ticker}} @ {{close}}")
```
Viola `pineforge/CLAUDE.md` (Estructura de Alertas OBLIGATORIA):
- `{{ticker}}` → símbolo **sucio** (`BINANCE:BTCUSDT.P`), el parser no quita el `.` → no matchea catálogo.
- No emite el **JSON canónico** (`side/symbol/timeframe/price/risk`) → no entra al webhook → no opera.
- No lleva plan RM (SL/TP/trailing/BE) → sin paridad con KryptoLab.

**Fix:** añadir `f_alertJson()` + `alert(..., alert.freq_once_per_bar_close)` con `syminfo.basecurrency+"USDT"`. Patrón canónico ya está en el CLAUDE.md.

### 🟠 R2 — Sin gemelo Python ni test de paridad (el hueco real)
C1/C2/C3 viven **solo en TV**. El contrato "doble destino" exige `KryptoLab/strategies/*.py` + `tests/test_*_parity.py` (tol 1e-9). Sin eso:
- No se puede `optimize` en KryptoLab → los params "ganadores" no existen.
- "Buenos resultados" = humo hasta que el backtest los mida.
→ **Este es el paso que de verdad falta.** Portar la ganadora a Python primero.

### 🟡 R3 — Eficiencia / DRY
- `ta.atr(14)` recalculado **4×** por barra en los `plotchar` de C1/C3 → precalcular `float atr14 = ta.atr(14)` una vez (CLAUDE 7.4).
- Aether/Athenea/Ancla/Lorentzian están **copiados** en cada combo (copy-paste). Riesgo: editas uno, los demás divergen → rompe paridad. **Extraer a librería Pine v6** (`import budai/core`) → 1 fuente, los 4 scripts la consumen.
- C3 Lorentzian: loop kNN con decimación `i%4` + ventana deslizante = O(maxBack/4) por barra. Default 800 OK; es el caro del set → no subir `maxBack` sin medir.

### 🟢 R4 — Limpieza de catálogo
Archivar a `_Experimentos/`: los 6-7 gemelos de confluencia, 2 de los 3 SMC, variantes WT. Quedarse con 1 referente por rol (tabla §2.1).

---

## 5. 🐋 EL indicador que BigBeluga construiría (la fusión)

> Un solo motor, **conmutado por régimen** (no apilar — enrutar). Se acopla a una estrategia: cada régimen activa su gatillo, el ML es el sesgo maestro, el flujo confirma, el RM cierra.

### Nombre compuesto
**`BudAI Tridente-Apex` · kNN-Regime Confluence Engine**
(alias corto chart: `BudAI ⟁ Tridente`)

### Qué contiene (módulos, rol exacto)
| # | Módulo | De dónde | Rol en el motor |
|---|---|---|---|
| 1 | **Lorentzian kNN** (5 feat: RSI14/RSI9/ADX/CCI/WT) | C3 | **Sesgo maestro** (gate direccional: solo se opera a favor del kNN) |
| 2 | **AlphaTrend + Efficiency Ratio** | Aether | **Router de régimen** → TENDENCIA vs RANGO/COMPRESIÓN |
| 3 | **Athenea WT+Slope+COG (cúspide)** | C1 | Gatillo en régimen **TENDENCIA** |
| 4 | **Kairos squeeze BB/KC → ruptura Donchian** | C2 | Gatillo en régimen **COMPRESIÓN→expansión** |
| 5 | **Ancla VWAP + RVOL** | C1/C3 | **Confirmación de flujo** (lado correcto + volumen) |
| 6 | **RM plan + alert() JSON** | nuevo | SL/TP1-3/trailing/BE → webhook + paridad KryptoLab |

### Lógica (la "estrategia" embebida)
```
sesgo = kNN.predict()                      // +1 / -1 / 0  → si 0: NO TRADE
régimen = router(AlphaTrend, ER)           // TEND | COMPRESIÓN | RANGO
gatillo = régimen==TEND ? Athenea.cúspide
        : régimen==COMPRESIÓN ? Kairos.ruptura
        : none                             // RANGO = stand down
confirm = lado_correcto(VWAP) and RVOL≥thr
LONG  = sesgo>0 and gatillo.bull and confirm and régimen!=RANGO and barstate.isconfirmed
SHORT = sesgo<0 and gatillo.bear and confirm and régimen!=RANGO and barstate.isconfirmed
→ alert(f_alertJson(side))  // JSON canónico + RM
```
**Por qué rinde mejor que C1/C2/C3 sueltos:** no fuerza un solo gatillo en todo mercado. Tendencia → sigue la onda; compresión → caza el estallido; rango → no opera (el 90% del drawdown retail nace de operar el rango). El kNN poda señales contra-sesgo.

### Dashboard (un solo veredicto)
`Sesgo kNN · Régimen · Gatillo activo · VWAP · RVOL · VEREDICTO (LONG/SHORT/NO TRADE)` — paleta neón, halo+núcleo blanco, sello ₿.

---

## 6. Plan (orden, para "buenos resultados" reales)

1. **Arreglar R1** en C1/C2/C3 (alert JSON canónico) — sin esto no operan en vivo.
2. **Construir `BudAI Tridente-Apex`** (§5) = indicador (chart) + `strategy()` (backtest).
3. **Portar a KryptoLab** (`strategies/tridente_apex.py`) + `test_tridente_parity.py` → R2.
4. **Optimize in-sample → validate OOS** en KryptoLab (BTCUSDT 1h/4h, 1-2 años, MISMO TP/SL).
5. Copiar params ganadores a los `input.*` del `.pine` → indicador mejorado en TV.
6. Extraer librería Pine compartida (R3) para que no haya drift.
7. Archivar redundancia (R4).

> Sin paso 3-4, "rinde" es estética. El edge se prueba en KryptoLab, no en el chart.
```
```
*Auditoría de diseño. No es consejo financiero ni promesa de rentabilidad.*
