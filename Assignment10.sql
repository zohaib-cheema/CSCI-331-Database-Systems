/*Dummy select for testing*/
SELECT * FROM student;

/*Drop user Zohaib*/
DROP USER 'Zohaib'@'localhost';

/* create new user */
CREATE USER 'Zohaib'@'localhost' IDENTIFIED BY '1379';

/* get all users */
SELECT * FROM mysql.user;

/* give select rights to new user */
GRANT SELECT ON university.* TO 'Zohaib'@'localhost';

/*Force a commit*/
commit work;

/* get all users */
SELECT * FROM mysql.user;