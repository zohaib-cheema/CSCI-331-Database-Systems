/* Use meta database */
USE meta;

/* Drop index if it exists (will fail if doesn't exist, but try/except handles it) */
DROP INDEX idx_query_assn ON query;

/* Task 2: Five queries to retrieve total number of queries for all assignments (03-14) */
/* Query 1: Everything at once - COUNT(*) without index */
SELECT COUNT(*) FROM query;

/* Query 2: Using IN clause - without index */
SELECT COUNT(*) FROM query WHERE query_assn IN ('03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14');

/* Query 3: Using OR clause - without index */
SELECT COUNT(*) FROM query WHERE query_assn = '03' OR query_assn = '04' OR query_assn = '05' OR query_assn = '06' OR query_assn = '07' OR query_assn = '08' OR query_assn = '09' OR query_assn = '10' OR query_assn = '11' OR query_assn = '12' OR query_assn = '13' OR query_assn = '14';

/* Query 4: Using LIKE - without index */
SELECT COUNT(*) FROM query WHERE query_assn LIKE '03' OR query_assn LIKE '04' OR query_assn LIKE '05' OR query_assn LIKE '06' OR query_assn LIKE '07' OR query_assn LIKE '08' OR query_assn LIKE '09' OR query_assn LIKE '10' OR query_assn LIKE '11' OR query_assn LIKE '12' OR query_assn LIKE '13' OR query_assn LIKE '14';

/* Query 5: Using UNION - without index */
SELECT SUM(cnt) as total FROM (
    SELECT COUNT(*) as cnt FROM query WHERE query_assn = '03'
    UNION ALL
    SELECT COUNT(*) FROM query WHERE query_assn = '04'
    UNION ALL
    SELECT COUNT(*) FROM query WHERE query_assn = '05'
    UNION ALL
    SELECT COUNT(*) FROM query WHERE query_assn = '06'
    UNION ALL
    SELECT COUNT(*) FROM query WHERE query_assn = '07'
    UNION ALL
    SELECT COUNT(*) FROM query WHERE query_assn = '08'
    UNION ALL
    SELECT COUNT(*) FROM query WHERE query_assn = '09'
    UNION ALL
    SELECT COUNT(*) FROM query WHERE query_assn = '10'
    UNION ALL
    SELECT COUNT(*) FROM query WHERE query_assn = '11'
    UNION ALL
    SELECT COUNT(*) FROM query WHERE query_assn = '12'
    UNION ALL
    SELECT COUNT(*) FROM query WHERE query_assn = '13'
    UNION ALL
    SELECT COUNT(*) FROM query WHERE query_assn = '14'
) AS subquery;

/* Task 5: Create index on query_assn column */
CREATE INDEX idx_query_assn ON query (query_assn);

/* Task 7: Re-execute the five queries with index */
/* Query 1: Everything at once - COUNT(*) with index */
SELECT COUNT(*) FROM query;

/* Query 2: Using IN clause - with index */
SELECT COUNT(*) FROM query WHERE query_assn IN ('03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14');

/* Query 3: Using OR clause - with index */
SELECT COUNT(*) FROM query WHERE query_assn = '03' OR query_assn = '04' OR query_assn = '05' OR query_assn = '06' OR query_assn = '07' OR query_assn = '08' OR query_assn = '09' OR query_assn = '10' OR query_assn = '11' OR query_assn = '12' OR query_assn = '13' OR query_assn = '14';

/* Query 4: Using LIKE - with index */
SELECT COUNT(*) FROM query WHERE query_assn LIKE '03' OR query_assn LIKE '04' OR query_assn LIKE '05' OR query_assn LIKE '06' OR query_assn LIKE '07' OR query_assn LIKE '08' OR query_assn LIKE '09' OR query_assn LIKE '10' OR query_assn LIKE '11' OR query_assn LIKE '12' OR query_assn LIKE '13' OR query_assn LIKE '14';

/* Query 5: Using UNION - with index */
SELECT SUM(cnt) as total FROM (
    SELECT COUNT(*) as cnt FROM query WHERE query_assn = '03'
    UNION ALL
    SELECT COUNT(*) FROM query WHERE query_assn = '04'
    UNION ALL
    SELECT COUNT(*) FROM query WHERE query_assn = '05'
    UNION ALL
    SELECT COUNT(*) FROM query WHERE query_assn = '06'
    UNION ALL
    SELECT COUNT(*) FROM query WHERE query_assn = '07'
    UNION ALL
    SELECT COUNT(*) FROM query WHERE query_assn = '08'
    UNION ALL
    SELECT COUNT(*) FROM query WHERE query_assn = '09'
    UNION ALL
    SELECT COUNT(*) FROM query WHERE query_assn = '10'
    UNION ALL
    SELECT COUNT(*) FROM query WHERE query_assn = '11'
    UNION ALL
    SELECT COUNT(*) FROM query WHERE query_assn = '12'
    UNION ALL
    SELECT COUNT(*) FROM query WHERE query_assn = '13'
    UNION ALL
    SELECT COUNT(*) FROM query WHERE query_assn = '14'
) AS subquery;

/* Task 8: Compare execution plans - BEFORE index (drop index first to show before state) */
/* Drop index to demonstrate before state */
DROP INDEX idx_query_assn ON query;

/* EXPLAIN Query 1: COUNT(*) - BEFORE index */
EXPLAIN SELECT COUNT(*) FROM query;

/* EXPLAIN Query 2: IN clause - BEFORE index */
EXPLAIN SELECT COUNT(*) FROM query WHERE query_assn IN ('03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14');

/* EXPLAIN Query 3: OR clause - BEFORE index */
EXPLAIN SELECT COUNT(*) FROM query WHERE query_assn = '03' OR query_assn = '04' OR query_assn = '05' OR query_assn = '06' OR query_assn = '07' OR query_assn = '08' OR query_assn = '09' OR query_assn = '10' OR query_assn = '11' OR query_assn = '12' OR query_assn = '13' OR query_assn = '14';

/* EXPLAIN Query 4: LIKE - BEFORE index */
EXPLAIN SELECT COUNT(*) FROM query WHERE query_assn LIKE '03' OR query_assn LIKE '04' OR query_assn LIKE '05' OR query_assn LIKE '06' OR query_assn LIKE '07' OR query_assn LIKE '08' OR query_assn LIKE '09' OR query_assn LIKE '10' OR query_assn LIKE '11' OR query_assn LIKE '12' OR query_assn LIKE '13' OR query_assn LIKE '14';

/* EXPLAIN Query 5: UNION - BEFORE index */
EXPLAIN SELECT SUM(cnt) as total FROM (
    SELECT COUNT(*) as cnt FROM query WHERE query_assn = '03'
    UNION ALL
    SELECT COUNT(*) FROM query WHERE query_assn = '04'
    UNION ALL
    SELECT COUNT(*) FROM query WHERE query_assn = '05'
    UNION ALL
    SELECT COUNT(*) FROM query WHERE query_assn = '06'
    UNION ALL
    SELECT COUNT(*) FROM query WHERE query_assn = '07'
    UNION ALL
    SELECT COUNT(*) FROM query WHERE query_assn = '08'
    UNION ALL
    SELECT COUNT(*) FROM query WHERE query_assn = '09'
    UNION ALL
    SELECT COUNT(*) FROM query WHERE query_assn = '10'
    UNION ALL
    SELECT COUNT(*) FROM query WHERE query_assn = '11'
    UNION ALL
    SELECT COUNT(*) FROM query WHERE query_assn = '12'
    UNION ALL
    SELECT COUNT(*) FROM query WHERE query_assn = '13'
    UNION ALL
    SELECT COUNT(*) FROM query WHERE query_assn = '14'
) AS subquery;

/* Re-create index for AFTER comparison */
CREATE INDEX idx_query_assn ON query (query_assn);

/* EXPLAIN Query 1: COUNT(*) - AFTER index */
EXPLAIN SELECT COUNT(*) FROM query;

/* EXPLAIN Query 2: IN clause - AFTER index */
EXPLAIN SELECT COUNT(*) FROM query WHERE query_assn IN ('03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14');

/* EXPLAIN Query 3: OR clause - AFTER index */
EXPLAIN SELECT COUNT(*) FROM query WHERE query_assn = '03' OR query_assn = '04' OR query_assn = '05' OR query_assn = '06' OR query_assn = '07' OR query_assn = '08' OR query_assn = '09' OR query_assn = '10' OR query_assn = '11' OR query_assn = '12' OR query_assn = '13' OR query_assn = '14';

/* EXPLAIN Query 4: LIKE - AFTER index */
EXPLAIN SELECT COUNT(*) FROM query WHERE query_assn LIKE '03' OR query_assn LIKE '04' OR query_assn LIKE '05' OR query_assn LIKE '06' OR query_assn LIKE '07' OR query_assn LIKE '08' OR query_assn LIKE '09' OR query_assn LIKE '10' OR query_assn LIKE '11' OR query_assn LIKE '12' OR query_assn LIKE '13' OR query_assn LIKE '14';

/* EXPLAIN Query 5: UNION - AFTER index */
EXPLAIN SELECT SUM(cnt) as total FROM (
    SELECT COUNT(*) as cnt FROM query WHERE query_assn = '03'
    UNION ALL
    SELECT COUNT(*) FROM query WHERE query_assn = '04'
    UNION ALL
    SELECT COUNT(*) FROM query WHERE query_assn = '05'
    UNION ALL
    SELECT COUNT(*) FROM query WHERE query_assn = '06'
    UNION ALL
    SELECT COUNT(*) FROM query WHERE query_assn = '07'
    UNION ALL
    SELECT COUNT(*) FROM query WHERE query_assn = '08'
    UNION ALL
    SELECT COUNT(*) FROM query WHERE query_assn = '09'
    UNION ALL
    SELECT COUNT(*) FROM query WHERE query_assn = '10'
    UNION ALL
    SELECT COUNT(*) FROM query WHERE query_assn = '11'
    UNION ALL
    SELECT COUNT(*) FROM query WHERE query_assn = '12'
    UNION ALL
    SELECT COUNT(*) FROM query WHERE query_assn = '13'
    UNION ALL
    SELECT COUNT(*) FROM query WHERE query_assn = '14'
) AS subquery;
