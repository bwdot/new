-- Active: 1705443952332@@34.132.247.25@3306
CREATE DATABASE FiberOptic;
USE FiberOptic;
CREATE TABLE student(
    student_id INT PRIMARY KEY,
    name VARCHAR(20),
    major VARCHAR(20)
);
DESC student;

INSERT INTO student VALUES(2, 'Jack', 'Biology');

DROP TABLE student;

SELECT * FROM student;
