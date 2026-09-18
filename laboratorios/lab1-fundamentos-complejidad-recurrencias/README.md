# Curso análisis de algoritmos 
## Estudiante: Carolina Uribe Builes


## Propósito carpetas y archivos  

* algoritmos.py: 
* datos.py: 
* parte3_casos.py: 
* parte4_complejidad.py: 
* graficas/: 

## Intrucciones para reproducir el experimento (PENDIENTE)
El proyecto fue desarrollado utilizando exclusivamente la biblioteca estándar de Python (`time`, `random`, `math`), por lo que no requiere la instalación de librerías ni dependencias externas.
Para la correcta reproducción del entorno basta con seguir los siguientes pasos:
1. Abra una terminal dentro de la carpeta nombrada 'lab1-fundamentos-complejidad-recurrencias' y ejecute los siguientes comandos:
    -  python -m venv venv
    -  venv\Scripts\activate

2. Para ejecutar el archivo 'parte3_casos.py' ejecute:
    - python parte3_casos.py

## Parte 1 - Respuesta argumentativa

El querer comprar un servidor que ofrezca el doble de velocidad que se tiene ahora mismo no solucionaría completamente el problema presentado, tal vez reduciría algo, pero ese algo sería insignificante, por lo que no es viable para el problema de la plataforma Tamiza. En cuanto a corrección, se dice que un algoritmo es correcto si entrega el resultado esperado a un problema planteado sin importar el tamaño de la entrada que reciba; para el caso del insertion sort, devuelve el resultado esperado sólo cuando se le permita finalizar todas las iteraciones y para el caso de Tamiza esto no pasa, no significa que el insertion sort no esté funcionando, sucede que no se le está dando el tiempo necesario para finalizar todo el proceso debido a la gran cantidad de registros. Por otro lado, la eficiencia determina que tantos recursos de tiempo y memoria requiere para llegar al resultado correcto, por lo tanto, el hecho de que un algoritmo sea correcto no significa que también sea eficiente. 

Ahora mismo, la plataforma Tamiza incumple con la restricción de la ventana temporal de 4 horas, obligando al centro a trabajar con listas que no están ordenadas en su totalidad, esto no significa que el insertion sort no esté funcionando, sucede que no se le está dando el tiempo necesario para finalizar todo el proceso debido al volumen de registros que se maneja actualmente. Duplicar la velocidad del servidor no soluciona el problema, ya que el verdadero cuello de botella se encuentra en el algoritmo. Insertion sort tiene una complejidad temporal de O(n²), por lo que, al aumentar la cantidad de datos 60 veces, el número de operaciones crece aproximadamente (602=3600) veces. Al implementar un servidor dos veces más rápido únicamente se reduce el tiempo de ejecución a la mitad, pero no modifica el crecimiento cuadrático propio del algoritmo. Es por esto que la solución que ofrecen basada en hardware dejaría de ser insuficiente si la cantidad de registros sigue aumentando en poco tiempo, a lo que propongo que la mejor solución es cambiar de algoritmo, haciendo uso del mergesort y su complejidad temporal de O(n log n).

Un caso personal donde un algoritmo correcto resultó siendo inviable ocurrió durante mis prácticas en un entorno hospitalario. Desarrollé un módulo para sincronizar la información de aproximadamente 1800 empleados entre dos APIs REST y una base de datos relacional. La lógica usada era correcta ya que procesaba y actualizaba a cada usuario con sus cargos y centros de costos adecuados, sin embargo, realizaba una consulta SQL individual por cada registro, lo que generaba aproximadamente n comunicaciones entre la BD y la aplicación, resultando en tiempos de ejecución de 20 segundos que incumplían con la restricción de latencia máxima del navegador web. Aunque la solución no corrompía datos ni retornaba información incorrecta, resultaba inviable teniendo en cuenta la ventana de latencia. Para solucionar esta situación, no fue necesario migrar a una base de datos más potente, sino optimizar y reestructurar la lógica de consultas.


## Parte 2

Ambientalmente hablando, el algoritmo se ejecuta todas las noches dentro de una ventana inicial de cuatro horas, lo que de por sí representa un consumo considerable de energía. Sin embargo, este consumo aumenta debido a la poca optimización del algoritmo, ya que se utiliza Insertion Sort para procesar una entrada de aproximadamente 1.200.000 registros. En la actualidad no basta con desarrollar una solución que funcione correctamente; también es importante considerar el impacto ambiental que genera, como el consumo energético y los recursos necesarios para mantener operativos los servidores, por ejemplo, el agua utilizada en sistemas de refrigeración. En este caso, la gran cantidad de operaciones que debe realizar Insertion Sort incrementa el tiempo de ejecución y, en consecuencia, el consumo de energía. El consumo de energía en las madrugadas se multiplica con el paso de los años, debido a que el sistema va a ir recibiendo cada vez más registros, ocasionando un mayor desbordamiento de la ventana de tiempo. En otras palabras, mientras más registros haya, más tiempo le toma a Insertion Sort ordenar la información y retornar el resultado esperado. Es por esto que lo ideal sería implementar un algoritmo más eficiente que reduzca el tiempo de procesamiento y, con ello, el consumo energético.

La lentitud del algoritmo provoca que no se tenga en cuenta de una manera oportuna el nivel de riesgo de un paciente, lo que puede poner en peligro su vida. En este caso, quien asume el mayor costo del error es el paciente. Sin embargo, la responsabilidad del problema también recae en el equipo de desarrollo, ya que la selección de Insertion Sort no contempló el crecimiento en el volumen de los datos. Además, el centro de contacto también se ve perjudicado al tener que trabajar con listas parciales o sin priorización por nivel de riesgo, lo que entorpece sus labores y disminuye la eficiencia del proceso.

Por último, una tensión propia de este caso es que el orden de la lista determina qué paciente recibe primero la llamada, lo que implica una gran responsabilidad para el algoritmo; ya que no basta con que el ordenamiento que produce sea rápido, sino que también debe garantizar una correcta priorización de los pacientes mediante el nivel de riesgo, con el fin de evitar retrasar la atención de un paciente que requiere mayor prioridad.


## Parte 3 
[CÓDIGO DE LA PARTE 3](https://github.com/Carolinaubes/analisis-algoritmos-carolinaubes/blob/f038b8a4f02f13e0494f2904325f08c2836e5bb9/laboratorios/lab1-fundamentos-complejidad-recurrencias/parte3_casos.py)
## 3.1 Explicación 

A continuación, se da una breve explicación de los 3 casos posibles, agregando en cada uno de ellos un ejemplo asociado al algoritmo Insertion Sort ([algoritmos.py](https://github.com/Carolinaubes/analisis-algoritmos-carolinaubes/blob/f038b8a4f02f13e0494f2904325f08c2836e5bb9/laboratorios/lab1-fundamentos-complejidad-recurrencias/algoritmos.py)). 

- Peor caso: Es el escenario más desfavorable posible, donde se realiza el máximo número de comparaciones y se obtiene el mayor tiempo de ejecución para ordenar una entrada de tamaño fijo “n”. Se puede observar cuando se reciben datos en el orden inverso al que se necesita, obligando a mover todos los elementos.

- Mejor caso: Es el escenario más favorable porque realiza el mínimo número de comparaciones y se obtiene el menor tiempo de ejecución para ordenar una entrada de tamaño fijo “n”. Se puede observar cuando los datos recibidos ya vienen en el orden esperado; es acá donde solo se revisa sin la necesidad de mover elementos.

- Caso promedio: Es el escenario más típico, en donde se realiza el número promedio de comparaciones y obtiene el tiempo esperado de ejecución a la hora de ordenar una entrada de tamaño fijo “n”. Se observa cuando los datos recibidos vienen en orden aleatorio.

Al tener una restricción tan importante como lo es la ventana de 4 horas, se vuelve indispensable implementar un algoritmo que pueda cumplir con lo solicitado, ofreciendo resultados esperados sin importar el tamaño de la entrada de los datos que reciba. Para lograr esto, la mejor opción sería probar en el peor de los casos, ya que allí se estaría evaluando la duración máxima del proceso de ordenamiento. 

Para la situación problema del centro Tamiza se identifica que:

- Caso A: Corresponde al caso promedio al proveer una entrada de datos cuyos elementos se encuentran en un orden aleatorio; esto debido a la carga directa desde el portal web de los laboratorios.
- Caso B: Corresponde al mejor caso porque se menciona que al recibir la información como un reproceso sobre la lista del día anterior, ésta ya viene ordenada casi en su totalidad, obligando a realizar una cantidad muy mínima de desplazamientos sobre los elementos no ordenados. 
- Caso C: Corresponde al peor caso al mencionar que los datos vienen distribuidos en orden inverso, es decir, de menor a mayor, alcanzando la mayor cantidad de comparaciones y desplazamientos.

Puede analizar la lógica utilizada para llevar a cabo cada uno de los casos accediendo al archivo [datos.py](https://github.com/Carolinaubes/analisis-algoritmos-carolinaubes/blob/f038b8a4f02f13e0494f2904325f08c2836e5bb9/laboratorios/lab1-fundamentos-complejidad-recurrencias/datos.py)

## 3.2 Demostración experimental

Los resultados experimentales presentados en las gráficas confirman con precisión las predicciones planteadas en la sección anterior (3.1), tanto para el número de comparaciones como para el tiempo de ejecución:
- El escenario A fue el que más se aproximó al caso promedio. Con n = 100 realizó 2542 comparaciones en 0.000318 segundos, escalando a 648.481 comparaciones en 0.123328 segundos para n = 1600 y superando los 10 millones en 1.786217 para n = 6400
- El escenario B fue el mejor caso. Con n = 100 realizó 99 comparaciones en 0.000017 segundos, escalando a 1843 comparaciones en 0.000384 segundos para n = 1600 y alcanzando apenas los 10.649 en 0.002223 segundos para n = 6400.
- El escenario C fue el peor caso. Con n = 100 realizó comparaciones en 0.000602 segundos, escalando a 1.279.200 comparaciones en 0.257077 segundos para n = 1600 y superando los 20 millones en 3.318880 segundos para n = 6400.


### Gráfica: Comparaciones vs Tamaño de Entrada
![image alt](https://github.com/Carolinaubes/analisis-algoritmos-carolinaubes/blob/f038b8a4f02f13e0494f2904325f08c2836e5bb9/laboratorios/lab1-fundamentos-complejidad-recurrencias/graficas/parte3_comparaciones.png)

### Gráfica: Tiempo vs Tamaño de Entrada
![image alt](https://github.com/Carolinaubes/analisis-algoritmos-carolinaubes/blob/f038b8a4f02f13e0494f2904325f08c2836e5bb9/laboratorios/lab1-fundamentos-complejidad-recurrencias/graficas/parte3_tiempo.png)

## Parte 4

## 4.1 Cálculo teórico

El algoritmo Merge Sort divide el arreglo en dos subproblemas de tamaño n/2, resuelve recursivamente cada uno de ellos y posteriormente fusiona ambas partes ya ordenadas recorriendo todos los elementos de una sola vez. Es por esto que su recurrencia es: T(n)=2T(n/2)+Θ(n)

Para obtener la cota final se hace uso del método maestro sobre la recurrencia planteada anteriormente donde se identifican los siguientes elementos:

![image alt](https://github.com/Carolinaubes/analisis-algoritmos-carolinaubes/blob/1a855a429f44cb0677dfd4bf9cb453c0af52fd38/laboratorios/lab1-fundamentos-complejidad-recurrencias/github-imagenes/desarrollo_metodo_maestro.png)

### Calculo de cota de Insertion Sort

Teniendo en cuenta la implementación del método Insertion Sort:

```
def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    datos_copy = datos.copy()  # Línea 1
    contador_comparaciones = 0  # Línea 2

    for i in range(1, len(datos_copy)):  # Línea 3
        clave = datos_copy[i]  # Línea 4
        j = i - 1  # Línea 5

        while j >= 0:  # Línea 6
            contador_comparaciones += 1  # Línea 7
            if datos_copy[j] < clave:  # Línea 8
                datos_copy[j + 1] = datos_copy[j]  # Línea 9
                j -= 1  # Línea 10
            else:  # Línea 11
                break  # Línea 12

        datos_copy[j + 1] = clave  # Línea 13

    return (datos_copy, contador_comparaciones)  # Línea 14
```

A partir del código anterior, se analiza el costo computacional de cada una de las instrucciones, en donde:
- t_i: Corresponde al número de veces que se comprueba la condición del bucle 'while' para la iteración i.
- m_i: Es el número de desplazamientos efectivos de elementos hacia la derecha.
- e_i: Corresponde al indicador de salida anticipada por el 'break'. Vale 1 si encontró la posición y 0 si llegó hasta el inicio de la lista.

| Línea | Instrucción | Costo | Veces ejecutada |
| :---: | :--- | :---: | :---: |
| 1 | `datos_copy = datos.copy()` | c_1 | n |
| 2 | `contador_comparaciones = 0` | c_2 | 1 |
| 3 | `for i in range(1, len(datos_copy)):` | c_3 | n |
| 4 | `clave = datos_copy[i]` | c_4 | n - 1 |
| 5 | `j = i - 1` | c_5 | n - 1 |
| 6 | `while j >= 0:` | c_6 | sum_{i=1}^{n-1} t_i |
| 7 | `contador_comparaciones += 1` | c_7 | sum_{i=1}^{n-1} (t_i - 1) |
| 8 | `if datos_copy[j] < clave:` | c_8 | sum_{i=1}^{n-1} (t_i - 1) |
| 9 | `datos_copy[j + 1] = datos_copy[j]` | c_9 | sum_{i=1}^{n-1} m_i |
| 10 | `j -= 1` | c_10 | sum_{i=1}^{n-1} m_i |
| 11 | `else:` | c_11 | sum_{i=1}^{n-1} e_i |
| 12 | `break` | c_12 | sum_{i=1}^{n-1} e_i |
| 13 | `datos_copy[j + 1] = clave` | c_13 | n - 1 |
| 14 | `return (datos_copy, contador_comparaciones)` | c_14 | 1 |

El tiempo total T(n) sale como un resultado de la sumatoria ponderada de los costos (c_k) de todas las líneas, quedando expresado como:

![image alt](https://github.com/Carolinaubes/analisis-algoritmos-carolinaubes/blob/dd87b7a65bb3a84bf322385b9ae77050effc58bd/laboratorios/lab1-fundamentos-complejidad-recurrencias/github-imagenes/tiempo_total.png)

El comportamiento del algoritmo es dependiente del valor que tome t_i, por lo tanto, analizando lo obtenido:
- En el mejor caso, el ciclo que se encuentra en el interior solo realiza una verificación por cada iteración (t_i = 1) y la sumatoria se comporta de forma lineal, permitiendo determinar que el término dominante es n, lo que resulta en una complejidad Θ(n).
- En el promedio y peor caso, el ciclo interior está obligado a recorrer varios o todos los elementos anterior (t_i crece de manera proporcional a i) y la sumatoria aritmética produce un factor n(n-1)/2, haciendo que el término dominante sea n², lo que resulta en una complejidad Θ(n²).

La complejidad de cada algoritmo para el mejor caso, peor y promedio se ve reflejada en la siguiente tabla:

| Algoritmo | Mejor Caso | Caso Promedio | Peor Caso |
| :--- | :---: | :---: | :---: |
| **Insertion Sort** | Θ(n) | Θ(n²) | Θ(n²) |
| **Merge Sort** | Θ(n log n) | Θ(n log n) | Θ(n log n) |

### Notas adicionales

