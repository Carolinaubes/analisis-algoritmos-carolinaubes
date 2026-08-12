"""Clasificador de años bisiestos.
 
Complete las funciones siguiendo la especificación de cada docstring.
"""
 
 
def es_bisiesto(anio: int) -> bool:
    """Determina si un año es bisiesto.
 
    Un año es bisiesto si es divisible por 4, excepto los años
    divisibles por 100 que no lo sean también por 400.
 
    Args:
        anio: año a evaluar (número entero).
 
    Returns:
        True si el año es bisiesto, False en caso contrario.
    """
    # TODO: implemente la lógica usando if / elif / else.
    if anio % 4 == 0:
        if anio % 100 == 0:
            if anio % 400 == 0:
                return True
            else:
                return False
        else:
            return True
 
 
def leer_anios() -> list[int]:
    """Solicita al usuario una lista de años separados por comas.
 
    Debe reintentar mientras la entrada no se pueda convertir a enteros
    (use try / except para capturar entradas inválidas).
 
    Returns:
        Lista de años como enteros.
    """
    # TODO: implemente la lectura y validación.

    while True:
        try:
            lista_anios = [int(anio.strip()) for anio in (input("Ingrese años separados por comas: ")).split(",")]
            return lista_anios
        except ValueError:
            print("Entrada inválida. Por favor ingrese números enteros separados por comas")
 
def main() -> None:
    """Punto de entrada del script."""
    # TODO: use leer_anios(), filtre los años bisiestos con una
    # comprensión de listas, e imprima un resumen que incluya al menos
    # la lista de años bisiestos y cuántos hay.

    lista_anios = leer_anios()
    lista_bisiestos = [anio for anio in lista_anios if es_bisiesto(anio) == True]
    cantidad_bisiestos = len(lista_bisiestos)

    print(f"RESUMEN------------\nAños ingresados: {lista_anios}\nAños bisiestos: {lista_bisiestos}\nCantidad de años bisiestos: {cantidad_bisiestos} de {len(lista_anios)}")
 
if __name__ == "__main__":
    main()