```
██████╗ ██╗   ██╗██████╗  █████╗ ██╗      ·  L O S   M E J O R E S
██╔══██╗██║   ██║██╔══██╗██╔══██╗██║         C R I P T O · T R A D I N G
██████╔╝██║   ██║██║  ██║███████║██║              C A P I T A L ®
██╔══██╗██║   ██║██║  ██║██╔══██║██║
██████╔╝╚██████╔╝██████╔╝██║  ██║██║      selección curada · estética neón
╚═════╝  ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝      ₿ BudAI Capital®
```

# ⭐ Vitrina — Los Mejores Indicadores BudAI

> Selección curada de la suite. **Copias** de los mejores; los originales siguen intactos en `01_BudAI/`.
> Estética OBRERO: líneas tiny, glow en capas, gradientes, paleta neón, sello `₿ BudAI`, sin relleno macizo.
> ⚠️ Editar siempre el **canónico** en `01_BudAI/`; estas son la vitrina de presentación.

---

## 💎 PREMIUM — los que se venden

| # | Indicador | Familia | Nivel | Qué contiene | Redundancia |
|---|---|---|---|---|---|
| 1 | **SMS v2** `BudAI_SmartMarketStructure_v2` | Estructura/SMC · overlay | 🟣 Institucional | OB **volumétricos** (fondo + franja buy/sell + métrica vol %), FVG/IFVG recortados con línea 50%, BOS/CHoCH, raids `$` + nodo glow, SMA/EMA ocultables. Código propio. | Reemplaza a `budai_smc` y `budai_structure` (mismo fin) |
| 2 | **Athenea** `budai_athenea_oscillator` | Ciclo/Híbrido · panel | 🔵→🟣 Pro+ | WaveTrend + Slope + COG + Squeeze BB/KC + Vix Fix + Money Flow + niveles Fibonacci. El **sello estético** de la marca. | Base compartida con Abyss/Oceanus/Pulse (variantes de onda) |
| 3 | **Siddharta** `budai_siddharta` | Meta-confluencia · panel | 🟣 Institucional | 4 módulos (WT+MF+Tendencia+COG) + 2 filtros (Volatilidad+ER) → **LONG/SHORT/NO TRADE**. | **Núcleo** de Nexus + OscPro×3 + Pythonissa Osc (6 gemelos) |
| 4 | **Pythonissa Signals** `budai_pythonissa_signals` | Sistema · overlay | 🟣 Institucional | Trail multinube, premium/discount, Kumo, MTF, zonas reversión, TP/SL auto, dashboard. Lee la onda del oscilador. | Pareja del oscilador (pack) |
| 5 | **Pythonissa Oscillator** `budai_pythonissa_oscillator` | Sistema · panel | 🟣 Institucional | Onda híbrida (WT+Slope+COG) + flujo (MFI+CMF+Delta) + LSMA + compresión + divergencias. | Comparte motor con Siddharta |

> **Pack premium recomendado:** Pythonissa Signals + Oscillator = **1 producto cerrado** (tipo Neptune). SMS v2, Athenea y Siddharta = piezas premium individuales.

---

## 🆓 FREE — funnel (atraen, muestran marca, enganchan a la suite)

| Indicador | Familia | Nivel | Qué contiene | Redundancia |
|---|---|---|---|---|
| **Aether** `BudAI_Aether_Regime` | Régimen · overlay | 🔵 Pro | AlphaTrend + clasificador TENDENCIA/RANGO (ER/ADX) | Solapa con `atlas` (régimen) |
| **Kairos** `BudAI_Kairos_Volatility` | Volatilidad · overlay | 🔵 Pro | Squeeze BB/KC + Donchian + nodo ruptura tras compresión | Solapa con `budai_squeeze`, `coil` |
| **Ancla** `BudAI_Ancla_VWAP` | Liquidez · overlay | 🔵 Pro | VWAP anclado + Volume Profile (POC/VAH/VAL) | Única en su tipo ✅ |
| **Oráculo** `BudAI_Oraculo_Divergence` | Divergencias · panel | 🔵 Pro | RSI/MFI/MACD, divergencias regulares + ocultas | Única en su tipo ✅ |
| **Cónclave** `BudAI_Conclave_Confluence` | Meta · overlay | 🟣 Institucional | Lee conectores de la suite → vota LONG/SHORT/NO TRADE | Concepto similar a Siddharta (uno panel-único, otro multi-script) |
| **Maya CRT** `BudAI_Maya_CRT` | Estructura · overlay | 🔵 Pro | Candle Range Theory (acumulación/manipulación/distribución) | Única ✅ |
| **Maya Oscillator** `BudAI_Maya_Oscillator` | Ciclo · panel | 🟢 Básico | Posición en rango 0-100, onda gradiente | Pareja de Maya CRT |
| **Volumetric OB** `budai_orderblocks` | SMC · overlay | 🟣 Institucional | OB atados a BOS/CHoCH, mitigación, breakers, overlap | Su lógica vive también dentro de SMS v2 |

---

## 🎨 Estética obligatoria (OBRERO) — la que entendimos

- **Líneas:** `tiny`, `linewidth=1` + halo (linewidth 2-3, transp ~80) + núcleo. Efecto **glow** en capas.
- **Señales:** `plotchar(..., "•"/"●", ...)` — **NUNCA** `plotshape(shape.circle)` (hace globos gigantes).
- **Nubes/zonas:** **gradiente** que se desvanece a 100% transp — JAMÁS relleno macizo.
- **Paleta:** neón seleccionable; default verde `#00e676` / rojo `#ff1744`.
- **Sello:** marca de agua `₿ BudAI` (`bottom_right`, `color.new(#b6f400,30)`, `size.tiny`).
- Sin `bgcolor`; cajas OB/FVG con borde fino 1px OK.

---

## 🔁 Mapa de redundancias (para tener claro, sin borrar)

```
SMC overlay      → SMS v2 ⭐  ⟵ budai_smc, budai_structure        (3 ≈ iguales)
OB volumétrico   → SMS v2 / budai_orderblocks                      (2)
Confluencia →     Siddharta ⭐ ⟵ Nexus, OscPro·Híbrido/Fusión/WT, Pythonissa Osc, Cónclave (6-7 gemelos)
Régimen          → Aether ⭐ / Atlas                                (2)
Squeeze/Compres. → Kairos ⭐ / budai_squeeze / coil                 (3)
Onda híbrida     → Athenea ⭐ ⟵ Abyss, Oceanus, Pulse              (variantes)
```
⭐ = la versión elegida como referente. Las demás se conservan como variantes/experimentos.

---

> Catálogo completo y comparativa vs otros creadores: `01_BudAI/00_CATALOGO_MAESTRO_BUDAI.md`
> Honestidad: estética y cobertura a nivel BigBeluga/LuxAlgo; pendiente real = ML/Lorentzian + validación con backtest.
