import requests

url = "https://contrataciondelsectorpublico.gob.es/sindicacion/sindicacion_643/licitacionesPerfilesContratanteCompleto3_202610.zip"
respuesta = requests.get(url, stream=True)
print(respuesta.status_code)
with open("data/raw/licitaciones_202610.zip", "wb") as fichero:
    for trozo in respuesta.iter_content(chunk_size=1024 * 1024):
        fichero.write(trozo)
