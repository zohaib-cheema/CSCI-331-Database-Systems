DROP TABLE IF EXISTS table_name;

/*[4] Run "SHOW DATABASES" to see all databases available in your MySQL DBMS.*/
SHOW DATABASES;

/*[5] Run "SHOW TABLES" against database "university" to see all tables in the University Database*/
SHOW TABLES;

/*[6] Run "SHOW TABLES" against database "information_schema" to see all tables in that database. You can learn more about the meaning of these tables at */
SELECT TABLE_NAME
FROM information_schema.tables
WHERE TABLE_SCHEMA = 'information_schema';

/*[7] Run "DESC information_schema.tables" to see its columns.*/
DESC information_schema.tables;

/*[8] Run "DESC information_schema.columns" to see its columns*/
DESC information_schema.columns;

/*[9] Run "DESC information_schema.table_constraints" to see its columns*/
DESC information_schema.table_constraints;

/*[10] Create a view v_table_columns that contains each db name, its tables, and their columns, data-types, and other "interesting" columns.Use the rename (AS) feature as appropriate. sort alphabetically by db name, table name, and then ordinal number of column.*/
CREATE OR REPLACE VIEW v_table_columns AS (SELECT table_schema AS data_base, TABLE_NAME AS `table`, COLUMN_NAME AS `column`, ORDINAL_POSITION AS `no`, IS_NULLABLE AS nullable, DATA_TYPE AS data_type, COALESCE(CHARACTER_MAXIMUM_LENGTH,NUMERIC_PRECISION,0) AS size FROM information_schema.columns WHERE table_schema NOT IN ('mysql','sys','information_schema','performance_schema') ORDER BY table_schema, TABLE_NAME, ORDINAL_POSITION);

/*Retrieve all rows from the view table columns*/
SELECT * FROM v_table_columns;

/*[11] Create a view v_udb_datatypes listing all the different data types being used in the university database, using DISTINCT to filter out the duplicates.Sort the results in alphabetical order of data type.*/
CREATE OR REPLACE VIEW v_udb_datatypes AS (SELECT DISTINCT DATA_TYPE FROM v_table_columns WHERE data_base = 'university' ORDER BY DATA_TYPE);

/*Retrieve all rows from the view udb data types*/
SELECT * FROM v_udb_datatypes;

/*[12] Make SELECT FROM v_table_columns a permanent addition to add_analytics() in DBUtil*/
