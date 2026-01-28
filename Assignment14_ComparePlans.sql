-- Assignment 14: Compare Execution Plans Before and After Index
-- Run this in MySQL Workbench to see the execution plans

USE meta;

-- ============================================
-- PART 1: BEFORE INDEX (drop index first)
-- ============================================

-- Drop index to show "before" state
DROP INDEX idx_query_assn ON query;

-- Query 1: COUNT(*) - BEFORE index
EXPLAIN SELECT COUNT(*) FROM query;

-- Query 2: IN clause - BEFORE index
EXPLAIN SELECT COUNT(*) FROM query WHERE query_assn IN ('03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14');

-- Query 3: OR clause - BEFORE index
EXPLAIN SELECT COUNT(*) FROM query WHERE query_assn = '03' OR query_assn = '04' OR query_assn = '05' OR query_assn = '06' OR query_assn = '07' OR query_assn = '08' OR query_assn = '09' OR query_assn = '10' OR query_assn = '11' OR query_assn = '12' OR query_assn = '13' OR query_assn = '14';

-- Query 4: LIKE - BEFORE index
EXPLAIN SELECT COUNT(*) FROM query WHERE query_assn LIKE '03' OR query_assn LIKE '04' OR query_assn LIKE '05' OR query_assn LIKE '06' OR query_assn LIKE '07' OR query_assn LIKE '08' OR query_assn LIKE '09' OR query_assn LIKE '10' OR query_assn LIKE '11' OR query_assn LIKE '12' OR query_assn LIKE '13' OR query_assn LIKE '14';

-- Query 5: UNION - BEFORE index
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

-- ============================================
-- PART 2: CREATE INDEX
-- ============================================

CREATE INDEX idx_query_assn ON query (query_assn);

-- ============================================
-- PART 3: AFTER INDEX
-- ============================================

-- Query 1: COUNT(*) - AFTER index
EXPLAIN SELECT COUNT(*) FROM query;

-- Query 2: IN clause - AFTER index
EXPLAIN SELECT COUNT(*) FROM query WHERE query_assn IN ('03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14');

-- Query 3: OR clause - AFTER index
EXPLAIN SELECT COUNT(*) FROM query WHERE query_assn = '03' OR query_assn = '04' OR query_assn = '05' OR query_assn = '06' OR query_assn = '07' OR query_assn = '08' OR query_assn = '09' OR query_assn = '10' OR query_assn = '11' OR query_assn = '12' OR query_assn = '13' OR query_assn = '14';

-- Query 4: LIKE - AFTER index
EXPLAIN SELECT COUNT(*) FROM query WHERE query_assn LIKE '03' OR query_assn LIKE '04' OR query_assn LIKE '05' OR query_assn LIKE '06' OR query_assn LIKE '07' OR query_assn LIKE '08' OR query_assn LIKE '09' OR query_assn LIKE '10' OR query_assn LIKE '11' OR query_assn LIKE '12' OR query_assn LIKE '13' OR query_assn LIKE '14';

-- Query 5: UNION - AFTER index
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
