# Curso análisis de algoritmos 
## Estudiante: Carolina Uribe Builes


## Propósito carpetas y archivos  

* medicion.py: Toma de tiempos de ejecución de Fuerza Bruta y Subarreglo Máximo y generación de gráficas en base a la comparación de estos resultados.
* pruebas.py: Lógica para probar el funcionamiento de los métodos definidos en subarreglo.py por medio de diferentes casos.
* subarreglo.py: Implementación de los algoritmos de Fuerza Bruta y Subarreglo Máximo
* graficas/: Carpeta que almacena las gráficas generadas en el laboratorio.

## Intrucciones para reproducir el experimento 
> Las siguientes instrucciones corresponden al sistema operativo **Windows**.

Para reproducir el entorno y ejecutar los experiemntos, siga los siguientes pasos:
1. Abra una terminal dentro de la carpeta nombrada 'lab2-divide-y-venceras'.
2. Cree el entorno virtual
```bash
    -  python -m venv venv
    -  venv\Scripts\activate
```
3. Active el entorno virtual:
```bash
    -  venv\Scripts\activate
```
4. Instale las dependencias contenidas en el archivo requirements.txt:
```bash
    -  pip install -r requirements.txt
```
5. Ejecute el archivo pruebas.py para verificar el funcionamiento de los métodos:
```bash
    -  python pruebas.py
```
6. Ejecute el archivo medicion.py para realizar las mediciones de tiempo y generar la gráfica:
```bash
    -  python medicion.py
```

La gráfica generada se almacenará en la carpeta **graficas/**

## Parte 1 - Verificación de soluciones y casos cubiertos
> Acceda al código de [subarreglo.py](./subarreglo.py) y [pruebas.py](./pruebas.py)

Para verificar las soluciones obtenidas por ambos métodos se resolvió cada serie calculando manualmente la suma máxima esperada, simulando el funcionamiento del método de fuerza bruta y de divide y vencerás. Lo anterior fue fundamental para poder determinar los valores esperados y así establecer si cada “assert” debía fallar o cumplirse.

Para este punto se decidió trabajar con los casos mínimos planteados por el maestro:
- Serie de ocho días de la situación problema.
- Serie de un solo elemento.
- Serie con todos los valores negativos.
- Serie con todos los valores positivos.
- Caso donde la mejor racha cruza el punto medio.
- 20 listas aleatorias.


## Parte 2 - Gráfica y medición
> Acceda al código de [medicion.py](./medicion.py)

![Tiempo de ejecución vs tamaño de entrada](./graficas/tiempo_vs_n.png)

Para realizar las mediciones se utilizó un ciclo for que permitió la generación de las siete series correspondientes a los siete tamaños de entrada definidos en el archivo de mediciones. Para cada tamaño se tomó un tiempo inicial y un tiempo final utilizando time.perf_counter(), con el propósito de medir el tiempo de ejecución de cada uno de los dos métodos (Fuerza Bruta y Subarreglo Máximo). 

No se repitió cada medición varias veces ni se calcularon promedios para los tiempos obtenidos. Lo que si fue ejecutado varias veces fue el programa, con el fin de comprobar que la generación de las series, la ejecución de los métodos y la generación de la gráfica estuvieran funcionando correctamente.


## Parte 3 - Respuestas análisis
1. Recurrencia:
2. Lo medido contra lo esperado:
3. Tamaños pequeños:
4. ¿Cúando conviene dividir?:
5. Concepto para la gerente:

