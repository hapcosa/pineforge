# BudAI Capital® — Informe de Clasificación de Osciladores

> Auditoría técnica y organización por niveles de madurez. Objetivo: dividir el trabajo de forma realista — qué está terminado, qué es base reutilizable y qué es referencia externa.

## Criterio de clasificación

Tres niveles **realistas** según arquitectura, no según estética:

| Nivel | Define | Veredicto | Estado de trabajo |
|---|---|---|---|
| **1 · Base** | Un solo concepto/módulo | Lectura direccional simple | Bloques reutilizables, listos |
| **2 · Avanzados** | Multi-módulo, confluencia parcial o MTF | Señales filtradas (débil/fuerte) | Funcionales, mejorables |
| **3 · Institucionales** | Veredicto único + régimen + perfiles | LONG / SHORT / NO TRADE | Suite final, en pulido |
| **Ref.** | Código externo / legado | Variable | No es obra BudAI; estudio |

---

## 📁 Nivel 1 — Base (módulo único) · 11

Cada uno mide **una** cosa bien. Son las piezas con las que se arman los superiores.

| Archivo | Qué mide | Reutilizable como módulo de |
|---|---|---|
| budai_slope | Pendiente de regresión (tendencia) | Tendencia |
| budai_tsi | True Strength Index (momentum doble suavizado) | Momentum |
| budai_squeeze | Compresión BB/KC + momentum | Volatilidad |
| budai_coil | Compresión de rango | Volatilidad |
| budai_panic | Pánico/euforia (Vix Fix) | Sentimiento |
| budai_moneyflow | Smart Money Flow (CMF) | Volumen |
| budai_tidal | Flujo cíclico | Volumen/ciclo |
| budai_stochrsi | StochRSI + bandas dinámicas | Momentum/timing |
| budai_momentum3d | Momentum normalizado + aceleración (3 capas) | Momentum |
| budai_reversalcloud | Trailing ATR (overlay) | Tendencia/reversión |
| budai_helix | Onda cíclica | Ciclo |

**Veredicto:** sólidos como ladrillos. No buscan dar señal final; alimentan a los Nivel 3.

## 📁 Nivel 2 — Avanzados (multi-módulo) · 9

Combinan 2+ módulos, dan señales débil/fuerte, algunos con MTF o divergencias. Aún disparan por cruce + filtro, no por veredicto único.

| Archivo | Núcleo | Observación crítica |
|---|---|---|
| budai_hybrid (Apex) | Momentum+Volumen+Tendencia + score 0–3 | **El mejor del nivel**; base conceptual de Siddharta |
| budai_athenea | WaveTrend+Slope+COG+Squeeze+VixFix | Referencia estética; muy completo, algo cargado |
| budai_oceanus | WaveTrend+kernel+MFI+LSMA+div | Saturado visualmente |
| budai_abyss | WaveTrend±100+MFI+div | Núcleo redundante con oceanus |
| budai_omni | "Todo en uno" configurable | Riesgo de ensalada |
| budai_pulse | Money flow + MTF score 4 TFs | MTF simple bien resuelto |
| budai_moneyflow_tide | MFI rápido/lento + CMF | Dual-MFI correlacionado |
| budai_orderflow | CVD por LTF + absorción | Depende de datos intrabar |
| budai_orderflow_pure | Footprint de delta + CVD sesión | Idem; potente pero costoso |

**Veredicto:** funcionales. Athenea/Apex valen como referencia; el resto comparte demasiado núcleo WaveTrend (duplicación).

## 📁 Nivel 3 — Institucionales (suite Siddharta) · 6

Veredicto único, perfiles Scalper/Day/Swing, filtros de régimen y anti-ruido, estética rayo unificada. **Es la línea de producto final.**

| Archivo | Rol en el ecosistema | Pregunta que responde |
|---|---|---|
| **budai_siddharta** | Motor maestro de confluencia | ¿LONG, SHORT o NO TRADE? |
| **budai_atlas** | Detector de régimen (filtro) | ¿Tendencia, rango o volátil? |
| **budai_eureka** | Liquidity Pulse | ¿Hubo barrido y reversión? |
| **budai_aion** | Confluencia MTF (grid) | ¿Alinean las temporalidades? |
| **budai_dharma** | Session Flow | ¿Es hora de liquidez real? |
| **budai_nirvana** | Gravity Reversal | ¿Reversión por sobreextensión? |

**Veredicto:** completos y coherentes entre sí. Pendiente: conectar Atlas→Siddharta como filtro y validar parámetros por activo.

## 📁 Referencias externas · 10

No son obra BudAI: se conservan como estudio/comparación.

`luxalgooscilator` · `ict_nyc_oscilator` · `autofibolevelosci` · `cybercyclev3` (Ehlers) · `oscilador` / `oscilador_v26` / `oscilador_v31` (CryptoProofit®) · `oscilador_budai_cripto` · `ARTEMISOSCILATORPRO` · `ARTEMISSQUEZE`.

> Artemis (TS Score + MTF) y LuxAlgo (momentum adaptativo) son los más sofisticados del grupo y buenos referentes de dashboard/score.

---

## Hoja de ruta sugerida

1. **Cerrar Nivel 3:** acoplar Atlas como filtro dentro de Siddharta; tabla de parámetros por activo (cripto vs índices).
2. **Depurar Nivel 2:** elegir UNO de {oceanus, abyss, omni} y archivar los otros (núcleo duplicado).
3. **Promover de Nivel 1:** momentum3d y stochrsi son candidatos a "intermedio+" si se les añade filtro de tendencia.
4. **No tocar Referencias:** solo lectura/estudio.

*Generado por auditoría de código. No constituye consejo financiero ni promesa de rentabilidad.*
