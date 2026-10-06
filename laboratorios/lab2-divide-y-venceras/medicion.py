import matplotlib.pyplot as plt
import subarreglo, time, random

tamanos = [10, 50, 100, 500, 1000, 4000, 8000]
tiempos_fb = [] # Resultados de tiempos producidos por Fuerza Bruta
tiempos_sm = [] # Resultados de tiempos producidos por Subarreglo Maximo
semilla = 42

random.seed(semilla)

for n in tamanos:
    valores = [random.randint(-100, 100) for _ in range(n)]

    inicio_fb = time.perf_counter()
    resultado_fb = subarreglo.subarreglo_fuerza_bruta(valores)
    fin_fb = time.perf_counter()
    tiempos_fb.append(fin_fb - inicio_fb)

    inicio_sm = time.perf_counter()
    resultado_sm = subarreglo.subarreglo_maximo(valores, 0, len(valores) - 1)
    fin_sm = time.perf_counter()
    tiempos_sm.append(fin_sm - inicio_sm)

    assert resultado_fb[2] == resultado_sm[2] # Verificacion de que ambos algoritmos producen el mismo resultado

    print(f"Tamaño: {n}")
    print(f"Fuerza bruta: {tiempos_fb[-1]:.6f} s")
    print(f"Divide y vencerás: {tiempos_sm[-1]:.6f} s")
    print(f"Suma: {resultado_fb[2]}\n")

# Creación de gráfica: Tiempo vs Tamano entrada
plt.plot(tamanos, tiempos_fb, marker="o", label="Fuerza Bruta")
plt.plot(tamanos, tiempos_sm, marker="o", label="Divide y Vencerás")

plt.title("Tiempo de ejecución vs tamaño de entrada")
plt.xlabel("Tamaño de entrada (n)")
plt.ylabel("Tiempo de ejecución (segundos)")
plt.legend()

plt.savefig("./laboratorios/lab2-divide-y-venceras/graficas/tiempo_vs_n.png")
plt.show()