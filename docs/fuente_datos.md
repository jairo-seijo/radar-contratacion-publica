# Fuente de datos: Plataforma de Contratación del Sector Público

## 1. Qué es## 1. Qué es

Licitaciones publicadas en los perfiles del contratante de la Plataforma de Contratación del Sector Público, excluyendo los contratos menores. Las publica el Ministerio de Hacienda y hay datos desde 2012.


## 2. Actualización

Se actualiza a diario. El fichero del mes en curso contiene datos hasta el día anterior, así que para analizar un mes entero hay que usar un mes ya cerrado.


## 3. Formato

Ficheros ATOM (XML) con un máximo de 500 entradas cada uno. Están encadenados: cada fichero indica el siguiente en el elemento `link rel="next"`. Se empieza a leer por `licitacionesPerfilesContratanteCompleto3.atom`.


## 4. Descargas

ZIP anual desde 2012 hasta 2026 (el de 2026 es incremental, crece cada mes). Además, 2025 y 2026 tienen un ZIP por cada mes.

- Anual: `https://contrataciondelsectorpublico.gob.es/sindicacion/sindicacion_643/licitacionesPerfilesContratanteCompleto3_AAAA.zip`
- Mensual: `https://contrataciondelsectorpublico.gob.es/sindicacion/sindicacion_643/licitacionesPerfilesContratanteCompleto3_AAAAMM.zip`

Ejemplo: octubre de 2026 es `..._202610.zip`.


## 5. Licencia y condiciones de uso

Datos reutilizables, también con fines comerciales, según las condiciones del Ministerio de Hacienda (Ley 37/2007).

- Citar el origen de los datos, "Origen de los datos: Ministerio de Hacienda", y la fecha de actualización, en el README y en el dashboard.
- No sugerir que el Ministerio participa o apoya el proyecto.
- No distorsionar la información: los indicadores se presentan como señales o avisos, nunca como acusaciones.


## 6. Advertencias para el análisis

- La cobertura no es homogénea entre años: los organismos se han ido añadiendo a la plataforma poco a poco. Las licitaciones de un ayuntamiento anteriores a su entrada no aparecen. Por eso, más licitaciones en un año no significa que se contrate más.
- Una misma licitación aparece una vez por cada modificación. Contar entradas no es contar licitaciones: hay que quedarse con la última versión.
- Hay campos que solo existen en licitaciones actualizadas desde ciertas fechas (por ejemplo, el NIF del órgano desde 2018). En los años antiguos faltarán.
- Hay importe con impuestos y sin impuestos: usar siempre el mismo (sin impuestos).
- Una licitación puede dividirse en lotes, cada uno con su importe. Pendiente decidir si la fila será la licitación o el lote (nivel 2).


## 7. Otros conjuntos y documentación

La página publica seis conjuntos, cada uno con un tipo de contratación distinto. Este proyecto usa el primero.

- Licitaciones en perfiles de la Plataforma (sin contratos menores): el conjunto principal.
- Licitaciones por agregación (desde 2016): las de comunidades con plataforma propia, que envían una copia a la estatal. Traen menos campos.
- Contratos menores (desde 2018): contratos pequeños que se adjudican sin concurso. Se usarán en el nivel 5.
- Encargos a medios propios (desde 2021): trabajos que la administración encarga a sus propias empresas públicas, sin licitar.
- Consultas preliminares de mercado (desde 2022): consultas a empresas antes de preparar una licitación.
- Perfiles de los órganos de contratación (Excel): la lista de organismos con su NIF, tipo de administración y código postal. Útil para `dim_organo` en el nivel 2.
- En un fichero de octubre de 2026 (499 licitaciones) aparecen unas 10 de concellos gallegos y alguna de la Xunta. Pendiente de cuantificar en el paso 1.9

Documentación:
- Documento resumen de los campos (diciembre de 2023; puede no estar actualizado).
- Especificación técnica del formato de sindicación (PDF): se usará en el paso 1.4.
- Página oficial: https://www.hacienda.gob.es/es-ES/GobiernoAbierto/Datos%20Abiertos/Paginas/licitaciones_plataforma_contratacion.aspx


## 8. Dudas pendientes

- ¿Las licitaciones de Galicia (Xunta y concellos) están en este conjunto o llegan por agregación? Comprobar en el paso 1.3 con datos reales.
- Octubre de 2026: ZIP de 184 MB, 124 ficheros, hasta unas 62.000 entradas (no licitaciones).

- ¿Cuántas licitaciones hay en un año? Pendiente de medir.


Preguntas que el proyecto debería responder:

- ¿Qué comunidades, provincias u organismos publican más licitaciones?


