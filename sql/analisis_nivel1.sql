-- Análisis del nivel 1: preguntas sobre las licitaciones de octubre de 2026
-- Fuente: data/bronze/licitaciones_202610.csv (sin deduplicar: hay versiones repetidas)

-- 1. ¿Cuántas licitaciones hay?
SELECT count(*) AS total_licitaciones FROM 'data/bronze/licitaciones_202610.csv';

-- 2. ¿Qué 10 órganos publican más licitaciones?
SELECT organo_de_contratacion, count(*) AS num_licitaciones
FROM 'data/bronze/licitaciones_202610.csv'
GROUP BY organo_de_contratacion
ORDER BY num_licitaciones DESC
LIMIT 10;

-- 3. Galicia: ¿cuántas licitaciones publican los concellos?
-- OJO: buscar 'concello' limita a esa palabra y deja fuera los sinónimos
-- (p. ej. "Ayuntamiento de Vigo", 127 licitaciones, no aparece).
-- Solución en el nivel 2: filtrar por provincia del órgano.
SELECT organo_de_contratacion AS concellos_de_galicia, count(*) AS num_licitaciones
FROM 'data/bronze/licitaciones_202610.csv'
WHERE organo_de_contratacion  ILIKE '%concello%'
GROUP BY organo_de_contratacion
ORDER BY num_licitaciones DESC
LIMIT 10;
-- 4. ¿Qué 10 empresas ganan más adjudicaciones?
SELECT adjudicatario AS empresa, count(*) AS num_adjudicaciones
FROM 'data/bronze/licitaciones_202610.csv'
WHERE adjudicatario IS NOT NULL
GROUP BY adjudicatario
ORDER BY num_adjudicaciones DESC
LIMIT 10;