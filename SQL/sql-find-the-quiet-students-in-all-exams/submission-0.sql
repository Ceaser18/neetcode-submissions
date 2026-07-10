-- Write your query below
WITH ranked AS
(
SELECT student_id,
       exam_id,
       RANK() OVER(PARTITION BY exam_id ORDER BY score DESC) r1,
       RANK() OVER(PARTITION BY exam_id ORDER BY score ASC) r2
FROM Exam
)

SELECT s.student_id,
       s.student_name
FROM Student s
JOIN Exam e
ON s.student_id=e.student_id
WHERE s.student_id NOT IN
(
    SELECT student_id
    FROM ranked
    WHERE r1=1 OR r2=1
)
GROUP BY s.student_id,s.student_name
ORDER BY s.student_id;