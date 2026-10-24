# Retroalimentación — Laboratorio 2: Dividir y vencer

**Estudiante:** Carolina Uribe Builes · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `1a96076`

Muy buen trabajo: el código es correcto y el informe se apoya en sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 18 / 20 |
| Calidad de la explicación teórica | 17 / 20 |
| Corrección de la implementación | 24 / 25 |
| Calidad del análisis de las gráficas | 22 / 25 |
| Documentación y organización del informe | 8 / 10 |
| **Total** | **89 / 100** |
| **Nota (0–5)** | **4.45** |

## 1. Corrección conceptual (18 / 20)
**Lo que hizo bien:**
- Identificó con sus datos que divide y vencerás empieza a ganar en n = 100 y explicó por qué antes pierde (el costo de las llamadas recursivas).
- Comparó con el máximo de un arreglo: combinar cuesta Θ(1), la recurrencia da Θ(n) y no hay mejora frente a un solo recorrido.
- Recomendó divide y vencerás y estimó el tiempo con 1.000.000 de registros (unas 9.5 horas contra unos 4 segundos), declarándolo como estimación y sin regla de tres lineal.

**Lo que puede mejorar:**
- En el tamaño n = 100 la ventaja es muy pequeña (0.000235 s contra 0.000275 s); conviene decir que con una sola medición ese punto de cruce es poco firme.
- Para la estimación de divide y vencerás usó 0.02 s redondeado; es mejor partir del valor medido (0.022 s).

## 2. Calidad de la explicación teórica (17 / 20)
**Lo que hizo bien:**
- Planteó T(n) = 2T(n/2) + Θ(n), explicó los dos subproblemas y el costo lineal del caso cruzado.
- Resolvió con el método maestro, comparó n^(log₂2) = n con f(n) y concluyó el caso 2 y Θ(n log n).

**Lo que puede mejorar:**
- Para la fuerza bruta dijo que las combinaciones "crecen proporcionalmente a n²"; falta mostrar el conteo (n + (n−1) + … + 1 = n(n+1)/2).
- Faltó explicar un poco más cuánto cuesta cada nivel de la recursión.

## 3. Corrección de la implementación (24 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en todos los casos pedidos y coinciden en listas aleatorias; el caso cruzado y el caso base están bien resueltos.
- No se llama a la fuerza bruta desde divide y vencerás, no se modifica la lista recibida y hay type hints y docstrings.
- El código cumple PEP 8.

**Lo que puede mejorar:**
- Los scripts `pruebas.py` y `medicion.py` no usan una función principal; no es grave, pero queda más ordenado.

## 4. Calidad del análisis de las gráficas (22 / 25)
**Lo que hizo bien:**
- La gráfica tiene título, ejes rotulados, leyenda, ambas curvas en los mismos ejes y siete tamaños.
- Calculó el factor al duplicar n (2.60 para fuerza bruta y 2.04 para divide y vencerás) y lo contrastó con 4 y con ≈2.2. Los valores citados (2.2 s y 0.02 s en n = 8000) coinciden con la gráfica.
- Incluyó una tabla con los valores medidos, útil para los tamaños pequeños.

**Lo que puede mejorar:**
- Fuerza bruta creció 2.6 veces y no 4; atribuirlo a la caché es solo una suposición. Repetir cada medición y usar la mediana ayudaría a comprobarlo.
- No repitió las mediciones, así que el ruido pesa en los tamaños pequeños.

## 5. Documentación y organización del informe (8 / 10)
**Lo que hizo bien:**
- El README sigue el orden pedido, enlaza el código de cada parte, muestra la gráfica y trae instrucciones para Windows, macOS y Linux.
- Hay varios commits descriptivos del laboratorio.

**Lo que puede mejorar:**
- No siguió el nombre de carpeta acordado: la carpeta se llama `lab2-divide-y-venceras` y el entregable pide `lab2-divide-y-vencer`. Estar dentro de `laboratorios/` sí es válido.

## ¿El código funciona?
Sí. Las pruebas pasan, ambas funciones coinciden con un cálculo de referencia en listas aleatorias y `medicion.py` genera la gráfica sin errores.

## Para el próximo laboratorio
- Use exactamente el nombre de carpeta que pide el entregable.
- Al justificar una complejidad, muestre el conteo o la suma paso a paso.
- Repita cada medición varias veces y grafique la mediana para reducir el ruido.
- Apóyese en valores medidos sin redondear al hacer estimaciones.
