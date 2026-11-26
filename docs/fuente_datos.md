# Fuente de datos: Plataforma de Contratación del Sector Público

## 1. Qué es

Licitaciones publicadas en los perfiles del contratante de la Plataforma de Contratación del Sector Público, excluyendo los contratos menores. Las publica el Ministerio de Hacienda y hay datos desde 2012.


## 2. Actualización

Se actualiza a diario. El fichero del mes en curso contiene datos hasta el día anterior, así que para analizar un mes entero hay que usar un mes ya cerrado.


## 3. Formato

Ficheros ATOM (XML) con un máximo de 500 entradas cada uno. Están encadenados: cada fichero indica el siguiente en el elemento `link rel="next"`. Se empieza a leer por `licitacionesPerfilesContratanteCompleto3.atom`.

Lo observado en octubre de 2026 (paso 1.3):

- La cadena va de lo más nuevo a lo más antiguo.
- El fichero sin fecha (`...Completo3.atom`) es la puerta de entrada; los demás se llaman `...Completo3_AAAAMMDD_HHMMSS[_N].atom`.
- Cada `<entry>` tiene un `<id>` que parece repetirse en todas sus versiones (comprobarlo en el paso 2.4).


## 4. Descargas

ZIP anual desde 2012 hasta 2026 (el de 2026 es incremental, crece cada mes). Además, 2025 y 2026 tienen un ZIP por cada mes.

- Anual: `https://contrataciondelsectorpublico.gob.es/sindicacion/sindicacion_643/licitacionesPerfilesContratanteCompleto3_AAAA.zip`
- Mensual: `https://contrataciondelsectorpublico.gob.es/sindicacion/sindicacion_643/licitacionesPerfilesContratanteCompleto3_AAAAMM.zip`

Ejemplo: octubre de 2026 es `..._202610.zip`.

Volumen medido (octubre de 2026):

- ZIP de 185 MB; 124 ficheros `.atom` de 14–16 MB; unos 1,7 GB descomprimido.
- Cada fichero trae como máximo 500 entradas; el inicial (sin fecha), 279.
- En total, 61.638 entradas. No son licitaciones distintas: cada versión de una licitación es una entrada.


## 5. Licencia y condiciones de uso

Datos reutilizables, también con fines comerciales, según las condiciones del Ministerio de Hacienda (Ley 37/2007).

- Citar el origen de los datos, "Origen de los datos: Ministerio de Hacienda", y la fecha de actualización, en el README y en el dashboard.
- No sugerir que el Ministerio participa o apoya el proyecto.
- No distorsionar la información: los indicadores se presentan como señales o avisos, nunca como acusaciones.


## 6. Advertencias para el análisis

- La cobertura no es homogénea entre años: los organismos se han ido añadiendo a la plataforma poco a poco. Las licitaciones de un ayuntamiento anteriores a su entrada no aparecen. (Según entiendo; pendiente de verificar.) Por eso, más licitaciones en un año no significa que se contrate más.
- Una misma licitación aparece una vez por cada modificación. Contar entradas no es contar licitaciones: hay que quedarse con la última versión.
- Hay campos que solo existen en licitaciones actualizadas desde ciertas fechas (por ejemplo, el NIF del órgano desde 2018). En los años antiguos faltarán.
- Hay importe con impuestos y sin impuestos: usar siempre el mismo (sin impuestos).
- Una licitación puede dividirse en lotes, cada uno con su importe. Pendiente decidir si la fila será la licitación o el lote (nivel 2).

## 7. Otros conjuntos y documentación

La página publica seis conjuntos, cada uno con un tipo de contratación distinto. Este proyecto usa el primero.

- Licitaciones en perfiles de la Plataforma (sin contratos menores): el conjunto principal.
- Licitaciones por agregación (desde 2016): las de comunidades con plataforma propia, que envían una copia a la estatal. Traen menos campos. (Según entiendo; pendiente de verificar.)
- Contratos menores (desde 2018): contratos pequeños que se adjudican sin concurso. Se usarán en el nivel 5.
- Encargos a medios propios (desde 2021): trabajos que la administración encarga a sus propias empresas públicas, sin licitar.
- Consultas preliminares de mercado (desde 2022): consultas a empresas antes de preparar una licitación.
- Perfiles de los órganos de contratación (Excel): la lista de organismos con su NIF, tipo de administración y código postal. Útil para `dim_organo` en el nivel 2.

Documentación:
- Documento resumen de los campos (diciembre de 2023; puede no estar actualizado).
- Especificación técnica del formato de sindicación (PDF): se usó en el paso 1.4.
- Página oficial: https://www.hacienda.gob.es/es-ES/GobiernoAbierto/Datos%20Abiertos/Paginas/licitaciones_plataforma_contratacion.aspx


## 8. Dudas pendientes

- Galicia: en un fichero de octubre de 2026 aparecen unas 10 licitaciones de concellos y alguna de la Xunta, así que al menos una parte está en este conjunto. Falta cuantificarlo en el paso 1.9 y saber si el resto llega por agregación.
- ¿Cuántas licitaciones hay en un año? Pendiente de medir.

Preguntas que el proyecto debería responder:

- ¿Qué comunidades, provincias u organismos publican más licitaciones?


## 9. Descarga con código (comprobado el 22-nov-2026)

- URL del ZIP mensual: la del apartado 4, con el mes siempre en dos cifras (`09`, no `9`).
- El servidor no acepta peticiones `HEAD`: corta la conexión. Hay que usar `GET` (con `stream=True` para no cargarlo entero en memoria).
- No envía `Content-Length` (usa `Transfer-Encoding: chunked`), así que no se sabe el tamaño antes de descargar.
- Envía `Last-Modified` (el ZIP de octubre se generó el 1-nov-2026 a las 05:00 GMT) y `ETag`: servirán para saber si el fichero cambió sin descargarlo (nivel 4).
- Tiempo de descarga de octubre de 2026 (185 MB): 27 min con el navegador (1.3) y unos 3 min con el script (22-nov, 23:30). Una sola medición de cada.
- Si el fichero pedido no existe, el servidor responde **200** con una página HTML de error (`Content-Type: text/html; charset=UTF-8`) y un mensaje engañoso ("Su certificado no está autorizado…"). No da un 404. Por eso el downloader comprueba que `Content-Type` sea `application/zip` antes de guardar (comprobado el 23-nov-2026 pidiendo `203012`).


