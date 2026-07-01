# 🔬 KRIPTOLAB INDICADORES — señaladores para backtest

> **Qué es:** indicadores `.pine` que **emiten señal discreta LONG/SHORT** (no
> `strategy()`), aparcados aquí para **portarse a `KryptoLab/strategies/*.py`**,
> medirse y **optimizar los mejores parámetros**. Misión: crear indicadores, no
> estrategias. Honestidad: ninguno "rinde" hasta que el backtest OOS lo diga.

Flujo (ver `KryptoLab/CLAUDE.md` §0 y §6):
```
.pine (aquí) ─port→ strategies/*.py + tests/test_*_parity.py
   → optimize (in-sample) → output/params_*.json (top10)
   → backtest/validate (OOS) → copiar params ganadores a los input.* del .pine
```
Sin **test de paridad** (tol 1e-9) los params NO transfieren → la mejora sería falsa.

---

## 📦 Contenido (los 2 huecos reales del informe)

| Archivo | Hueco | Qué contiene (módulos) | Señal | Alert |
|---|---|---|---|---|
| `BudAI_Helios_TrendVolume.pine` | (a) Motor de tendencia limpio **con volumen** | ① SuperTrend(ATR) · ② EMA Ribbon(5) + macro EMA200 · ③ RVOL · ④ Régimen ADX/DI | flip ST alineado con ribbon+vol+ADX | ✅ JSON canónico |
| `BudAI_Lorentzian_Flow.pine` | (b) ML / Money Flow | ① kNN Lorentzian(5 feat) · ② filtros vol/régimen/ADX · ②b kernel Nadaraya-Watson · ③ flujo MFI+CMF+Δ · ④ S/R adaptativo | flip del sesgo kNN confirmado | ✅ JSON canónico (añadido) |

Ambos: señal en `barstate.isconfirmed` (sin repaint), símbolo limpio
`basecurrency+USDT`, plan RM (SL/TP1-3/trailing/BE) en el JSON. Conector
`conn_*` (display.none) para el Cónclave.

---

## 🎛️ Espacio de parámetros para optimizar (→ `ParamDef`)

Defaults **NO optimizados**. Estos rangos = espacio de búsqueda sugerido
(mapean 1:1 a `min_val/max_val/step` del `ParamDef` Python). El optimizador
(`cli.py optimize --method bayesian`) busca dentro de aquí.

### Helios
| Param | default | min | max | step | tipo |
|---|--:|--:|--:|--:|---|
| `stLen` (ATR) | 10 | 5 | 30 | 1 | int |
| `stMult` | 3.0 | 1.5 | 6.0 | 0.1 | float |
| `r1..r5` (ribbon) | 8/13/21/34/55 | — | — | — | int (apilados) |
| `macroLen` | 200 | 100 | 300 | 10 | int |
| `volThr` (RVOL) | 1.2 | 1.0 | 3.0 | 0.1 | float |
| `adxThr` | 20 | 12 | 35 | 1 | float |
| `reqStack` | false | — | — | — | bool |

### Lorentzian
| Param | default | min | max | step | tipo |
|---|--:|--:|--:|--:|---|
| `kNeighbors` | 8 | 3 | 24 | 1 | int |
| `maxBack` | 1000 | 500 | 2000 | 100 | int (coste ↑) |
| `rsiLenA/B` | 14/9 | 5 | 30 | 1 | int |
| `cciLen` | 20 | 10 | 40 | 2 | int |
| `kH` (kernel) | 8 | 4 | 20 | 1 | int |
| `kR` | 8.0 | 2.0 | 16.0 | 0.5 | float |
| filtros (`useVol/useReg/useKernel/reqFlow`) | on | — | — | — | bool |

> **Riesgo (común, paridad de salidas):** `sl_pct` 0.5–3.0 · `tp1/2/3` escalado ·
> `trail_act/cb` · `be_trig/off`. Deben reflejar el RM con que backtestea KryptoLab.

---

## ▶️ Estado del port

> Los ports viven en el repo hermano **`KryptoLab/`** (rutas relativas a su raíz).
> Esta carpeta solo guarda los `.pine` fuente + este índice.

| Indicador → estrategia | Strategy | Parity test | CLI alias | Estado |
|---|---|---|---|---|
| Helios | `strategies/helios.py` | `tests/test_helios_parity.py` (3/3 ✅) | `helios` | **PORTADO + medible** |
| Lorentzian | `strategies/lorentzian.py` | `tests/test_lorentzian_parity.py` (3/3 ✅) | `lorentzian` (`lflow`,`knn`) | **PORTADO + medible** |
| Oceanus · cruce fuerte | `strategies/oceanus_strongcross.py` | `tests/test_oceanus_strongcross_parity.py` (2/2 ✅) | `oceanus_strongcross` (`ostrong`) | **PORTADO + medible** |
| Oceanus · divergencia | `strategies/oceanus_divergence.py` | `tests/test_oceanus_divergence_parity.py` (2/2 ✅) | `oceanus_divergence` (`odiv`) | **PORTADO + medible** |

> **Oceanus** (`pineforge/01_BudAI/Osciladores/Nivel_2_Avanzados/budai_oceanus.pine`)
> se partió por tipo de señal: **divergencia** (alcista+bajista por pivotes sobre el
> oscilador) y **cruce fuerte** (cruce osc/trig en zona OS/OB con flujo MFI a favor).
> La **salida OB/OS (bounce)** queda fuera por ahora (contra-tendencia, sin filtro de
> flujo → menor prior). La LSMA dual del Pine es solo visual → no se porta.

Primitivas añadidas a `indicators/common.py` (Pine-fieles):
- (Helios) `supertrend()`, `dmi()` — reusan `atr`/`rma`.
- (Oceanus/Lorentzian) `rsi()`, `cci()`, `mfi()` + `_rolling_sum()` — reusan `rma`/`sma`.
  Oscilador WaveTrend de Oceanus compartido en `indicators/oceanus.py`.

Sin regresión en los ports existentes (helios 3/3 verde tras los cambios en `common.py`).

### Cómo correr el test (gotcha de entorno)
`KryptoLab/.venv` es Linux → no corre en Windows, y `pytest tests/` peta al recorrer
el symlink roto `lib64`. Usar un Python Windows con numpy e **importar el test
directo** (no via pytest):
```
& "C:\Users\Lenovo\AppData\Local\Programs\Python\Python313\python.exe" -c ^
  "import tests.test_lorentzian_parity as T; T.test_lorentzian_no_filters(); print('OK')"
```

### Optimizar por perfiles (`--profile`)
`cli.py optimize` acepta `--profile {signal|risk|mm|all}`. Las 3 familias son
**disjuntas** (signal + risk + mm = todos los params):
- `signal` → **solo params del indicador** (ni risk ni money mgmt).
- `risk` → **solo risk management COMÚN** del `rm_mixin`: SL/TP/trailing/BE/leverage.
  *NO* incluye money management.
- `mm` (alias `sizing`/`dca`) → **solo money management** (`mm_*`: martingala/kelly/
  fixed_ratio/sizing). Es una "estrategia de sizing" aparte del RM común.
- `all` (default) → todos. Compone con `--optimize-params`/`--exclude-params`.

### Siguiente
1. **Optimizar la señal** in-sample → `optimize --strategy ostrong … --profile signal`.
2. **Congelar y afinar RM común** → `optimize … --profile risk --params-file output/params_*.json --trial 1`.
3. **(Opcional) afinar sizing** → `optimize … --profile mm --params-file …`.
4. `validate` OOS (WFE≥0.3, DSR≥0.5, MC p<0.05) → copiar params ganadores a los `input.*` del `.pine`.

*No es consejo financiero ni promesa de rentabilidad.*
