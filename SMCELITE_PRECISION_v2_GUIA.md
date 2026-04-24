# SMCELITE PRECISION ENTRY v2 — Guía de Usuario

## 📋 Descripción

Indicador Pine Script v6 que detecta **Señales S (SMC Elite)** con motor de estructura real (CHoCH + Sweep) y aplica **Fisher Transform + Divergencia de Momentum** para entrada de precisión dentro de una ventana configurable.

**Novedad v2:** Motor SMC compacto con pivotes reales, divergencia robusta, alertas personalizadas.

---

## 🎯 Concepto Visual

```
┌─────────────────────────────────┐
│ CHoCH Bullish + Sweep           │  Signal S (Score ≥ 5)
│ (smcTrend=1)                    │  Trigger: WATCH activa
└─────────────────────────────────┘
         │
         ├─→ Vela 1-2: Fisher se despierta
         │   (monitorea zona extrema ±1.5)
         │
         ├─→ Vela 2-4: Divergencia Momentum
         │   (nuevo extremo SIN acompañamiento)
         │
         └─→ Vela 3-5: Fisher cruza EMA
             en dirección correcta
                    │
                    ↓
            ◇ ENTRY Confirmada
            (Label + Alerta)
```

---

## 🔧 Parámetros Principales

### 📊 Signal S Configuration
- **Lookback (bars):** 20 — ventana de frescura para CHoCH/Sweep (rango: 3-100)
- **Min Score:** 5 — puntuación mínima 0-10 (default: 5)
  - 5 = estándar (recomendado)
  - 7 = selectivas
  - 9 = muy estrictas
- **Require CHoCH:** ON — exigir Change of Character
- **Require Sweep:** OFF — exigir liquidation sweep (líberate si no necesitas confirmación extra)
- **Require OB/FVG:** ON — precio en zona de Order Block o FVG
- **Require HTF:** OFF — alineación multi-timeframe (1H/4H)
- **Require CI<max:** ON — choppiness < 50 (anti-range)

### 🐟 Fisher Transform
- **Period:** 9 — para 1H (ajustable 5-20, 13 para 4H)
- **Zone Extreme:** 1.5 — umbral zona extrema (±1.5 a ±2.0)
- **EMA Period:** 3 — suavizado de señal

### 📈 Momentum Divergence
- **Period:** 5 — close - close[5] (default para 1H, cambiar a 3 para 4H)
- **EMA Period:** 3 — suavizado del momentum
- **Min Bars Between Pivots:** 3 — separación mínima entre pivotes

### ⏱️ Precision Entry Watch
- **Window:** 5 — máximo de velas desde Signal S (5 velas = 5 horas en 1H)
- **Require Divergence:** ON — fuerza divergencia para ENTRY (recomendado ON)
- **Require OB/FVG Zone:** OFF — ENTRY debe estar en zona de estructura institucional

### 🎨 Visualization & Alerts
- **Show Signal S:** ON — mostrar etiquetas ◆ S-LONG/SHORT
- **Show ENTRY:** ON — mostrar etiquetas ◇ ENTRY ↑/↓
- **Show Fisher Panel:** ON — panel separado con Fisher
- **Show Window BG:** ON — sombrear ventana activa

---

## 📊 Visualización

### Gráfico Principal (Overlay)
| Elemento | Símbolo | Color | Significado |
|----------|---------|-------|-------------|
| Signal S Long | `◆ S-LONG ★` | Dorado | Estructura bullish + Score ≥ 5 |
| Signal S Short | `◆ S-SHORT ★` | Dorado | Estructura bearish + Score ≥ 5 |
| ENTRY Long | `◇ ENTRY ↑` | Verde brillante | Entrada de precisión confirmada |
| ENTRY Short | `◇ ENTRY ↓` | Naranja | Entrada de precisión confirmada |
| Watch Window | Fondo blanco | Blanco 90% | Ventana activa de monitoreo |

### Panel Fisher (Separado)
| Línea | Color | Estilo | Información |
|-------|-------|--------|------------|
| Fisher | Azul | Sólida | Índice Fisher normalizado |
| Signal | Rojo | Punteada | EMA3 del Fisher |
| +1.5 / -1.5 | Gris | Línea | Zonas extremas |
| Zero | Gris | Línea | Referencia central |
| BG | Verde/Rojo | Coloreado | Fisher en zona extrema |

---

## 🚀 Cómo Usar

### Setup Inicial
1. **Copiar código** de `/home/obrero/programacion/PineForge/SMCELITE_PRECISION.pine`
2. **Pine Script Editor** → Crear nuevo indicador → Pegar
3. **Agregar al gráfico** 1H o 4H (tested on these TFs)
4. **Defaults son buenos** — casi no requieren ajuste

### Interpretación

#### Signal S Aparece (◆)
- Indica confluencia de estructura + filtros (Score ≥ 5)
- **COMIENZA VENTANA DE VIGILANCIA** (5 velas máximo)
- No es aún entrada — es "sistema activado"

#### Dentro de la Ventana
- Sistema monitorea **Fisher Transform**:
  - ¿Entra en zona extrema (±1.5)?
  - ¿Cruza su EMA en dirección correcta?
- Sistema monitorea **Divergencia Momentum**:
  - ¿Nuevo extremo de precio SIN nuevo extremo de momentum?

#### ENTRY Confirmada (◇)
- Todos los criterios met:
  - ✅ Fisher en zona extrema
  - ✅ Fisher cruza EMA correctamente
  - ✅ Divergencia momentum presente
- **Dispara alerta personalizada**
- Label aparece en precio
- Ventana se cierra automáticamente

#### Ventana Expira
- Si 5+ velas pasan sin confirmación → Signal invalidada
- Regresa a IDLE, espera nuevo Signal S

---

## 🎓 Ejemplos Prácticos

### Escenario 1: Signal S Long (Entrada Exitosa)
```
Barra N:   ◆ S-LONG ★ (CHoCH bullish detectado, Score=6)
           Ventana abierta → monitorea Fisher

Barra N+1: Fisher sigue bajando (tendencia del mercado)

Barra N+2: Fisher toca -1.7 (zona extrema bullish)
           fisherWasExtreme = true

Barra N+3: Fisher cruza arriba su EMA (señal de reversión)
           Divergencia OK (último pl nuevo + momentum diverg)

           ◇ ENTRY ↑ ← ENTRADA DE PRECISIÓN CONFIRMADA
           ⚠️ Alerta: "◇ ENTRY ↑ CONFIRMED | BTC | 42500"
```

### Escenario 2: Signal S Pero Divergencia Falla
```
Barra N:   ◆ S-LONG ★

Barra N+1-4: Fisher en zona extrema, cruza EMA OK
             PERO precio hace nuevo mínimo + momentum sigue bajando
             (NO hay divergencia)

Barra N+5: Ventana vencida → INVALIDADA
           Regresa a IDLE
```

---

## ⚙️ Ajustes por Timeframe

### Para 1H (Default / Recomendado)
```
Fisher Period:        9
Momentum Period:      5
Min Score:           5-7
Watch Window:        5
Lookback:           20
```

### Para 4H (Cambios recomendados)
```
Fisher Period:        13 (más smoothing)
Momentum Period:      3 (reversal más rápido)
Min Score:           6-8 (más selectivo)
Watch Window:        3 (12 horas máximo)
Lookback:           30
Frost Mode:         "Swing"
```

### Para 15m (Scalping)
```
Fisher Period:        5
Momentum Period:      3
Min Score:           4
Watch Window:        3 (45 min máximo)
Lookback:           10
Frost Mode:         "Scalping"
```

---

## 📱 Alertas Personalizadas (New v2)

### Configurar Alertas en TradingView

1. **En el gráfico** → Click derecho en el indicador
2. **Create Alert** → Elegir:
   - `◆ Signal S LONG` — Te notifica cuando detecta estructura bullish
   - `◆ Signal S SHORT` — Estructura bearish
   - `◇ ENTRY Long` — Entrada larga confirmada
   - `◇ ENTRY Short` — Entrada corta confirmada

3. **Acciones disponibles:**
   - Email
   - Push notification (app móvil)
   - Webhook (bot Discord/Telegram)

**Recomendación:** Activar solo `◇ ENTRY Long/Short` para no ser bombardeado.

---

## 🔍 Debugging / Troubleshooting

### "No aparecen señales S"
- ✅ Verificar `Min Score` no sea muy alto (probar 5)
- ✅ Verificar timeframe es 1H o 4H
- ✅ Verificar `Require CHoCH` no esté bloqueando (probar OFF)
- ✅ Verificar `Require Choppiness` — si Chop Index > 50 bloquea todo

### "Signal S aparece pero sin ENTRY"
- Esto es NORMAL — significa:
  - ✓ Estructura OK
  - ✗ Pero Fisher/Divergencia no se alinearon
- **Solución:** Reducir `Zone Extreme` (ej: 1.2 en lugar de 1.5) para ser menos estricto

### "Demasiadas falsas señales"
- Aumentar `Min Score` a 7-8
- Activar `Require Sweep` para confluencia extra
- Ajustar Frost/WAE thresholds

### "Indicador muy lento"
- Reducir `Max Historical Signals` input (default: 50, probar 20)
- Reducir `Max Labels Count` en declaración

---

## 📊 Score Breakdown (v2)

```
Score Long = 0-10 puntos

+2: CHoCH Bullish detectado y fresco (<20 barras)
+2: Sweep Down (liquidity grab) detectado
+1: Frost Engine bullish OK
+1: WAE Explosion bullish OK
+1: MTF Trend bullish
+1: Choppiness OK (CI < 50)
+1: Volume Absorption bullish
────────────────────────────────
   Total: 0-10 puntos

Señal activa si: Score ≥ Min Score (default: 5)
```

---

## 🎯 Setup Recomendado

Para operador conservador (1H timeframe):

```
Signal S Config:
├─ Require CHoCH: ON
├─ Require Sweep: ON ← Más confirmación
├─ Require OB/FVG: ON
├─ Min Score: 7 ← Más selectivo
└─ Lookback: 20

Fisher Transform:
├─ Period: 9
├─ Zone Extreme: 1.5
└─ EMA Period: 3

Momentum Divergence:
├─ Period: 5
├─ Min Bars Between: 3
└─ Require Divergence: ON

Watch Window:
├─ Window: 5
├─ Require Divergence: ON
└─ Require OB/FVG Zone: ON
```

---

## 📞 Soporte

### Errores de Compilación
- Verificar Pine Script v6 en TradingView
- Si hay error "range", CLAUDE.md tiene solución (sección 9.1)
- Si hay error "label.style", CLAUDE.md tiene solución (sección 9.2)

### Preguntas sobre Lógica
- Ver CHANGELOG (v2_CHANGELOG.md) para cambios vs v1
- Ver CLAUDE.md para reglas de Pine Script v6

---

**Versión:** 2.0
**Pine Script:** v6
**Última actualización:** 2026-04-23
**Estado:** ✅ Listo para producción
