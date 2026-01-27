/*retrieve all course names that have the vowels A, E, I, O, U in that order, contiguously one after another*/
SELECT title FROM course WHERE title LIKE '%AEIOU%';

/*retrieve all course names that have the vowels A, E, I, O, U in that order, sequentially but not necessarily contiguously*/
SELECT title FROM course WHERE title LIKE '%A%E%I%O%U%';

/*retrieve all course names that have the vowels A, E, I, O, U in any order*/
SELECT TITLE FROM COURSE WHERE title LIKE '%A%' AND title LIKE '%E%' AND title LIKE '%I%' AND title LIKE '%O%' AND title LIKE '%U%';

/*retrieve all course names that have at least one of the vowels A, E, I, O, U*/
SELECT TITLE FROM COURSE WHERE title LIKE '%A%' OR title LIKE '%E%' OR title LIKE '%I%' OR title LIKE '%O%' OR title LIKE '%U%';

/*retrieve all course names that have none of the vowels A, E, I, O, U*/
SELECT TITLE FROM COURSE WHERE title NOT LIKE '%A%' AND title NOT LIKE '%E%' AND title NOT LIKE '%I%' AND title NOT LIKE '%O%' AND title NOT LIKE '%U%';

/*retrieve all instructors and students and their departments, with four columns: status (either 'student' or 'instructor'), id, name, and department*/
SELECT 'student' AS status, id, name, dept_name AS department FROM student
UNION
SELECT 'instructor', id, name, dept_name AS department FROM instructor;

/*retrieve the names of all students who failed a course (grade of F) along with the name of the course that they failed*/
SELECT student.name, course.title FROM student NATURAL JOIN takes JOIN course ON (takes.course_id = course.course_id) WHERE grade = 'F';

/*retrieve the number of solid A grades*/
SELECT COUNT(grade) AS solid_A_grades FROM takes WHERE grade = 'A';

/*retrieve the names and numbers of all grades*/
SELECT COUNT(grade) AS all_grades FROM takes WHERE grade IS NOT NULL;

/*retrieve the percentage of solid A grades compared to all courses, and rename that column "Percent_A"*/
SELECT (SELECT COUNT(grade) AS solid_A_grades FROM takes WHERE grade = 'A') / (SELECT COUNT(grade) AS all_grades FROM takes WHERE grade IS NOT NULL) AS Percent_A;

/*retrieve the names and numbers of all courses that do not have prerequisites.*/
SELECT title AS name, course_id AS number FROM course WHERE course_id NOT IN (SELECT course_id FROM prereq);

/*retrieves the names of all students and the names of their advisor if they have one.*/
SELECT student.name AS student_name, instructor.name AS advisor FROM student LEFT OUTER JOIN advisor ON (student.id = advisor.s_id) LEFT OUTER JOIN instructor ON (advisor.i_id = instructor.id);
