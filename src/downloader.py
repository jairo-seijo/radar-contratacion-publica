import zipfile
from pathlib import Path

import requests

from parser import guardar_csv, leer_fichero


def ruta_del_zip(anio_mes):
    return f"data/raw/licitaciones_{anio_mes}.zip"


def descargar_zip(anio_mes):
    ruta = ruta_del_zip(anio_mes)
    if Path(ruta).exists():
        print(f"{ruta} ya existe, no se descarga")
        return
    url = f"https://contrataciondelsectorpublico.gob.es/sindicacion/sindicacion_643/licitacionesPerfilesContratanteCompleto3_{anio_mes}.zip"
    respuesta = requests.get(url, stream=True)
    print(respuesta.status_code)
    if respuesta.headers["Content-Type"] != "application/zip":
        raise ValueError(
            f"La descarga de {anio_mes} no es un ZIP: el mes no existe o la fuente ha fallado"
        )
    with open(ruta, "wb") as fichero:
        for trozo in respuesta.iter_content(chunk_size=1024 * 1024):  # noqa: FURB122
            fichero.write(trozo)


def descomprimir_zip(anio_mes):
    ruta_zip = ruta_del_zip(anio_mes)
    carpeta = f"data/raw/{anio_mes}"
    with zipfile.ZipFile(ruta_zip) as archivo_zip:
        archivo_zip.extractall(carpeta)


def leer_mes(anio_mes):
    carpeta = Path(f"data/raw/{anio_mes}")
    licitaciones = []
    for ruta_atom in sorted(carpeta.glob("*.atom")):
        licitaciones.extend(leer_fichero(ruta_atom))
    return licitaciones


descargar_zip("202610")
descomprimir_zip("202610")
licitaciones = leer_mes("202610")
print(len(licitaciones))
guardar_csv(licitaciones, "data/bronze/licitaciones_202610.csv")
