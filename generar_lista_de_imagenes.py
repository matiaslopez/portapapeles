
from pathlib import Path
import re

def generar_lista_de_imagenes(carpeta):
    '''
    Genera una lista de diccionarios con información de las imágenes en la carpeta dada.
    Cada diccionario contiene:
    - nombre: el nombre del archivo
    - ruta: la ruta absoluta del archivo
    - fecha: la fecha extraída del nombre del archivo
    - hora: la hora extraída del nombre del archivo
    - lugar: el lugar extraído del nombre del archivo

    El formato esperado del nombre del archivo es: "WhatsApp Image YYYY-MM-DD at HH.MM.SS_LLL.jpeg"
    Donde:
    - YYYY-MM-DD es la fecha
    - HH.MM.SS es la hora
    - LLL es el lugar (tres letras mayúsculas)
    '''
    lista_de_imagenes = []
    curr_path = Path(carpeta)

    for archivo in curr_path.glob("*.jpeg"):
        current_file = {}

        current_file["nombre"] = archivo.name
        current_file["ruta"] = archivo.resolve()

        fecha = re.search(r'\d{4}-\d{2}-\d{2}', archivo.name)
        current_file["fecha"] = fecha.group() if fecha else None

        hora = re.search(r'\d{2}\.\d{2}\.\d{2}', archivo.name)
        current_file["hora"] = hora.group() if hora else None

        lugar = re.search(r'[A-Z]{3}', archivo.name)
        current_file["lugar"] = lugar.group() if lugar else None

        lista_de_imagenes.append(current_file)

    return lista_de_imagenes