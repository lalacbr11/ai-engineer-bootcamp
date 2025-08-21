
SELECT * FROM students;

SELECT AVG(age) AS avg_age FROM students;

SELECT grade, COUNT(*)
FROM students
GROUP BY grade;
