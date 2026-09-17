"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1."""
 

def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.
 
    No modifica la lista recibida: trabaja sobre una copia.
 
    Args:
        datos: lista de indices de riesgo a ordenar.
 
    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    # TODO: implemente el algoritmo contando cada comparacion
    # entre dos elementos de la lista.

    datos_copy = datos.copy()
    contador_comparaciones = 0  # contador de comparaciones

    # Recorre desde el segundo elemento (indice 1) hasta el final
    for i in range(1, len(datos_copy)):
        clave = datos_copy[i] # elemento que se va a insertar
        j = i - 1 # ultimo indice de la parte ya ordenada

        while j >= 0:
            contador_comparaciones += 1
            if datos_copy[j] < clave:
                datos_copy[j + 1] = datos_copy[j]
                j -= 1
            else:
                break
 
        datos_copy[j + 1] = clave # inserta 'clave' en su lugar correcto
    return (datos_copy, contador_comparaciones)
