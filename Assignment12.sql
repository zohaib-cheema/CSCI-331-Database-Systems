/* Storage engine, row format, and table options for the whole database */
SHOW TABLE STATUS FROM university;

/* Table physical metadata - Tablespace and file-per-table */
SELECT *
FROM information_schema.INNODB_TABLESPACES
WHERE NAME LIKE 'university%';
