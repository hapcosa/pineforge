# 🔬 Informe de Análisis — Osciladores e Indicadores BudAI

> Leído .pine por .pine. **Estricto y realista**: el nivel se asigna por lo que el código *hace*, no por cuánto se habla de él. SMC excluido por ahora (a petición — solo se salva "Smart Market Structure v.2").
> Fecha: 2026-06-04.

---

## 1. Cómo se mide (criterios)

- **Nivel:** 🟢 Básico (1 primitiva), 🔵 Pro (híbrido 2-3 módulos), 🟣 Institucional (≥4 módulos con veredicto).
- **Confluencias:** cuántas familias distintas fusiona (Tendencia · Momentum · Volatilidad · Flujo · Estructura · Ciclo).
- **¿Da señal discreta?** = ¿produce LONG/SHORT claros (backtesteable)? vs. solo lectura visual.
- **¿Tan pro como Athenea?** comparación honesta de completitud.

---

## 2. Osciladores — tabla .pine por .pine

| Archivo | Tipo | Confluencias | Nivel | Señal discreta | ¿≈ Athenea? |
|---|---|---|---|:---:|:---:|
| `budai_coil` | Volatilidad+Momentum | 2 | 🔵 | sí (release) | no |
| `budai_squeeze` | Volatilidad+Momentum | 2 | 🔵 | sí (release) | no |
| `budai_slope` | Tendencia (regresión) | 1 | 🟢 | parcial | no |
| `budai_tsi` | Momentum (TSI)+div | 1-2 | 🟢 | parcial | no |
| `budai_stochrsi` | Momentum (timing) | 1-2 | 🟢 | sí (cruces) | no |
| `budai_momentum3d` | Momentum (visual) | 1 | 🟢 | no (lectura) | no |
| `budai_panic` | Reversión (Vix Fix) | 1 | 🔵 | sí (picos) | no |
| `budai_moneyflow` | Flujo (MFI+CMF+Δ) | 3 | 🔵 | parcial | no |
| `budai_helix` | Momentum doble+div | 2-3 | 🔵 | sí | ~ |
| `budai_tidal` | Momentum+Flujo+OB/OS | 3 | 🔵 | sí | ~ |
| `budai_reversalcloud` | Tendencia+Reversión (overlay) | 2 | 🔵 | sí (giro) | no |
| `budai_abyss` | Momentum+Flujo+div (Nautilus) | 3 | 🔵 | sí (OB/OS+div) | ~ |
| `budai_oceanus` | Ciclo+Presión+LSMA+div | 4 | 🟣 | sí (nodos) | **sí** |
| `budai_moneyflow_tide` | Flujo doble+ribbons | 2-3 | 🔵 | parcial | no |
| `budai_orderflow` | Order Flow (CVD/Δ) | 2 | 🔵 | sí (absorción) | nicho |
| `budai_orderflow_pure` | Footprint Δ puro | 1-2 | 🔵 | lectura | nicho |
| `budai_pulse` | WT+COG+Mom+MF+MAs+Fibo+MTF | 5+ | 🟣 | sí | **SÍ (gemelo)** |
| `budai_omni` | Selector 5 motores | 5 (selectable) | 🟣 | sí (nodos) | **sí (versátil)** |
| **`budai_athenea`** | WT+Slope+COG+Squeeze+VixFix+MF | 5-6 | 🟣 | sí | — (referencia) |
| `budai_confluence` (Matrix) | Mom+Tendencia+Estructura+Flujo → score | 4 | 🟣 | **sí (A+)** | supera* |
| `budai_hybrid` (Apex) | Mom+Volumen+Tendencia → score | 3 | 🟣 | **sí (verdict)** | supera* |
| `budai_siddharta` | 4 módulos + 2 filtros → LONG/SHORT/NO TRADE | 6 | 🟣 | **sí (verdict)** | supera* |
| `budai_aion` | Confluencia MTF 3 TF (semáforo) | meta | 🟣 | contexto | distinto |
| `budai_atlas` | Régimen TENDENCIA/RANGO/VOLÁTIL | 3 | 🟣 | contexto | distinto |
| `budai_dharma` | Flujo en sesión London/NY | 2 | 🔵 | contexto | distinto |
| `budai_eureka` | Sweep liquidez+rechazo+WT | 3 | 🟣 | **sí (trampa)** | distinto |
| `budai_nirvana` | Reversión z-score+agotamiento Δ | 3 | 🟣 | sí (reversión) | distinto |
| `budai_nexus` / `oscillator_pro×3` | Motor estructural → verdict (SMC-aware) | 5-6 | 🟣 | sí | supera* (pausado: SMC) |
| `budai_pythonissa_oscillator` | Onda+Flujo+div → verdict | 5 | 🟣 | sí | supera* |
| **Lorentzian Flow** | ML kNN + Flujo + HTF + Kernel | ML+3 | 🟣 | **sí** | distinto/superior |

\* "supera" = como **sistema de señales con veredicto**, no como oscilador de lectura.

---

## 3. Verdad incómoda (lo que pediste: no coronar a Athenea)

**Athenea es uno de los mejores OSCILADORES de LECTURA, pero NO es único ni el mejor SISTEMA:**

- **Gemelos de Athenea** (igual de "pro" en completitud): **Pulse** (prácticamente la misma fusión WT+COG+MF+MAs+Fibo, + MTF), **Omni** (selector de 5 motores), **Oceanus** (onda+presión+LSMA+div). Si Athenea desaparece, Pulse hace casi lo mismo.
- **Superiores como SISTEMA de decisión** (dan LONG/SHORT/NO TRADE con confluencia y filtro de calidad): **Siddharta**, **Apex (hybrid)**, **Confluence Matrix**, **Lorentzian**, y la familia Pythonissa/OscPro. Athenea da cruces; estos dan veredictos filtrados.
- **Conclusión honesta:** Athenea = excelente gatillo cíclico. Para "rendimiento", el cerebro debe ser un motor de confluencia (Siddharta/Apex/Lorentzian) y Athenea ser **una de las entradas**, no el sistema entero.

---

## 4. Los elegidos para BACKTESTING (carpeta `BACKTESTING/`)

Copiados los que **dan señal discreta** (lo único backtesteable de verdad):
`Athenea v2 Pro` · `Siddharta` · `Apex (hybrid)` · `Confluence Matrix` · `Pulse` · `Omni` · `Lorentzian Flow`.
> Los puros de lectura (TSI, StochRSI, Momentum3D, Slope) NO se backtestean solos — son confirmadores, no sistemas.

---

## 5. Combinaciones (carpeta `Estrategias/`) — basadas en lógica de los grandes

**Principio (LuxAlgo / Kivanç / LazyBear / ICT):** un sistema = **Filtro de tendencia + Gatillo + Confirmación (volumen/flujo) + Riesgo**. NUNCA apilar 3 osciladores de la misma familia (eso es ruido, no confluencia).

| # | Combinación | Piezas (rol) | Lógica del grande que imita | Viabilidad |
|---|---|---|---|:---:|
| **C1** | **Núcleo Tendencia-Gatillo-Flujo** | Aether (régimen) + Athenea ProMax (gatillo) + Ancla (VWAP/vol) | Triple pantalla (Elder) / confluencia LuxAlgo | 🟢 ALTA |
| **C2** | **Ruptura de volatilidad** | Kairos (squeeze) + Aether (solo a favor) + volumen | Squeeze de LazyBear + filtro tendencia | 🟢 ALTA |
| **C3** | **ML + contexto** | Lorentzian (sesgo) + Aether (régimen) + Ancla (vol) | Clasificación Lorentzian (Dehorty) con filtro | 🟢 ALTA |
| **C4** | **Reversión a la media** | Oráculo (divergencia) + Nirvana (z-score) + Ancla (VAH/VAL) | Mean-reversion en extremos | 🟡 MEDIA (contra-tendencia) |
| **C5** | **Meta-confluencia** | Cónclave leyendo conectores de todos | Sistema de votos / scoring | 🟢 ALTA (ya casi hecho) |

**Combinaciones que NO recomiendo (lo digo claro):**
- Athenea + Pulse + Omni → los tres son momentum cíclico = **redundancia**, no confluencia. Más señales ≠ mejor.
- Apilar Siddharta + Apex + Confluence Matrix → tres "cerebros" votando lo mismo = falsa seguridad.

---

## 6. Cómo empezamos (orden propuesto)

1. **Backtesteables listos** en `BACKTESTING/` ✅.
2. Construir **C1** primero (el núcleo, mayor viabilidad) → 1 indicador de confluencia visual + 1 `strategy()` con entradas/salidas/TP-SL para backtest real.
3. Luego **C2** y **C3**. Cada uno: indicador + estrategia en `Estrategias/`.
4. C4 solo con filtro estricto (reversión = peligrosa). C5 = extender el Cónclave.
5. **Athenea sigue mejorando** aparte (ver ROADMAP dentro de `BudAI_Athenea_v3_ProMax.pine`).

> ⚠️ Honestidad de fondo: el backtest dirá la verdad que ninguna estética puede prometer. Hasta tenerlo, ningún indicador "rinde" — solo *lee* mejor. Por eso el paso de `Estrategias/` + `BACKTESTING/` es el que de verdad importa.

---

## 7. Nota de estética (recordatorio del ADN BudAI)

Sólido, hermoso, futurista. **Fondos de color para líneas blancas = efecto eléctrico/neón.** Líneas hiperdelgadas, círculos diminutos, señales simples y precisas. **Dashboards con mejor paleta** (no el cuadro primitivo gris) — ya aplicado en Athenea V3 (cabecera cyan, dos tonos de columna). Pendiente: replicar ese dashboard mejorado en el resto de la suite.
