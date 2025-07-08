CREATE DATABASE studentdb;

USE studentdb;

CREATE TABLE studentsdata (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    age INT,
    marks FLOAT
);
select*from studentsdata;
