from random import randint

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo

# Serie de ocho dias de la situación problema 
serie = [-3, 5, -2, 8, -6, 3, 9, -4]
resultado_fuerza_bruta = subarreglo_fuerza_bruta(serie)
resultado_divide_venceras = subarreglo_maximo(serie, 0, len(serie) - 1)

assert resultado_fuerza_bruta[2] == 17
assert resultado_divide_venceras[2] == 17
assert resultado_fuerza_bruta[2] == resultado_divide_venceras[2]

# Serie de un solo elemento 
serie = [6]
resultado_fuerza_bruta = subarreglo_fuerza_bruta(serie)
resultado_divide_venceras = subarreglo_maximo(serie, 0, len(serie) - 1)

assert resultado_fuerza_bruta[2] == 6
assert resultado_divide_venceras[2] == 6
assert resultado_fuerza_bruta[2] == resultado_divide_venceras[2]

# Serie con todos los valores negativos 
serie = [-3, -5, -2, -8, -6, -3, -9, -4]
resultado_fuerza_bruta = subarreglo_fuerza_bruta(serie)
resultado_divide_venceras = subarreglo_maximo(serie, 0, len(serie) - 1)

assert resultado_fuerza_bruta[2] == -2
assert resultado_divide_venceras[2] == -2
assert resultado_fuerza_bruta[2] == resultado_divide_venceras[2]

# Serie con todos los valores positivos
serie = [3, 5, 2, 8, 6, 3, 9, 4]
resultado_fuerza_bruta = subarreglo_fuerza_bruta(serie)
resultado_divide_venceras = subarreglo_maximo(serie, 0, len(serie) - 1)

assert resultado_fuerza_bruta[2] == 40
assert resultado_divide_venceras[2] == 40
assert resultado_fuerza_bruta[2] == resultado_divide_venceras[2]

# Caso donde la mejor racha cruza el punto medio.
serie = [-10, 4, 5, 6, 7, -10]
resultado_fuerza = subarreglo_fuerza_bruta(serie)
resultado_divide = subarreglo_maximo(serie, 0, len(serie) - 1)

assert resultado_fuerza[2] == 22
assert resultado_divide[2] == 22
assert resultado_fuerza[2] == resultado_divide[2]

# Generación de 20 listas aleatorias
for _ in range(20):
    longitud_listas = randint(1, 20)
    serie = [randint(-10, 10) for _ in range(longitud_listas)]

    resultado_fuerza = subarreglo_fuerza_bruta(serie)
    resultado_divide = subarreglo_maximo(serie, 0, len(serie) - 1)

    assert resultado_fuerza[2] == resultado_divide[2] # Solo se valida si ambos son iguales porque no se tiene conocimiento de la suma exacta
