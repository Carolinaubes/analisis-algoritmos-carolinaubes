"""Subarreglo maximo: fuerza bruta y divide y venceras."""
 
 
def subarreglo_fuerza_bruta(valores: list[float]) -> tuple[int, int, float]:
    """Encuentra la mejor racha probando todos los pares de dias (i, j).
 
    Args:
        valores: variacion diaria de caja, una por dia. Tiene al menos
            un elemento.
 
    Returns:
        Una tupla (inicio, fin, suma) con los indices inclusivos del
        tramo de mayor suma y el valor de esa suma.
    """
    # TODO: implemente la solucion en Θ(n²): acumule la suma dentro del
    # ciclo en vez de recalcularla desde cero para cada par.

    mejor_inicio = 0
    mejor_fin = 0
    mejor_suma = valores[0] # Inicializada con el primero de la lista de valores

    for inicio in range(len(valores)):
        suma_actual = 0
        for fin in range(inicio, len(valores)):
            suma_actual += valores[fin]
            if suma_actual > mejor_suma:
                mejor_suma = suma_actual
                mejor_inicio = inicio
                mejor_fin = fin

    return (mejor_inicio, mejor_fin, mejor_suma)

def suma_cruzada(
    valores: list[float], inicio: int, medio: int, fin: int
) -> tuple[int, int, float]:
    """Encuentra el mejor tramo que cruza el punto medio.
 
    Args:
        valores: variacion diaria de caja.
        inicio: indice inicial del rango considerado (inclusive).
        medio: indice del ultimo elemento de la mitad izquierda.
        fin: indice final del rango considerado (inclusive).
 
    Returns:
        Una tupla (inicio, fin, suma) del mejor tramo que incluye al
        menos un elemento de cada mitad.
    """
    # TODO: barrido lineal desde el punto medio hacia cada lado.

    mejor_suma_izq = float("-inf") # Inicializo con - infinito para asegurar q cualquier otro número será mayor
    suma = 0
    mejor_inicio = medio

    # Lado izquierdo: medio a inicio
    for i in range(medio, inicio - 1, -1):
        suma += valores[i]
        if suma > mejor_suma_izq:
            mejor_suma_izq = suma
            mejor_inicio = i

    mejor_suma_der = float("-inf")
    suma = 0
    mejor_fin = medio + 1

    # Lado derecho: medio + 1 a fin
    for j in range(medio + 1, fin + 1):
        suma += valores[j]
        if suma > mejor_suma_der:
            mejor_suma_der = suma
            mejor_fin = j

    return (mejor_inicio, mejor_fin, mejor_suma_izq + mejor_suma_der)
 
def subarreglo_maximo(
    valores: list[float], inicio: int, fin: int
) -> tuple[int, int, float]:
    """Encuentra la mejor racha por divide y venceras.
 
    Args:
        valores: variacion diaria de caja.
        inicio: indice inicial del rango a considerar (inclusive).
        fin: indice final del rango a considerar (inclusive).
 
    Returns:
        Una tupla (inicio, fin, suma) del mejor tramo dentro de
        valores[inicio..fin].
    """
    # TODO: caso base, dos llamadas recursivas, caso cruzado y combinar.

    # Caso base
    if inicio == fin:
        return (inicio, fin, valores[inicio])

    medio = (inicio + fin) // 2

    izquierda = subarreglo_maximo(valores, inicio, medio)
    derecha = subarreglo_maximo(valores, medio + 1, fin)
    cruzada = suma_cruzada(valores, inicio, medio, fin)

    if derecha[2] <= izquierda[2] >= cruzada[2]:
        return izquierda
    elif izquierda[2] <= derecha[2] >= cruzada[2]:
        return derecha
    else:
        return cruzada
