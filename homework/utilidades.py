RUTA_ARCHIVO = "files/input/data.csv"

def leer_datos():
    """
    Lee el archivo de datos y devuelve una lista de filas,
    donde cada fila es una lista con las 5 columnas.
    """
    filas = []
    with open(RUTA_ARCHIVO, encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea:
                partes = linea.split("\t")
                filas.append(partes)
    return filas
