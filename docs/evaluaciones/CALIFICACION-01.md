# Retroalimentación — Fundamentos, complejidad y recurrencias

**Estudiante:** Carolina Uribe Builes · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-06 23:59 · **Versión revisada:** commit `31327ea`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 21 / 25 |
| Calidad de la explicación teórica | 21 / 25 |
| Corrección de la implementación | 16 / 20 |
| Calidad del análisis de las gráficas | 15 / 20 |
| Documentación y organización del informe | 6 / 10 |
| **Total** | **79 / 100** |
| **Nota (0–5)** | **3.95** |

## 1. Corrección conceptual (21 / 25)
**Lo que hizo bien:**
- Distingue bien entre un algoritmo correcto y uno eficiente, y nombra la ventana de cuatro horas como la restricción que se incumple.
- Explica que un servidor el doble de rápido solo reduce el tiempo a la mitad y no cambia el crecimiento cuadrático.
- Su ejemplo propio (sincronizar 1800 empleados con una consulta por registro) tiene datos y una restricción clara.
- Relaciona el tiempo de ejecución con el consumo de energía y señala al paciente como quien asume el mayor costo, además del equipo de desarrollo y el centro de contacto.

**Lo que puede mejorar:**
- En la Parte 2 la energía se menciona en general, pero no explica con claridad por qué el gasto se acumula noche tras noche durante años.
- Los dos perjuicios (paciente y centro de contacto) pueden desarrollarse más, indicando para cada uno quién paga el error.
- La discusión sobre que el orden decide a quién se llama primero es muy breve.

## 2. Calidad de la explicación teórica (21 / 25)
**Lo que hizo bien:**
- Define peor caso, mejor caso y promedio indicando que se toman sobre entradas de tamaño fijo `n`, y justifica usar el peor caso por la ventana estricta.
- Deja escrita la predicción antes del experimento (A promedio, B mejor, C peor).
- Plantea la recurrencia `T(n) = 2T(n/2) + Θ(n)` y la resuelve con el método maestro, llegando a `Θ(n log n)`.
- Hace el análisis de insertion sort línea por línea y presenta la tabla de complejidades.

**Lo que puede mejorar:**
- En la imagen del método maestro escribe `f(n) = 2`, pero debe ser `f(n) = Θ(n)`. La conclusión es correcta, pero ese dato está mal.
- No explica de dónde sale cada término de la recurrencia (por qué 2 subproblemas, por qué `n/2`, por qué el costo de combinar es lineal).
- En la tabla de líneas, `datos.copy()` aparece ejecutándose `n` veces, pero se ejecuta una sola vez.

## 3. Corrección de la implementación (16 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien (de mayor a menor), no alteran la lista recibida, cuentan comparaciones entre elementos y no usan `sorted()` ni `sort()`.
- `merge_sort` tiene su propia mezcla recursiva en la función `merge`.
- Los tres generadores producen listas del tamaño pedido, sin repetidos, y la semilla permite repetir los resultados.
- Los docstrings están completos y las funciones tienen type hints.

**Lo que puede mejorar:**
- Hay incumplimientos de PEP 8: comentarios pegados al código sin dos espacios, una sola línea en blanco entre funciones, varios `import` en una línea y líneas demasiado largas en los scripts de las partes 3 y 4.
- Quedaron los comentarios `# TODO` de la plantilla dentro del código.

## 4. Calidad del análisis de las gráficas (15 / 20)
**Lo que hizo bien:**
- La gráfica `parte4_tiempo.png` tiene título, ejes con unidades y leyenda, y muestra bien cómo insertion sort se dispara mientras merge sort casi no crece.
- Identifica con cifras que C es el peor caso, B el mejor y A cercano al promedio, y lo contrasta con su predicción.
- El concepto técnico recomienda merge sort, estima 17,4 horas para insertion sort y unos 6 segundos para merge sort, declara que son estimaciones, responde a la propuesta del servidor y menciona la memoria adicional.

**Lo que puede mejorar:**
- Las dos gráficas de la Parte 3 son de barras y no tienen unidades en los ejes (el tiempo debe decir "segundos"). El escenario B casi no se ve, y debía compararse en los mismos ejes con curvas que muestren la forma de crecimiento.
- En 4.3 dice que, en todos los escenarios, merge sort fue mejor. Eso no es cierto para el escenario B, donde insertion sort es casi instantáneo. Además, esa comparación en los tres escenarios no está en el código entregado, así que no se puede verificar.
- La extrapolación está bien encaminada, pero conviene escribir el cálculo paso a paso (el factor por el que crece `n` y cómo se aplica).

## 5. Documentación y organización del informe (6 / 10)
**Lo que hizo bien:**
- El informe sigue el orden de las partes, enlaza el código de cada parte, tiene instrucciones para reproducir y 12 commits con mensajes descriptivos.

**Lo que puede mejorar:**
- No siguió la convención de rama: el trabajo está en `master` y no en `main`.
- Las imágenes del informe usan direcciones completas de GitHub apuntando a un commit específico, no rutas relativas a la carpeta del `README.md`.
- `parte3_casos.py` no genera las gráficas (se hicieron aparte), y `parte4_complejidad.py` guarda la imagen en la carpeta del laboratorio y no en `graficas/`. Así el experimento no se reproduce por completo.
- Las instrucciones de entorno solo sirven para Windows. Se agregó una carpeta `github-imagenes/` dentro del laboratorio que no hace parte del entregable.

## ¿El código funciona?
Sí. Los dos algoritmos ordenan bien, los generadores funcionan y `parte3_casos.py` y `parte4_complejidad.py` corren sin errores y muestran los resultados. Solo la Parte 4 produce una gráfica, y la guarda fuera de `graficas/`.

## Para el próximo laboratorio
- Entregue en la rama `main` y use rutas relativas para las imágenes.
- Haga que cada script genere sus propias gráficas dentro de `graficas/`, con ejes rotulados con unidades y curvas en los mismos ejes.
- Revise el estilo PEP 8 (espacios antes de comentarios, dos líneas en blanco entre funciones, un `import` por línea, líneas cortas) y quite los `TODO`.
- Explique cada término de las recurrencias y revise los datos de sus desarrollos (por ejemplo, el valor de `f(n)`).
- Compruebe que lo que afirma en el informe se pueda ver en su código y en sus gráficas.
