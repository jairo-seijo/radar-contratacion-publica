# Diario del proyecto

## 2026-11-07 — Paso 1.4: entender el XML

- Hice: localicé en el XML las rutas de los 6 campos (expediente, objeto, importe, CPV, órgano y adjudicatario) y las documenté en `docs/campos_xml.md`. Decidí usar el importe sin IVA y quedarme con el primer CPV.
- Falló: modifiqué sin querer el fichero `.atom` original al pulsar una tecla con texto seleccionado. Con el autoguardado activado, el cambio se guardó solo (el contador de entradas bajó de 499 a 498).
- Lo resolví: deshice el cambio con Ctrl+Z hasta volver a 499 y desactivé el autoguardado.
- Aprendí: los datos raw no se tocan nunca. En empresas se protegen como solo lectura y se guarda siempre el original para poder reprocesar.

## 2026-11-08 — Paso 1.4: remates (validar rutas, id, updated)

- Hice: instalé la extensión XML de Red Hat y aprendí a ver la ruta de cualquier línea en la barra de arriba. Con ella comprobé la ruta del adjudicatario y localicé el id y la fecha de actualización.
- Falló: al escribir rutas a mano me como letras del final (`ContractFolderI` en vez de `ContractFolderID`, `update` en vez de `updated`). En el código eso no da error: devuelve vacío.
- Lo resolví: copio los nombres con Ctrl+C en vez de teclearlos y compruebo cada ruta con la barra de la extensión.
- Aprendí: con la extensión XML veo la ruta completa haciendo clic en la línea, sin tener que subir de padre en padre a mano.

## 2026-11-12 — Paso 1.5: primer script de lectura

- Fechas: del 2026-11-10 al 2026-11-12
- Hice: escribí `src/parser.py`, que lee un fichero `.atom` con lxml y saca los 6 campos de cada licitación (499 en total) usando las rutas de      `campos_xml.md`. Lo metí todo en una función, `leer_fichero(ruta)`, que devuelve una lista de diccionarios.
- Falló: sobre todo errores de escritura: letras de más o de menos en nombres (`leer_ficheros` en vez de `leer_fichero`) y una línea en el sitio equivocado que cortaba la función en dos. Python no siempre avisa: una ruta mal escrita devuelve `None` sin dar error.
- Lo resolví: leyendo el error por la última línea, comparando con el original y copiando los nombres con Ctrl+C en vez de teclearlos. Comprobando siempre que salen 499 fichas.
- Aprendí: a dejar que las herramientas trabajen por mí: Shift+Alt+F para que Ruff ordene el código y Alt+Z para leer líneas largas sin desplazarme.
- Tiempo: 2 h 10 min

## Paso 1.6 – Campos que faltan

- Fechas: del 2026-11-15 al 2026-11-16
- Tiempo: 3 h 15 min

Qué hice:
- Configuré el parser de lxml para que no siga entidades externas ni salga a internet (protección frente a XXE).
- Añadí al parser el estado de la licitación y el código de resultado, y el namespace `cbc-place-ext`.
- Medí los vacíos de todos los campos: 299 sin adjudicatario, 3 sin CPV, el resto completos.
- Investigué 13 licitaciones adjudicadas o resueltas sin ganador: 11 desiertas y 2 desistimientos, comprobado con la lista oficial de códigos.
- Provoqué a propósito el error de `find(...).text` para ver por qué `findtext` es más seguro.

Decisión: los datos que faltan se quedan como `None`, no se rellenan con un texto inventado.

Lo que más me costó: entender todo en general, porque es todo nuevo para mí.

XXE: un XML de fuera con una trampa (una “entidad”, como un “ver anexo”) que hace que mi programa lea ficheros de mi ordenador o salga a internet. Mi parser no sigue esas entidades.

## Paso 1.7 – Guardar en CSV

Fechas: 2026-11-22
Tiempo: 1 h 20 min

Qué hice: pasé los datos de raw a bronze. Convertí la lista de licitaciones en una tabla con pandas (DataFrame) y la guardé en `data/bronze/licitaciones_202610.csv` con una función nueva, `guardar_csv`. Salen 499 filas y 8 columnas.

Qué me costó: entender cómo encaja todo: qué hace cada línea y por qué va en ese sitio. Me lié al llamar a `guardar_csv`: primero puse `df` y luego `pd.DataFrame(...)`, cuando lo que tenía que darle era la lista (`licitaciones`) y la ruta. También me costó entender por qué algunos datos del CSV llevan comillas.

Qué aprendí:

- `index=False`: el índice es la numeración interna de pandas, no un dato. Si lo guardas, te sobra una columna.
- Si un texto lleva una coma, en el CSV se partiría en dos. Las comillas lo evitan.
- `leer_fichero` lee y entrega la información con `return`. `guardar_csv` lo guarda y listo: no tiene nada que entregar.
- Los datos no se suben a GitHub. El `.gitignore` los deja fuera.
- En bronze los datos van sin limpiar. Quitar saltos de línea y pasar el importe a número lo dejo para el paso 1.9.

## Paso 1.8 – Descarga automática

Fechas: 2026-11-22 a 2026-11-24
Tiempo: 4 h

### Qué hice

- `src/downloader.py` hace todo el mes con un solo comando: descarga el ZIP, comprueba que es un ZIP, lo descomprime, lee los 124 `.atom` con el parser y guarda el CSV en bronze.
- Octubre de 2026: 185 MB de ZIP → 1,7 GB de XML → 61.638 filas → CSV de 16 MB.
- Si el ZIP ya está en `data/raw/`, no lo vuelve a descargar.
- La descarga es idéntica byte a byte a la oficial (comprobado con `sha256sum`).
- El parser pasó a ser solo una "caja de herramientas": el trabajo lo hace el downloader.

### Qué falló y cómo lo resolví

- **`requests.head` → el servidor colgaba** (`Connection reset by peer`). Probé hipótesis de una en una: repetir, la URL en el navegador, el User-Agent, `head` por `get`. Causa: el servidor no acepta `head`. Solución: `get` con `stream=True`.
- **Con un mes que no existe, el servidor responde 200 y manda una página de error HTML.** Lo descubrí provocando el error con `203012`. Solución: comprobar que el `Content-Type` sea `application/zip` y, si no, parar con `raise`.
- **Al importar el parser salía un `499` que nadie pedía.** Había código suelto al final de `parser.py`. Al importar un fichero, Python lo ejecuta entero. Solución: dejar en el parser solo funciones.

### Qué aprendí

1. Cuando algo falla: revisar varias posibilidades, de una en una, empezando por la más fácil de comprobar y cambiando una sola cosa cada vez.
2. Un 200 no garantiza que el dato sea bueno: hay que validar lo que llega.
3. No repetir trabajo hecho: mirar si el fichero ya existe antes de descargarlo.
4. Cada función hace un solo trabajo: así se pueden usar, revisar y probar por separado.
5. DRY: cada dato escrito en un solo sitio (la ruta del ZIP, en `ruta_del_zip`).
6. Un fichero que se importa debe tener solo funciones, sin código suelto.
7. `extend` vacía la caja en la estantería; `append` mete la caja entera.

### Lo que más me costó y lo que más me gustó

- Me costó y a la vez me gustó enlazar el parser con el downloader.
- El primer día me costó entender cómo hacerlo, porque había muchas cosas nuevas a la vez.
- Me gustó ver todo lo que se podrá hacer con esto.

### Conceptos para repasar

`requests.get` y `stream=True` · código de estado · cabeceras (`Content-Type`) · `with open(..., "wb")` · `iter_content` · f-string · `return` y `return valor` · `Path(...).exists()` · `zipfile` y `extractall` · `glob("*.atom")` y `sorted` · `extend` frente a `append` · importar mis propias funciones · prefijos `feat:`, `fix:`, `chore:`, `refactor:`.

### Cómo lo contaría en una entrevista

"Automaticé la ingesta: el downloader descarga el ZIP mensual, valida que sea un ZIP porque la fuente devuelve 200 con páginas de error, evita descargas repetidas y procesa unos 1,7 GB de XML hasta un CSV de unas 62.000 filas. Limitación conocida: hay licitaciones repetidas por versiones, que resolveré en el nivel 2."