-- Análisis del nivel 1: preguntas sobre las licitaciones de octubre de 2026
-- Fuente: data/bronze/licitaciones_202610.csv (sin deduplicar: hay versiones repetidas)

-- 1. ¿Cuántas licitaciones hay?
SELECT count(*) AS total_licitaciones FROM 'data/bronze/licitaciones_202610.csv';

-- 2. ¿Qué 10 órganos publican más licitaciones?
SELECT organo_de_contratacion, count (*) AS num_licitaciones
FROM 'data/bronze/licitaciones_202610.csv'
GROUP BY organo_de_contratacion
ORDER BY num_licitaciones DESC
LIMIT 10;