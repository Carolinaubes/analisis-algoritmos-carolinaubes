import algoritmos, datos, time

# Uso de Insertion Sort para medir comparaciones y tiempo de ejecución en diferentes escenarios

tamanos = [100, 200, 400, 800, 1600, 3200, 6400]
semilla = 42

for n in tamanos:
    # Escenario A: lista aleatoria
    datos_aleatorios = datos.generar_aleatorio(n, semilla)
    inicio = time.perf_counter()
    _, comparaciones_aleatorio = algoritmos.insertion_sort(datos_aleatorios)
    fin = time.perf_counter()
    tiempo_aleatorio = fin - inicio

    # Escenario B: lista casi ordenada
    datos_casi_ordenados = datos.generar_casi_ordenado(n, semilla)
    inicio = time.perf_counter()
    _, comparaciones_casi_ordenado = algoritmos.insertion_sort(datos_casi_ordenados)
    fin = time.perf_counter()
    tiempo_casi_ordenado = fin - inicio

    # Escenario C: lista inversa
    datos_inversos = datos.generar_inverso(n)
    inicio = time.perf_counter()
    _, comparaciones_inverso = algoritmos.insertion_sort(datos_inversos)
    fin = time.perf_counter()
    tiempo_inverso = fin - inicio

    print(f"Tamaño: {n}")
    print(f"Escenario A (Aleatorio): Comparaciones={comparaciones_aleatorio}, Tiempo={tiempo_aleatorio:.6f} segundos")
    print(f"Escenario B (Casi Ordenado): Comparaciones={comparaciones_casi_ordenado}, Tiempo={tiempo_casi_ordenado:.6f} segundos")
    print(f"Escenario C (Inverso): Comparaciones={comparaciones_inverso}, Tiempo={tiempo_inverso:.6f} segundos\n")
