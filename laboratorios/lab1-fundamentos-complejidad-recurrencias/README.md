# Curso análisis de algoritmos 
## Estudiante: Carolina Uribe Builes


## Propósito carpetas y archivos  

* algoritmos.py: 
* datos.py: 
* parte3_casos.py: 
* parte4_complejidad.py: 
* graficas/: 

## Intrucciones para reproducir el experimento
El proyecto fue desarrollado utilizando exclusivamente la biblioteca estándar de Python (`time`, `random`, `math`), por lo que no requiere la instalación de librerías ni dependencias externas.
Para la correcta reproducción del entorno basta con seguir los siguientes pasos:
1. Abra una terminal dentro de la carpeta nombrada 'lab1-fundamentos-complejidad-recurrencias' y ejecute los siguientes comandos:
    -  python -m venv venv
    -  venv\Scripts\activate

2. Para ejecutar el archivo 'parte3_casos.py' ejecute:
    - python parte3_casos.py

## Parte 1 - Respuesta argumentativa

El querer comprar un servidor que ofrezca el doble de velocidad que se tiene ahora mismo no solucionaría completamente el problema presentado, tal vez reduciría algo, pero ese algo sería insignificante, por lo que no es viable para el problema de la plataforma Tamiza. En cuanto a corrección, se dice que un algoritmo es correcto si entrega el resultado esperado a un problema planteado sin importar el tamaño de la entrada que reciba; para el caso del insertion sort, devuelve el resultado esperado sólo cuando se le permita finalizar todas las iteraciones y para el caso de Tamiza esto no pasa, no significa que el insertion sort no esté funcionando, sucede que no se le está dando el tiempo necesario para finalizar todo el proceso debido a la gran cantidad de registros. Por otro lado, la eficiencia determina que tantos recursos de tiempo y memoria requiere para llegar al resultado correcto, por lo tanto, el hecho de que un algoritmo sea correcto no significa que también sea eficiente. 

Ahora mismo, la plataforma Tamiza incumple con la restricción de la ventana temporal de 4 horas, obligando al centro a trabajar con listas que no están ordenadas en su totalidad, esto no significa que el insertion sort no esté funcionando, sucede que no se le está dando el tiempo necesario para finalizar todo el proceso debido al volumen de registros que se maneja actualmente. Duplicar la velocidad del servidor no soluciona el problema, ya que el verdadero cuello de botella se encuentra en el algoritmo. Insertion sort tiene una complejidad temporal de O(n2), por lo que, al aumentar la cantidad de datos 60 veces, el número de operaciones crece aproximadamente (602=3600) veces. Al implementar un servidor dos veces más rápido únicamente se reduce el tiempo de ejecución a la mitad, pero no modifica el crecimiento cuadrático propio del algoritmo. Es por esto que la solución que ofrecen basada en hardware dejaría de ser insuficiente si la cantidad de registros sigue aumentando en poco tiempo, a lo que propongo que la mejor solución es cambiar de algoritmo, haciendo uso del mergesort y su complejidad temporal de O(n log n).

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

### Notas adicionales

