import requests

url = "https://contrataciondelsectorpublico.gob.es/sindicacion/sindicacion_643/licitacionesPerfilesContratanteCompleto3_202610.zip"
respuesta = requests.get(url, stream=True)
print(respuesta.status_code)
if respuesta.headers["Content-Type"] != "application/zip":
    raise ValueError("La descarga no es un ZIP: el mes no existe o la fuente ha fallado")
with open("data/raw/licitaciones_202610.zip", "wb") as fichero:
    for trozo in respuesta.iter_content(chunk_size=1024 * 1024):  # noqa: FURB122
        fichero.write(trozo)
