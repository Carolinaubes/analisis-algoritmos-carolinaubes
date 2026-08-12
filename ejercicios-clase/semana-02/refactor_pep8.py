# Código original
def CalcularPromedio(Lista):
    s=0
    for x in Lista:
     s=s+x
    return s/len(Lista)
 
l=[1,2,3,4,5]
print(CalcularPromedio(l))

# Código refactorizado siguiendo PEP8
def calcular_promedio(lista: list) -> float:
    """ Calcula el promedio de los elementos de una lista de números.

    Args:
        lista: Lista de números usados para calcular promedio.

    Returns:
        Float: Promedio de los elementos de la lista.
    """

    suma = 0
    for numero in lista:
        suma = suma + numero

    return suma / len(lista)

def main() -> None:
    lista = [1, 2, 3, 4, 5]
    print(calcular_promedio(lista))

if __name__ == "__main__":
    main()