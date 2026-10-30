# Retroalimentación — Laboratorio 2: Dividir y vencer

**Estudiante:** Carolina Uribe Builes · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-30 23:59 · **Versión revisada:** commit `58e67b3`

Muy buen trabajo: el laboratorio está completo, funciona y su informe es claro.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 18 / 20 |
| Calidad de la explicación teórica | 18 / 20 |
| Corrección de la implementación | 24 / 25 |
| Calidad del análisis de las gráficas | 23 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **93 / 100** |
| **Nota (0–5)** | **4.65** |

## 1. Corrección conceptual (18 / 20)
**Lo que hizo bien:**
- Identifica con sus datos que desde n = 100 divide y vencerás gana, y explica que en tamaños pequeños el costo de las llamadas recursivas todavía pesa.
- Compara con el máximo de un arreglo: combinar cuesta solo una comparación, la recurrencia da `Θ(n)` y por eso dividir no mejora nada.
- Recomienda divide y vencerás, estima el tiempo con 1.000.000 de registros para ambos algoritmos y declara que es una estimación.

**Lo que puede mejorar (y cómo corregirlo):**
- La estimación de divide y vencerás usa 0.02 s (cifra redondeada) como base, aunque su tabla dice 0.022 s. Por eso el resultado queda algo por debajo de lo que daría su propia medición.
  → *Cómo corregirlo:* parta siempre del valor exacto de su tabla y rehaga la cuenta con ese número.
- La estimación solo se apoya en un tamaño (n = 8000) y no menciona que, como las mediciones no se repitieron, la base puede tener ruido.
  → *Cómo corregirlo:* agregue una frase que explique cuánto confía en esa base y por qué el resultado es solo un orden de magnitud.

## 2. Calidad de la explicación teórica (18 / 20)
**Lo que hizo bien:**
- Plantea `T(n) = 2T(n/2) + Θ(n)` explicando los dos subproblemas de tamaño n/2 y el costo lineal del caso cruzado.
- Resuelve con el método maestro, comparando `n^(log_2 2) = n` con `f(n)`, y concluye `Θ(n log n)` por el caso 2.
- Explica que la fuerza bruta es `Θ(n²)` por sus dos ciclos.

**Lo que puede mejorar (y cómo corregirlo):**
- La justificación del `Θ(n²)` es muy breve: dice que las combinaciones crecen como n², pero no cuenta cuántas son.
  → *Cómo corregirlo:* indique cuántas veces se repite el ciclo interno para cada inicio y qué suma resulta al sumar todos los inicios.

## 3. Corrección de la implementación (24 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en todos los casos pedidos: serie de ocho días, un elemento, todos negativos, todos positivos y un caso que cruza el punto medio.
- Las 20 listas aleatorias coinciden entre ambos algoritmos, y las pruebas comparan la suma, no los índices.
- `subarreglo_maximo` resuelve los tres casos sin llamar a la fuerza bruta, no cambia la lista recibida y la fuerza bruta acumula la suma sin recalcularla.
- Las funciones tienen *type hints*, *docstrings* con `Args` y `Returns` y dos líneas en blanco entre ellas.

**Lo que puede mejorar (y cómo corregirlo):**
- Las listas aleatorias de `pruebas.py` no usan semilla fija, así que cada ejecución prueba listas distintas y un fallo ocasional no se podría repetir.
  → *Cómo corregirlo:* llame a `random.seed(...)` con un número fijo antes de generar las listas.

## 4. Calidad del análisis de las gráficas (23 / 25)
**Lo que hizo bien:**
- La gráfica `tiempo_vs_n.png` tiene ambas curvas en los mismos ejes, título, ejes rotulados y leyenda, con siete tamaños.
- Lo que dice el informe coincide con la gráfica: la fuerza bruta llega a cerca de 2.2 segundos en n = 8000 y divide y vencerás queda casi pegada al eje.
- Calcula el factor al duplicar n (de 4000 a 8000) para ambos algoritmos, lo contrasta con lo esperado y da una posible razón de que la fuerza bruta crezca menos de lo previsto.
- Incluye una tabla con los valores medidos, que ayuda a leer los tamaños pequeños.

**Lo que puede mejorar (y cómo corregirlo):**
- Cada tiempo se midió una sola vez, y el informe lo dice. Con una sola medición, el factor de 2.60 de la fuerza bruta puede deberse al ruido y no a la caché; esa explicación queda sin comprobar.
  → *Cómo corregirlo:* repita cada medición unas tres veces dentro de `medicion.py` y use el promedio o la mediana antes de graficar y de calcular los factores.
- Solo se calcula un par de tamaños consecutivos.
  → *Cómo corregirlo:* calcule el factor también en otro par donde n se duplique (por ejemplo 500 y 1000) para ver si el patrón se mantiene.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- La carpeta `laboratorios/lab2-divide-y-vencer/` está en una ubicación válida y trae todos los archivos pedidos.
- El `README.md` tiene su nombre, las instrucciones para reproducir, y las partes en orden; la gráfica se incrusta con ruta relativa que sí encuentra el archivo y cada parte enlaza su código.
- Hay varios commits con mensajes descriptivos.

## ¿El código funciona?
Sí. Las pruebas pasan sin errores, la medición corre completa y genera la gráfica en `graficas/`.
