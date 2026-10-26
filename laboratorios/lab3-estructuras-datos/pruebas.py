"""Pruebas de las estructuras de datos de la guia de envios."""

import random

from estructuras import ListaEnlazada, TablaHash


def probar_lista_enlazada() -> None:
    """Verifica las operaciones básicas de la lista enlazada."""
    lista = ListaEnlazada()

    lista.insertar(1234567890, "en bodega")
    lista.insertar(2345678901, "en reparto")
    lista.insertar(3456789012, "entregado")

    assert lista.buscar(1234567890) == "en bodega"
    assert lista.buscar(2345678901) == "en reparto"
    assert lista.buscar(3456789012) == "entregado"
    assert lista.buscar(9999999999) is None

    assert lista.tamano == 3


def probar_tabla_hash() -> None:
    """Verifica búsquedas, colisiones y factor de carga."""
    tabla = TablaHash(7)

    for guia in (10, 24, 17):
        tabla.insertar(guia, "en bodega")

    assert tabla.hash(10) == 3
    assert tabla.hash(24) == 3
    assert tabla.hash(17) == 3

    assert tabla.buscar(10) == "en bodega"
    assert tabla.buscar(24) == "en bodega"
    assert tabla.buscar(17) == "en bodega"
    assert tabla.buscar(99) is None

    assert tabla.casillas[3].tamano == 3
    assert tabla.tamano == 3
    assert tabla.factor_carga() == 3 / 7


def probar_colecciones_aleatorias() -> None:
    """Compara ambas estructuras en veinte colecciones aleatorias."""
    generador = random.Random(42)
    estados = (
        "en bodega",
        "en reparto",
        "entregado",
        "devuelto",
    )

    for _ in range(20):
        lista = ListaEnlazada()
        tabla = TablaHash(101)
        guias = generador.sample(range(1000000000, 9999999999), 50)
        guias_ausentes = generador.sample(
            range(10000000000, 10000001000),
            20,
        )

        for guia in guias:
            estado = generador.choice(estados)
            lista.insertar(guia, estado)
            tabla.insertar(guia, estado)

        for guia in guias:
            assert lista.buscar(guia) == tabla.buscar(guia)
            assert lista.buscar(guia) is not None

        for guia in guias_ausentes:
            assert lista.buscar(guia) is None
            assert tabla.buscar(guia) is None

        assert lista.tamano == tabla.tamano == 50

def main() -> None:
    """Ejecuta todas las pruebas."""
    probar_lista_enlazada()
    probar_tabla_hash()
    probar_colecciones_aleatorias()

if __name__ == "__main__":
    main()