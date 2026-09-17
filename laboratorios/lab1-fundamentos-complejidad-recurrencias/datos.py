"""Generadores de lotes de registros para los escenarios de Tamiza."""
 
 
import random, math

def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote de n registros en orden aleatorio (escenario A).
 
    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio, para que el
            experimento sea reproducible.
 
    Returns:
        Lista de n indices de riesgo enteros distintos, desordenada.
    """
    # TODO: implemente el escenario A.
    random.seed(semilla)
    registros = list(range(1, n + 1))
    random.shuffle(registros)
    return registros
 
 
def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote casi ordenado: 98% ordenado y 2% al final (escenario B).
 
    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio.
 
    Returns:
        Lista de n indices de riesgo enteros distintos, con el primer
        98% en el orden que el algoritmo produce y el 2% restante
        desordenado al final.
    """
    # TODO: implemente el escenario B.
    random.seed(semilla)
    k = math.floor(n * 0.98) # Obtengo el 98% de los registros ordenados
    registros = list(range(1, n + 1)) # Lista con la cantidad de registros 

    r_ordenados = registros[n - k:][::-1] # Representa el 98% ordenado
    r_desordenados = registros[:n - k] # Representa el 2% 
    random.shuffle(r_desordenados) # Desordeno el 2% de los registros

    casi_ordenado = r_ordenados + r_desordenados # Concateno el 98% ordenado con el 2% desordenado
    
    return casi_ordenado
 
 
def generar_inverso(n: int) -> list[int]:
    """Genera un lote en el orden exactamente contrario (escenario C).
 
    Args:
        n: cantidad de registros del lote.
 
    Returns:
        Lista de n indices de riesgo enteros distintos, en el orden
        inverso al que el algoritmo debe producir.
    """
    # TODO: implemente el escenario C.
    return list(range(1, n + 1))
