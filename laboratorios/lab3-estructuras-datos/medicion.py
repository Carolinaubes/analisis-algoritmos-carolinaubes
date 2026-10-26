"""Experimentos de rendimiento para ListaEnlazada y TablaHash."""

import random
import time
from pathlib import Path

import matplotlib.pyplot as plt

from estructuras import ListaEnlazada, TablaHash


CANTIDAD_BUSQUEDAS = 200
SEMILLA_FIJA = 42
TAMANO_B = 20_000  # Tamaño fijo para el experimento B


def generar_guias_inexistentes(
    existentes: set[int],
    cantidad: int,
    semilla: int = 7,
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: guias almacenadas en las estructuras.
        cantidad: cuantas guias inexistentes generar.
        semilla: semilla del generador, para reproducir la medicion.

    Returns:
        Una lista con `cantidad` guias que no pertenecen a `existentes`.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []

    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)

    return inexistentes


def es_primo(numero: int) -> bool:
    """Indica si un entero es primo.

    Args:
        numero: entero que se desea comprobar.

    Returns:
        True si el numero es primo; False en caso contrario.
    """
    if numero < 2:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False

    divisor = 3
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 2

    return True


def primo_mas_cercano(objetivo: int) -> int:
    """Obtiene el primo mas cercano a un valor objetivo.

    Args:
        objetivo: valor alrededor del cual buscar el primo.

    Returns:
        El numero primo mas cercano al objetivo.
    """
    inferior = max(2, objetivo)
    superior = max(2, objetivo)

    while not es_primo(inferior):
        inferior -= 1
        if inferior < 2:
            inferior = 2
            break

    while not es_primo(superior):
        superior += 1

    if abs(objetivo - inferior) <= abs(superior - objetivo):
        return inferior
    return superior


def generar_guias_existentes(cantidad: int, semilla: int) -> list[int]:
    """Genera guias unicas de diez digitos de forma reproducible.

    Args:
        cantidad: numero de guias que se deben generar.
        semilla: semilla fija del generador aleatorio.

    Returns:
        Una lista de guias unicas de diez digitos.
    """
    azar = random.Random(semilla)
    return azar.sample(range(10**9, 10**10), cantidad)


def verificar_muestra(
    lista: ListaEnlazada,
    tabla: TablaHash,
    guias: list[int],
) -> None:
    """Comprueba que ambas estructuras coincidan en una muestra existente.

    Args:
        lista: lista enlazada construida con las guias.
        tabla: tabla hash construida con las mismas guias.
        guias: guias existentes que se usaran para la comprobacion.
    """
    for guia in guias[: min(20, len(guias))]:
        estado_lista = lista.buscar(guia)
        estado_tabla = tabla.buscar(guia)
        assert estado_lista is not None
        assert estado_lista == estado_tabla


def medir_busquedas(
    estructura: ListaEnlazada | TablaHash,
    guias: list[int],
) -> float:
    """Calcula el tiempo medio de busqueda para una lista de guias.

    Args:
        estructura: estructura en la que se realizaran las busquedas.
        guias: guias que se van a buscar.

    Returns:
        Tiempo medio por busqueda (en segundos).
    """
    inicio = time.perf_counter()
    for guia in guias:
        estructura.buscar(guia)
    duracion = time.perf_counter() - inicio
    return duracion / len(guias)


def construir_estructuras(
    guias: list[int],
    m: int,
) -> tuple[ListaEnlazada, TablaHash]:
    """Construye ambas estructuras con los mismos datos.

    Args:
        guias: guias que se insertaran.
        m: numero de casillas de la tabla hash.

    Returns:
        La lista enlazada y la tabla hash ya construidas.
    """
    lista = ListaEnlazada()
    tabla = TablaHash(m)

    for guia in guias:
        estado = f"estado_{guia % 4}"
        lista.insertar(guia, estado)
        tabla.insertar(guia, estado)

    return lista, tabla


def experimento_a() -> tuple[list[int], list[float], list[float]]:
    """Mide busquedas fallidas en lista enlazada y tabla hash.

    Returns:
        Los tamaños probados y los tiempos medios de ambas estructuras.
    """
    tamanos = [100, 500, 1_000, 5_000, 20_000, 50_000]
    tiempos_lista: list[float] = []
    tiempos_tabla: list[float] = []

    for n in tamanos:
        guias = generar_guias_existentes(n, SEMILLA_FIJA + n)
        m = primo_mas_cercano(n // 2)
        lista, tabla = construir_estructuras(guias, m)

        verificar_muestra(lista, tabla, guias)
        inexistentes = generar_guias_inexistentes(
            set(guias),
            CANTIDAD_BUSQUEDAS,
            semilla=7,
        )

        tiempo_lista = medir_busquedas(lista, inexistentes)
        tiempo_tabla = medir_busquedas(tabla, inexistentes)
        tiempos_lista.append(tiempo_lista)
        tiempos_tabla.append(tiempo_tabla)

        print(
            f"A: n={n:>6}, m={m:>6}, "
            f"alfa={tabla.factor_carga():.3f}, "
            f"lista={tiempo_lista:.8f} s/busqueda, "
            f"tabla={tiempo_tabla:.8f} s/busqueda"
        )

    # Creacion de grafica: Experimento A - Tiempo de busqueda fallida vs tamaño de entrada

    plt.figure(figsize=(9, 5.5))
    plt.plot(tamanos, tiempos_lista, marker="o", label="Lista enlazada")
    plt.plot(tamanos, tiempos_tabla, marker="s", label="Tabla hash")
    plt.title("Experimento A: búsqueda fallida en lista y tabla hash")
    plt.xlabel("Número de guías (n)")
    plt.ylabel("Tiempo medio por búsqueda (segundos)")
    plt.yscale("log")
    plt.legend()
    plt.grid(True, which="both", alpha=0.3)
    plt.tight_layout()

    ruta_graficas = Path(__file__).resolve().parent / "graficas"
    ruta_graficas.mkdir(exist_ok=True)
    ruta_grafica = ruta_graficas / "lista_vs_tabla.png"
    plt.savefig(ruta_grafica)

    return tamanos, tiempos_lista, tiempos_tabla


def experimento_b() -> tuple[list[float], list[float]]:
    """Mide el tiempo de busqueda fallida para distintos factores de carga.

    Returns:
        Los factores de carga medidos y los tiempos medios por busqueda.
    """
    n = TAMANO_B
    factores_objetivo = [0.5, 1.0, 4.0, 10.0]
    guias = generar_guias_existentes(n, SEMILLA_FIJA + n)
    inexistentes = generar_guias_inexistentes(
        set(guias),
        CANTIDAD_BUSQUEDAS,
        semilla=7,
    )
    lista_referencia = ListaEnlazada()
    for guia in guias:
        lista_referencia.insertar(guia, f"estado_{guia % 4}")

    tiempos: list[float] = []
    factores_reales: list[float] = []

    for factor_objetivo in factores_objetivo:
        m_objetivo = round(n / factor_objetivo)
        m = primo_mas_cercano(m_objetivo)
        _, tabla = construir_estructuras(guias, m)
        verificar_muestra(lista_referencia, tabla, guias)

        for guia in inexistentes[:20]:
            assert tabla.buscar(guia) is None

        tiempo = medir_busquedas(tabla, inexistentes)
        alfa_real = tabla.factor_carga()
        tiempos.append(tiempo)
        factores_reales.append(alfa_real)

        print(
            f"B: n={n:>6}, m={m:>6}, alfa={alfa_real:.3f}, "
            f"tabla={tiempo:.8f} s/busqueda"
        )

    # Creacion de grafica: Experimento B - Tiempo de busqueda fallida vs factor de carga

    plt.figure(figsize=(9, 5.5))
    plt.plot(factores_reales, tiempos, marker="o", label="Tabla hash")
    plt.title("Experimento B: efecto del factor de carga")
    plt.xlabel("Factor de carga (α = n / m)")
    plt.ylabel("Tiempo medio por búsqueda (segundos)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    ruta_graficas = Path(__file__).resolve().parent / "graficas"
    ruta_graficas.mkdir(exist_ok=True)
    ruta_grafica = ruta_graficas / "tiempo_vs_alfa.png"
    plt.savefig(ruta_grafica)

    return factores_reales, tiempos


def main() -> None:
    """Ejecuta ambos experimentos y genera las dos graficas."""
    experimento_a()
    experimento_b()


if __name__ == "__main__":
    main()
