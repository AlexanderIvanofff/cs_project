CREATE TABLE students
(
    id         int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    first_name varchar(255),
    last_name  varchar(255),
    course_id  int
);

CREATE TABLE courses
(
    id           int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    title        varchar(255),
    credits      varchar(255),
    professor_id int
);

CREATE TABLE professors
(
    id         int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    first_name varchar(255),
    last_name  varchar(255),
    title_id   int NOT NULL
);

CREATE TABLE titles
(
    id         int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    title_name varchar(255)
);