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