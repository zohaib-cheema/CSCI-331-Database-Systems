/*[4] Create a table grade_points (grade, points) that maps letter grades to number grades.*/
DROP TABLE IF EXISTS grade_points;

CREATE TABLE grade_points (
    grade VARCHAR(2) PRIMARY KEY,
    points DECIMAL(2,1),
    CONSTRAINT chk_grade_points CHECK (points >= 0 AND points <= 4.0)
);

/*Insert the grades and their points*/
INSERT INTO grade_points
VALUES ('A', 4.0),('A-', 3.7), ('B+', 3.3),('B', 3.0),('B-', 2.7),('C+', 2.3),
       ('C', 2.0),('C-', 1.7),('D+', 1.3),('D', 1.0),('D-', 0.7),('F+', 0.3),('F', 0.0);

/*Retrieve grades and their points*/
SELECT * FROM grade_points;

/*[5] Add a foreign key from the grade column in the existing takes table to the new grade_points table. Omitted due to data dependency issues.*/
-- ALTER TABLE takes ADD CONSTRAINT fk_takes_grade_points FOREIGN KEY (grade) REFERENCES grade_points(grade);

/*[6] Create a view v_takes_points that returns the data in takes table along with the numeric equivalent of the grade.*/
CREATE OR REPLACE VIEW v_takes_points AS (SELECT id AS student_id, course_id, semester, year, takes.grade AS grade, points FROM takes NATURAL JOIN grade_points WHERE takes.grade = grade_points.grade);

/*Retrieve rows from v_takes_points*/
SELECT * FROM v_takes_points;

/*[7] Compute the total number of grade points (credits * grade points) earned by student X (pick a student id from the DB). You will need to join takes, course, and the new grade_points tables. If the student is in the system, but hasn't taken any courses, the student's total points is 0.*/
SELECT COALESCE(SUM(course.credits * v_takes_points.points), 0) AS total_points
FROM course, v_takes_points
WHERE course.course_id = v_takes_points.course_id AND student_id = '45678';

/*[8] Compute the GPA - i.e. total grade points / total credits - for the same student in the previous question.*/
SELECT COALESCE((SELECT SUM(course.credits * v_takes_points.points) FROM course, v_takes_points WHERE course.course_id = v_takes_points.course_id AND student_id = '45678') / 
(SELECT SUM(course.credits) FROM course, v_takes_points WHERE course.course_id = v_takes_points.course_id AND student_id = '45678'), 0) AS gpa_student_45678;

/*[9] Find the GPA of all students, i.e. not just for one student at a time.*/
SELECT student.id, COALESCE(SUM(course.credits * v_takes_points.points) / SUM(course.credits), 0) AS gpa
FROM student LEFT JOIN v_takes_points ON student.id = v_takes_points.student_id
LEFT JOIN course ON v_takes_points.course_id = course.course_id
GROUP BY student.id;

/*[10] Create a view v_student_gpa (id, gpa) that gives a dynamic version of the information in the previous question.*/
CREATE OR REPLACE VIEW v_student_gpa AS (SELECT student.id AS id, COALESCE(SUM(course.credits * v_takes_points.points) / SUM(course.credits), 0) AS gpa FROM student LEFT JOIN v_takes_points ON student.id = v_takes_points.student_id LEFT JOIN course ON v_takes_points.course_id = course.course_id GROUP BY student.id);

/*Retrieve rows from v_student_gpa*/
SELECT * FROM v_student_gpa;

/*[11] Determine the rank of the students and their GPAs adapting the query with rank() from the slides.*/
SELECT id, RANK() OVER (ORDER BY gpa DESC) AS s_rank, gpa
FROM v_student_gpa
ORDER BY s_rank;

/*[12] Determine the rank of the students and their GPAs adapting the query without rank() from the slides.*/
SELECT id, (1 + (SELECT COUNT(*) FROM v_student_gpa B WHERE B.gpa > A.gpa)) AS s_rank, gpa
FROM v_student_gpa A
ORDER BY s_rank;
