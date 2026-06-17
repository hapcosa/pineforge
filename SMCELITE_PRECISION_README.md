# SMC Elite Precision Entry v1 — Fisher + Divergence

## 📋 Descripción General

Indicador independiente que **detecta señales S del SMCELITE** y aplica **Fisher Transform + Divergencia de Momentum** para dar entradas de precisión dentro de una ventana configurable.

## 🎯 Concepto

```
Signal S (confluencia base)
    ↓
WATCH (monitorear 5 velas)
    ↓
Fisher en zona extrema (±1.5) + Divergencia momentum
    ↓
◇ ENTRY confirmada (Verde ↑ / Rojo ↓)
```

## 🔧 Parámetros Principales

### 📊 Signal S
- **Lookback**: cuántas barras atrás buscar CHoCH/BOS (default: 20)
- **Min Score**: puntuación mínima para activar vigilancia (default: 5/10)
- **Require CHoCH/Sweep/OB/FVG**: filtros individuales activables
- **Require HTF / CI<max**: filtros de tendencia MTF y choppiness

### 🐟 Fisher Transform
- **Period**: 9 para 1H, 13 para 4H (ajustable 5-20)
- **Zone Extreme**: umbrales de zona extrema (±1.5, ±2.0 recomendado)
- **EMA Period**: suavizado de señal (default: 3)

### 📈 Momentum Divergence
- **Period**: cierre - cierre[5] en 1H, [3] en 4H
- **EMA Period**: suavizado momentum (default: 3)
- **Min Bars Between Pivots**: separación mínima entre pivotes (default: 3)

### ⏱️ Precision Entry Watch
- **Window**: máximo de velas para confirmación (default: 5 = 5h en 1H)
- **Require Divergence**: fuerza divergencia para ENTRY (toggle)
- **Require OB/FVG Zone**: ENTRY debe estar en zona de soporte/resistencia institucional

### 🎨 Visualization
- **Show Signal S**: mostrar etiquetas ◆ S-LONG/SHORT
- **Show ENTRY**: mostrar etiquetas ◇ ENTRY con arrow
- **Show Fisher Panel**: plot Fisher en panel separado
- **Show Window BG**: sombrear ventana activa

## 📊 Visualización

### Gráfico Principal
- **◆ S-LONG/SHORT** (dorado) — Señal S original cuando se activa
- **◇ ENTRY ↑/↓** (verde/rojo brillante) — Entrada de precisión confirmada
- **Sombreado blanco** (suave) — Ventana de vigilancia activa (5 velas)

### Panel Fisher
- **Línea azul sólida** — Fisher Transform
- **Línea roja punteada** — EMA señal Fisher
- **Líneas grises** — Zonas extremas (±1.5)
- **Coloreado de fondo** — Verde cuando Fisher>+extremo, rojo cuando <-extremo

## 🚀 Flujo de Uso

### Setup en TradingView
1. Cargar en gráfico **1H** o **4H** (configuración optimizada)
2. Desactivar OB/FVG si no están dibujados en tu SMCELITE (no afecta señales)
3. Ajustar **Min Score for Signal S** según agresividad deseada:
   - 5 = señales frecuentes
   - 7 = estándar (recomendado)
   - 9 = muy selectivas

### Interpretación
- **Signal S aparece** → Comienza ventana de vigilancia (5 velas)
- **Fisher entra zona extrema** → sistema "despierta" buscando cruce
- **Fisher cruza su EMA** → si hay divergencia → **◇ ENTRY confirmada**
- **Ventana expira sin ENTRY** → señal descartada, regresa a IDLE

## ⚙️ Filtros Cuantitativos (Scoring)

**Frost Engine (Rango suavizado + ADX)**
- Detecta dirección institucional sin retraso
- Incluye confianza (ADX > 20 = +1 punto)

**WAE Explosion (MACD + Bollinger)**
- Momentum > umbral de "explosión"
- Filtra falsas rupturas en mercados laterales

**Choppiness Index**
- Bloquea señales en mercados choppy (CI > 50)
- Mejora calidad de entradas en tendencias claras

**Volume Absorption**
- Detecta velas de absorción institucional
- Baja wick + alto volumen = rechazo del mercado

## 📝 Notas Técnicas

### Divergencia de Momentum (Simplificada)
En esta v1, la divergencia se detecta como:
- **Alcista**: nuevo mínimo de precio sin nuevo mínimo de momentum en últimas N barras
- **Bajista**: nuevo máximo de precio sin nuevo máximo de momentum en últimas N barras
- Se puede mejorar con lógica de pivotes más sofisticada

### FVG/OB Proximity
El indicador está preparado para incluir proximidad de FVG/OB, actualmente simplificado.
Para máxima precisión, activar FVG/OB en SMCELITE y ajustar `requireZoneEntry`.

### Fidelidad vs SMCELITE
Esta v1 utiliza filtros simplificados sin el motor completo de estructura del SMCELITE.
Las señales S pueden diferir ligeramente, pero la lógica de entrada de precisión es independiente.

## 🎓 Mejoras Futuras

- [ ] Integrar motor de `structure()` completo del SMCELITE
- [ ] Detección de divergencia con pivotes exactos (barssince)
- [ ] OB/FVG confirmation zones con box graphics
- [ ] Alertas personalizadas para ENTRY vs Signal S
- [ ] Backtest integration metrics

## 📞 Soporte

Si hay errores de compilación en TradingView:
1. Verificar que sea Pine Script v6
2. Revisar sintaxis ternaria (debe estar entre paréntesis)
3. Asegurar que no hay punto y coma dentro de líneas de asignación múltiple

---
**Versión**: 1.0
**Pine Script**: v6
**Última actualización**: 2026-04-23
