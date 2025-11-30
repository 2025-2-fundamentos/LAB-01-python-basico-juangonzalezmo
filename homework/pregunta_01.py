"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from .utilidades import leer_datos

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    datos = leer_datos()
    suma = 0
    for fila in datos:
        suma += int(fila[1])
    return suma


