import algoritmos, datos, time
import matplotlib.pyplot as plt

# Uso de Insertion Sort para medir comparaciones y tiempo de ejecución en diferentes escenarios

tamanos = [100, 200, 400, 800, 1600, 3200, 6400]
tiempos_is = [] # Resultados de tiempos producidos por Insertion Sort
tiempos_ms = [] # Resultados de tiempos producidos por Merge Sort
semilla = 42

for n in tamanos:
    # Escenario A: lista aleatoria

    datos_aleatorios = datos.generar_aleatorio(n, semilla)

    # Toma de tiempo para Insertion Sort (is)
    inicio_is = time.perf_counter()
    _, comparaciones_aleatorio_is = algoritmos.insertion_sort(datos_aleatorios)
    fin_is = time.perf_counter()
    tiempo_aleatorio = fin_is - inicio_is
    tiempos_is.append(tiempo_aleatorio)

    # Toma de tiempo para Merge Sort (ms)
    inicio_ms = time.perf_counter()
    _, comparaciones_aleatorio_ms = algoritmos.merge_sort(datos_aleatorios)
    fin_ms = time.perf_counter()
    tiempo_aleatorio_ms = fin_ms - inicio_ms
    tiempos_ms.append(tiempo_aleatorio_ms)

    print(f"Tamaño: {n}")
    print(f"Escenario A (Aleatorio): \n- InsertionSort: Comparaciones={comparaciones_aleatorio_is}, Tiempo={tiempo_aleatorio:.6f} segundos\n- MergeSort: Comparaciones={comparaciones_aleatorio_ms}, Tiempo={tiempo_aleatorio_ms:.6f} segundos")

# Creación de gráfica: Tiempo vs Tamano entrada
plt.plot(tamanos, tiempos_is, marker="o", label="Insertion Sort")
plt.plot(tamanos, tiempos_ms, marker="o", label="Merge Sort")

plt.title("Tiempo de ejecución - Escenario A")
plt.xlabel("Tamaño de entrada (n)")
plt.ylabel("Tiempo de ejecución (segundos)")
plt.legend()

plt.savefig("parte4_tiempo.png")
plt.show()