# REPORTE DE TRABAJO — Chat "Motores nuevos + Réplica/Híbrido"

> Resumen para que la próxima IA sepa exactamente qué se hizo en este chat y qué falta.
> Leer junto con: `PROMPT_NUEVO_CHAT_BUDAI.md`, `PROMPT_PERSONA_BUDAI.md`,
> `BUDAI_OSCILADORES_GUIA.md`. Fecha de cierre: 2026-06-02.

---

## 1 · CONTEXTO
BudAI Capital® — suite de osciladores Pine Script v6 para TradingView, estética **Athenea**
(onda + brillo blanco + glow fading a 50/0 + fibo morados + nodos/señales doble `plotchar "•"`
+ dashboard tiny + marca de agua `₿ BudAI Cripto`). Se trabaja UNO a la vez, el usuario revisa
en TV y manda capturas; corregir hasta premium. Español, directo. Carpeta osciladores:
`Osciladores/` (el usuario está reorganizando en subcarpetas tipo `Nivel_1_Base/`).

---

## 2 · LO QUE SE HIZO EN ESTE CHAT

### 2.1 · Documentos
- **`PROMPT_PERSONA_BUDAI.md`** (NUEVO) — define la persona del asistente: programador senior
  con IA + creador de indicadores + trader rentable + diseñador obsesivo. Obliga a recordar
  estética/parámetros, buscar corrección, ofrecer y enseñar. Se pega junto al prompt de proyecto.

### 2.2 · Motores nuevos creados (6) — estética Athenea
| Archivo | Nombre | Motor / Núcleo |
|---|---|---|
| `budai_orderflow.pine` | Order Flow Delta | CVD (delta acum. vía `request.security_lower_tf`) onda + delta por vela de fondo + absorción |
| `budai_orderflow_pure.pine` | Order Flow Pro | Order flow PURO: velas de delta (footprint, `plotcandle`) + delta MA + CVD de sesión |
| `budai_reversalcloud.pine` | Reversal Cloud | OVERLAY: nube trailing tipo SuperTrend + reversión + agotamiento |
| `budai_stochrsi.pine` | Stoch RSI Pro | RSI→estocástico doble-suavizado + bandas dinámicas (media±desv) + fusión con sesgo RSI |
| `budai_momentum3d.pine` | Momentum Wave 3D | Momentum normalizado + 3 capas eco (profundidad); apilamiento = aceleración real |
| `budai_tsi.pine` | True Strength Index | TSI clásico: doble EMA del momentum, rango ±100 centrado en 0, divergencias |

### 2.3 · Réplica + Híbrido (a partir de capturas del "Neptune Oscillator")
| Archivo | Nombre | Qué es |
|---|---|---|
| `budai_oceanus.pine` | Oceanus Oscillator | RÉPLICA fiel: WaveTrend + Hyper Wave (kernels 0.8/0.3) + Money Flow MFI 35 + LSMA 21/6 (sobre el osc) + nodos azules + glow blanco + barras top/bottom + divergencias con trazo |
| `budai_hybrid.pine` | Apex Confluence Oscillator | HÍBRIDO maestro: 3 módulos (momentum WT + volumen CMF + tendencia MA) → score −3..+3, modos Conservador/Normal/Agresivo, señales débil/fuerte + zona "No Operar" + agotamiento |

### 2.4 · Correcciones aplicadas en este chat
- **Glow "corrido"**: las señales en `location.top/bottom` con doble `plotchar` de distinto `size`
  quedaban desalineadas. SOLUCIÓN GLOBAL: anclar ambas capas en `location.absolute` al MISMO
  valor (osc / nivel fijo / precio). Aplicado a todos los nuevos. (Guardado en memoria.)
- **Oceanus**: error real `plotchar size="nodeSz"` → `size` debe ser CONST, no derivado de
  `input.string`. Se quitó el selector de tamaño y se fijó `size.small`.
- **Apex**: se quitaron las **barras de score** (plot stepline que dibujaba rectángulos blancos).
  El `scoreNet` sigue en el dashboard.
- **Apex y Reversal Cloud**: demasiadas "×" de agotamiento (se disparaba en CADA barra
  sobreextendida). Cambiado a disparar SÓLO al entrar al evento (`cond and not cond[1]`).

---

## 3 · ESTADO DE LA SUITE
- Antes: 13 osciladores. **Ahora: 21** (13 + 6 motores nuevos + Oceanus + Apex).
- Lista principal de motores pendientes del prompt: **COMPLETA** (Volume Delta, Reversal Cloud,
  Stoch RSI, Momentum 3D, TSI). Opcionales aún sin hacer: **Fisher Transform, Schaff Trend
  Cycle, Ultimate RSI**.

---

## 4 · LO QUE FALTA / PRÓXIMOS PASOS
1. **Revisión visual en TV** de los 6 motores + Oceanus + Apex; afinar (grosor de nube de
   Oceanus, tamaño/cantidad de nodos azules de Apex, etc.). Esperar capturas del usuario.
2. **Osciladores opcionales**: Fisher Transform, Schaff Trend Cycle, Ultimate RSI (si se quieren).
3. **Reorganización de carpetas**: el usuario está moviendo `.pine` a subcarpetas (`Nivel_1_Base/`,
   etc.). Los 8 archivos nuevos se crearon en `Osciladores/` raíz → puede que haya que ordenarlos.
4. **Fase de confluencia** (pendiente histórica): combinar osciladores en sistemas de score.
   Apex ya es un primer paso de confluencia institucional.
5. **Pulir** la suite SMC/tendencia/overlay de la raíz (sigue en pausa).
6. **Manual de uso + presets por activo** (BTC, NASDAQ, EURUSD).

---

## 5 · NOTAS TÉCNICAS PARA NO REPETIR ERRORES
- `plotchar(size=...)` requiere **const** (no `input.string` ni series). Usar `size.tiny/small/normal`.
- Señales con glow → SIEMPRE `location.absolute` al mismo valor (evita el glow corrido).
- Marcas de evento (agotamiento, divergencia) → disparar en la transición `cond and not cond[1]`
  para no saturar de símbolos.
- `request.security_lower_tf` devuelve arrays; verificar `array.size()` y dar fallback si `==0`.
- Aviso `SHORT_TITLE_TOO_LONG` es WARNING, no error: el shorttitle largo es intencional (regla
  del proyecto = nombre completo). Compila igual.
- Linter del IDE da falsos positivos con emojis/acentos: lo que vale es que compile en TradingView.
