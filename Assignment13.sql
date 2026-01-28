/* Drop schema sales */
DROP SCHEMA IF EXISTS sales;

/* Create schema sales */
CREATE SCHEMA sales;

/* Make it the default */
USE sales;

/* Drop table sale */
DROP TABLE IF EXISTS sale;

/* Create table sale */
CREATE TABLE sale (
    product_name VARCHAR(100),
    store_location VARCHAR(50),
    num_sales INT
);

/* Insert data into table sale */
INSERT INTO sale (product_name, store_location, num_sales) VALUES
('Chair', 'North', 55),
('Desk', 'Central', 120),
('Couch', 'Central', 78),
('Chair', 'South', 23),
('Chair', 'South', 10),
('Chair', 'North', 98),
('Desk', 'West', 61),
('Couch', 'North', 180),
('Chair', 'South', 14),
('Desk', 'North', 45),
('Chair', 'North', 87),
('Chair', 'Central', 34),
('Desk', 'South', 42),
('Couch', 'West', 58),
('Couch', 'Central', 27),
('Chair', 'South', 91),
('Chair', 'West', 82),
('Chair', 'North', 37),
('Desk', 'North', 68),
('Couch', 'Central', 54),
('Chair', 'South', 81),
('Desk', 'North', 25),
('Chair', 'North', 46),
('Chair', 'Central', 121),
('Desk', 'South', 85),
('Couch', 'North', 43),
('Desk', 'West', 10),
('Chair', 'North', 5),
('Chair', 'Central', 16),
('Desk', 'South', 9),
('Couch', 'West', 22),
('Couch', 'Central', 59),
('Chair', 'South', 76),
('Chair', 'West', 48),
('Chair', 'North', 19),
('Desk', 'North', 3),
('Couch', 'West', 63),
('Chair', 'South', 81),
('Desk', 'North', 85),
('Chair', 'North', 90),
('Chair', 'Central', 47),
('Desk', 'West', 63),
('Couch', 'North', 28);

/* Task 3: Write a query to retrieve all rows from the sale table */
SELECT * FROM sale;

/* Task 4: Write a query to retrieve all product names from the sale table */
SELECT DISTINCT product_name FROM sale;

/* Task 5: Write a query to retrieve all product names and sum from the sale table */
SELECT product_name, SUM(num_sales) FROM sale GROUP BY product_name;

/* Task 6: Write a query to keep track of all sales in location "north" as a separate column */
SELECT product_name, SUM(CASE WHEN store_location = 'North' THEN num_sales ELSE 0 END) AS north FROM sale GROUP BY product_name;

/* Task 7: Modify the query to include a group by clause on the product_name */
SELECT product_name, SUM(CASE WHEN store_location = 'North' THEN num_sales ELSE 0 END) AS north FROM sale GROUP BY product_name;

/* Task 8: Modify the query to cover all four locations */
SELECT product_name, 
    SUM(CASE WHEN store_location = 'North' THEN num_sales ELSE 0 END) AS north,
    SUM(CASE WHEN store_location = 'Central' THEN num_sales ELSE 0 END) AS central,
    SUM(CASE WHEN store_location = 'South' THEN num_sales ELSE 0 END) AS south,
    SUM(CASE WHEN store_location = 'West' THEN num_sales ELSE 0 END) AS west,
    SUM(CASE WHEN store_location = 'East' THEN num_sales ELSE 0 END) AS east
FROM sale GROUP BY product_name;

/* Task 8 with total column */
SELECT product_name, 
    SUM(CASE WHEN store_location = 'North' THEN num_sales ELSE 0 END) AS north,
    SUM(CASE WHEN store_location = 'Central' THEN num_sales ELSE 0 END) AS central,
    SUM(CASE WHEN store_location = 'South' THEN num_sales ELSE 0 END) AS south,
    SUM(CASE WHEN store_location = 'West' THEN num_sales ELSE 0 END) AS west,
    SUM(CASE WHEN store_location = 'East' THEN num_sales ELSE 0 END) AS east,
    SUM(CASE WHEN store_location IS NOT NULL THEN num_sales ELSE 0 END) AS total
FROM sale GROUP BY product_name;

/* Task 9: Consider this hypothetical query to do group concatenation */
/* SET @sql = NULL;
SELECT GROUP_CONCAT(logic) INTO @sql FROM your_table;
SET @sql = CONCAT('select…', @sql, 'from…');
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt; */

/* Task 10: Consider this actual query to do group concatenation */
/* Note: This query uses PREPARE statement which may not work in DBUtil due to multiple semicolons */
/* The PREPARE statement should be run manually in MySQL Workbench if needed */
/* SET @sql = NULL;
SELECT GROUP_CONCAT(DISTINCT CONCAT(
    'SUM(',
    'CASE WHEN store_location = "', store_location, '" THEN num_sales ELSE 0 END)',
    ' AS ', store_location)
) INTO @sql
FROM sale;
SET @sql = CONCAT('SELECT product_name, ', @sql, ' FROM sale GROUP BY product_name');
SELECT @sql;
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt; */
