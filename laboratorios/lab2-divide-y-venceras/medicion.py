import random
import time
from pathlib import Path

import matplotlib.pyplot as plt

import subarreglo


tamanos = [10, 50, 100, 500, 1000, 4000, 8000]
tiempos_fb = []  # Tiempos de Fuerza Bruta
tiempos_sm = []  # Tiempos de Subarreglo Maximo
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

    # Validar que ambos algoritmos producen el mismo resultado
    assert resultado_fb[2] == resultado_sm[2]

    print(f"Tamaño: {n}")
    print(f"Fuerza bruta: {tiempos_fb[-1]:.6f} s")
    print(f"Divide y vencerás: {tiempos_sm[-1]:.6f} s")
    print(f"Suma: {resultado_fb[2]}\n")

# Creacion de grafica: Tiempo vs Tamano entrada
plt.plot(tamanos, tiempos_fb, marker="o", label="Fuerza Bruta")
plt.plot(tamanos, tiempos_sm, marker="o", label="Divide y Vencerás")

plt.title("Tiempo de ejecución vs tamaño de entrada")
plt.xlabel("Tamaño de entrada (n)")
plt.ylabel("Tiempo de ejecución (segundos)")
plt.legend()
plt.grid(True)
plt.tight_layout()

ruta_graficas = Path(__file__).resolve().parent / "graficas"
ruta_graficas.mkdir(exist_ok=True)

ruta_grafica = ruta_graficas / "tiempo_vs_n.png"

plt.savefig(ruta_grafica)
plt.show()