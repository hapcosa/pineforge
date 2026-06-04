# PLAN MAESTRO · BudAI Cripto — Re-creación de indicadores
### Hoja de ruta. Un pine NUEVO por cada uno. No tocamos los existentes.

---

## PARTE A · Lo que YA tenemos (suite BudAI actual)
| # | Archivo | Qué es |
|---|---|---|
| A1 | `juliondicador.pine` | Julio Nacci — Fibo+EMA+FVG+Wyckoff+Sesiones + 5 estrategias |
| A2 | `ict_ny_scalper.pine` | ICT NYC SCALPER MODE — liquidez/sweep/FVG/FATALITY |
| A3 | `ict_nyc_oscilator.pine` | ICT NYC OSCILATOR — COG+Momentum+MoneyFlow |
| A4 | `oscilador_budai_cripto.pine` | OSCILADOR BUDAI — WaveTrend+círculos+estrategia |
| A5 | `MANUAL_ICT_NYC.html` + `INFORME_INDICADORES_REFERENCIA.md` | docs |

> Estos quedan intactos. Todo lo nuevo = archivo aparte con prefijo `budai_`.

---

## PARTE B · BIBLIOTECA DE REFERENCIA (qué recrear)
Origen y mecánica de cada uno. **Recreamos lógica, no copiamos código.**

### Osciladores (panel inferior · TU FUERTE)
| Ref | Autor origen | Mecánica de señal |
|---|---|---|
| WaveTrend | LazyBear | cruce wt1×wt2 en extremos |
| Squeeze Momentum | LazyBear | BB dentro de Keltner = compresión; histograma momentum |
| Wave Trend 3D / RSI suavizado | varios | momentum normalizado |
| Nautilus | BigBeluga | círculos OB/OS, fuerte=círculo, simple=X |
| Regression Slope Osc | BigBeluga | pendiente regresión × señal cruzando 0 |
| Equilibrium Momentum Shift | BigBeluga | shift desde equilibrio + divergencia |
| Oscillator Matrix / Hyperwave | LuxAlgo | momentum + money flow + divergencia |
| Williams Vix Fix | ChrisMoody | proxy de pánico/suelo |
| Squeeze Pro / TTM | varios | compresión multi-banda |

### Estructura SMC (overlay · contexto)
| Ref | Autor | Qué marca |
|---|---|---|
| Smart Money Concepts | LuxAlgo (free) | BOS/CHoCH, OB, FVG, EQH/EQL, premium/discount |
| Price Action SMC | BigBeluga (free) | FVG imanes, doble techo/suelo, liquidez |
| Order Blocks | LonesomeTheBlue | OB con mitigación |
| Harmonic Patterns | LonesomeTheBlue | patrones armónicos |
| Liquidity / FVG / Premium-Discount | varios | zonas institucionales |

### Tendencia + señales (overlay)
| Ref | Autor | Señal |
|---|---|---|
| Signals & Overlays | LuxAlgo | confirmation/contrarian/exit + Smart Trail |
| Market Waves | BigBeluga | ▲▼ en Smart Bands |
| SuperTrend / Trend Catcher | varios | trailing de tendencia |
| Range Filter | DonovanWall | filtro de rango/tendencia |

---

## PARTE C · PLAN DE EJECUCIÓN (paso a paso · uno a uno)
Cada paso = 1 pine nuevo `budai_*`, estética BudAI, marca de agua, header.
Lo hacemos **en este orden**. No avanzamos al siguiente hasta cerrar el actual.

### FASE 1 — Osciladores (base, fácil de testear aislado)
- **Paso 1** · `budai_squeeze.pine` — Squeeze Momentum (compresión/expansión). Pre-breakout.
- **Paso 2** · `budai_nautilus.pine` — Oscilador estilo Nautilus (círculos OB/OS fuerte/simple).
- **Paso 3** · `budai_regslope.pine` — Regression Slope Oscillator (reversión por pendiente).
- **Paso 4** · `budai_vixfix.pine` — Williams Vix Fix (detector de suelos de pánico).

### FASE 2 — Estructura SMC (contexto)
- **Paso 5** · `budai_smc.pine` — Smart Money Concepts limpio (BOS/CHoCH/OB/FVG/EQH-EQL/zonas).
- **Paso 6** · `budai_orderblocks.pine` — Order Blocks con mitigación (estilo LonesomeTheBlue).
- **Paso 7** · `budai_liquidity.pine` — Liquidez + FVG + premium/discount autónomo.

### FASE 3 — Tendencia + señales (overlay)
- **Paso 8** · `budai_signals.pine` — motor Signals (confirmation/contrarian/exit) propio.
- **Paso 9** · `budai_trend.pine` — Trend Catcher / SuperTrend + Range Filter combinados.
- **Paso 10** · `budai_marketwaves.pine` — Smart Bands con ▲▼ (estilo Market Waves).

### FASE 4 — Combinación (la meta)
- **Paso 11** · `budai_confluence.pine` — Combinador/Score: oscilador + SMC + tendencia → entrada A+.
- **Paso 12** · Pulido: alertas combinadas, presets por activo, manual unificado de la suite.

---

## CONVENCIONES (para todos los nuevos)
- Header ASCII BudAI + `© BudAI Cripto`.
- Marca de agua visual configurable.
- Paleta: cian `#00e5ff` / magenta-rosa `#ff1e6e` / verde `#00e676` / morado `#9d6cff` / dorado `#ffd54f`.
- Estética LuxAlgo limpia (sin saturar), círculos/etiquetas mínimas, dashboard sobrio.
- Señales confirmadas a cierre (no repaint), `lookahead_off` en MTF.
- Cumplir reglas Pine v6 del CLAUDE.md (sin ternario-tupla, dibujo en scope global, etc).

---

## ESTADO
- [x] Paso 1 · Squeeze → `budai_squeeze.pine` ✅
- [x] Paso 2 · Nautilus → `budai_abyss.pine` (Abyss Oscillator) ✅
- [ ] Paso 3 · Regression Slope
- [ ] Paso 4 · Vix Fix
- [ ] Paso 5 · SMC
- [ ] Paso 6 · Order Blocks
- [ ] Paso 7 · Liquidity
- [ ] Paso 8 · Signals
- [ ] Paso 9 · Trend
- [ ] Paso 10 · Market Waves
- [ ] Paso 11 · Confluence
- [ ] Paso 12 · Pulido + manual

> Después de la Fase 4: combinaciones a medida y backtest.
