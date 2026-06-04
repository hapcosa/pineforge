# Manual · ICT NYC SCALPER MODE + ICT NYC OSCILATOR

Sistema de 2 piezas para operar **exclusivamente la sesión de New York**.
- **ICT NYC SCALPER MODE** (sobre el precio) → marca el setup y la entrada.
- **ICT NYC OSCILATOR** (panel inferior) → confirma con dinero institucional + ciclo.

Regla de oro: **el scalper propone, el oscilador confirma.** Solo entras cuando los dos coinciden.

---

## 1. Instalación en TradingView

1. Abre TradingView → un gráfico cualquiera.
2. Botón **Pine Editor** (abajo).
3. Pega `ict_ny_scalper.pine` → **Add to chart** (sale sobre las velas).
4. Abre otra pestaña en el Pine Editor (`+`), pega `ict_nyc_oscilator.pine` → **Add to chart** (sale en panel abajo).
5. Guarda ambos (icono guardar) para tenerlos en *Indicators → My scripts*.

> Si ves un foco rojo de error: copia el texto exacto + número de línea. Los avisos del editor que dicen "undefined timeframe.isdwm" o similares suelen ser falsos; lo que importa es que compile al darle *Add to chart*.

---

## 2. Activos recomendados (los más usados en NY)

| Activo | Símbolo TradingView | Por qué |
|---|---|---|
| **NASDAQ** | `NAS100` / `US100` / `MNQ1!` | El rey del scalping NY. Volumen real, killzone limpísima. |
| **S&P500** | `SPX500` / `ES1!` / `MES1!` | Igual de bueno, algo más lento. |
| **BTC** | `BTCUSDT` (Binance) | 24/7 pero reacciona fuerte al open NY. Volumen real. |
| **EUR/USD** | `EURUSD` | Clásico forex. ⚠️ usa *tick-volume* (Money Flow aproximado). |
| **Oro** | `XAUUSD` | Muy activo en NY. |

**Mejores:** NASDAQ y S&P (volumen real = Money Flow fiable). BTC excelente también.
EUR/USD funciona, pero el oscilador es menos preciso por el volumen estimado.

---

## 3. Timeframes

| Estilo | TF entrada | Contexto |
|---|---|---|
| **Scalping (recomendado)** | 1m – 3m | mirar 15m antes |
| Intradía | 5m – 15m | 1H |

El indicador solo dispara dentro de la **killzone NY** (apertura). Fuera de esa ventana, no hay señales (es a propósito).

---

## 4. Cómo leer el SCALPER (sobre el precio)

- **Cajas de colores** = sesiones: ASIA (azul), LONDON (naranja), NYC (verde). La etiqueta muestra el **máx (H)** y **mín (L)** de cada sesión.
- **Líneas BSL/SSL** = liquidez (los stops de la gente):
  - **BSL** (arriba) = stops de los shorts.
  - **SSL** (abajo) = stops de los longs.
  - Cuando una se rompe se vuelve **punteada + ✗** = liquidez ya barrida.
- **🔔** arriba = **apertura de Wall Street** (09:30 ET). Empieza lo bueno.
- **🧲 Imán** = a dónde quiere ir el precio (liquidez más cercana sin tomar). Es tu objetivo.
- **Cajas FVG** (verde/roja) = desequilibrios; se borran solas al rellenarse. Son zonas de entrada.
- **Zonas Premium (roja) / Descuento (verde)** + línea **EQ** dorada = caro vs barato.
  Regla: **compra en descuento, vende en premium.**

### La secuencia (Power of 3 / AMD)
1. **Acumulación**: Asia y London arman un rango (dejan liquidez arriba y abajo).
2. **Manipulación**: NY abre y **barre** una liquidez (la `✗` aparece, sale un `✗` xcross). Es la trampa.
3. **Distribución**: el precio gira → sale la flecha **▲ BULL** o **▼ BEAR** con SL y TP1/TP2/TP3.

El dashboard (arriba derecha) te dice en qué fase estás: `MANIPULACION` → prepárate; señal → entra.

---

## 5. Cómo leer el OSCILADOR (panel inferior)

Es una línea 0–100 que mezcla **ciclo (COG Ehlers) + momentum + dinero (Money Flow)**.

- **Sobre 50** y verde = sesgo alcista / acumulación.
- **Bajo 50** y rojo = sesgo bajista / distribución.
- **Línea blanca** = media de señal (cruces = giros).
- **Barras de fondo** = Money Flow (verde acumulación, rojo distribución).
- **Niveles Fibo "—"** (0.382 / 0.5 / 0.618): si el oscilador se **frena** justo en uno, ahí hay decisión:
  - rebota en **0.382** desde abajo = fin del descuento → posible LONG.
  - se topa con **0.618** desde arriba = fin del premium → posible SHORT.
- **● BUY / ● SELL** = señal del oscilador. **▲▼** = divergencia (precio nuevo extremo, oscilador no → giro probable).
- **Cuadro arriba-derecha** = veredicto: `CONFIRMA LONG · ACUMULACIÓN · 0.382–0.5`.

---

## 6. Cómo operar (paso a paso)

1. Espera la **🔔** (apertura NY). Antes de eso, no operas.
2. Mira que el scalper marque **MANIPULACION** (barrió una liquidez, salió `✗`).
3. Espera la **flecha** del scalper (`▲ BULL` en descuento / `▼ BEAR` en premium).
4. Mira el **oscilador**: debe decir `CONFIRMA LONG` (o SHORT) y el Money Flow ir a favor.
   - Bonus de alta probabilidad: divergencia ▲/▼ o rebote en un fibo del oscilador.
5. **Entrada A+** = flecha del scalper **+** confirmación del oscilador → entras.
6. **SL** = el que dibuja el scalper (detrás de la liquidez barrida).
7. **Salidas**: cierra parcial en **TP1 (2R)**, mueve SL a break-even, deja correr a **TP2 (3R)** / **TP3 (4R)**. El **🧲 imán** te dice si hay espacio hasta la próxima liquidez.

### Cuándo NO operar
- No salió la campana / fuera de killzone.
- El scalper marca pero el oscilador dice `Neutro` o el Money Flow va en contra.
- El oscilador está **plano pegado a un fibo** sin cruzar su media = sin convicción.
- Viernes después del cierre, sábado, domingo (el indicador ya los bloquea).

---

## 7. Parámetros ideales (presets)

### Scalping NASDAQ / BTC 1–3m (recomendado)
**Scalper:** Activo = preset correcto (o Auto) · Mín. confluencias = 2 · MSS micro pivote = 2.
**Oscilador:** COG = 9 · Momentum = 10 · Normalización = 34 · Suavizado = 2 · Media = 9 · Money Flow = 14 · "Exigir Money Flow a favor" = ON.

### Más estricto (menos señales, mejor calidad)
**Scalper:** Mín. confluencias = 3.
**Oscilador:** Suavizado = 3, divergencias ON.

### Intradía 5–15m
**Scalper:** MSS = 3 · dealing range Lookback = 60.
**Oscilador:** COG = 14 · Normalización = 50 · Media = 14.

---

## 8. Gestión de riesgo (disciplina)
- Máximo **1 setup por killzone** (ya forzado por defecto).
- Riesgo fijo por trade (ej. 0.5–1% de la cuenta).
- Siempre parcial en TP1 + break-even. Nunca muevas el SL en contra.
- Si pierdes 1–2 seguidos, cierra el día. NY ya te dio su oportunidad.

---

## 9. Resumen en una frase
> Espera la campana de NY → deja que barra la liquidez de Asia/London → entra **a favor** del giro cuando el oscilador confirme acumulación/distribución y el precio esté en descuento/premium → SL bajo la liquidez, TP hacia el imán.
