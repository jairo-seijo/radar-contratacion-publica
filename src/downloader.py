from pathlib import Path

import requests


def descargar_zip(anio_mes):
    ruta = f"data/raw/licitaciones_{anio_mes}.zip"
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


descargar_zip("202610")
