CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  age INT NOT NULL,
  grade TEXT
);

INSERT INTO students (name, age, grade) VALUES
('Laura', 30, 'A'),
('Emma', 25, 'B'),
('Olivia', 28, 'A'),
('Mia', 22, 'C');

