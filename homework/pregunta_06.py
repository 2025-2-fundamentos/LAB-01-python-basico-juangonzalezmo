"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from .utilidades import leer_datos

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    datos = leer_datos()
    estadisticas = {}

    for fila in datos:
        cadena_dicc = fila[4]
        pares = cadena_dicc.split(",")
        for par in pares:
            clave, valor = par.split(":")
            valor = int(valor)

            if clave not in estadisticas:
                estadisticas[clave] = {"min": valor, "max": valor}
            else:
                if valor < estadisticas[clave]["min"]:
                    estadisticas[clave]["min"] = valor
                if valor > estadisticas[clave]["max"]:
                    estadisticas[clave]["max"] = valor

    resultado = []
    for clave in sorted(estadisticas.keys()):
        resultado.append(
            (clave, estadisticas[clave]["min"], estadisticas[clave]["max"])
        )

    return resultado