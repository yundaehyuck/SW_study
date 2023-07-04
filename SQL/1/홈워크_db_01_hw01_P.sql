CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

-- 1) 
INSERT INTO zoo VALUES 
(5, 180, 210, 'gorilla', 'omnivore');

-- 2)
INSERT INTO zoo (rowid, name, eat, weight, age) VALUES
(10,'dolphin', 'carnivore', 210, 3),
-- rowid는 고유값인데 중복되어서 에러남
-- 그래서 rowid를 바꿔줌
-- (10, 'alligator', 'carnivore', 250, 50);
(15, 'alligator', 'carnivore', 250, 50);

-- 3)

-- weight는 NULL이 없어야하는데, 이러면 weight에 NULL이 들어가서 에러
-- weight에 값을 넣어주든지 해야함
-- INSERT INTO zoo (name, eat, age) VALUES
INSERT INTO zoo (name,eat,weight,age) VALUES
-- ('dolphin', 'carnivore', 3);
('dolphin', 'carnivore', 260, 3);
