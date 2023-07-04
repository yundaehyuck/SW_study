
-- zoo라는 이름의 table생성
-- name, eat, weight, height, age라는 컬럼을 가짐
CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

-- zoo라는 테이블에 6개의 레코드를 차례대로 넣는다

INSERT INTO zoo VALUES 
('gorilla', 'omnivore', 215, 180, 5),
('tiger', 'carnivore', 220, 115, 3),
('elephant', 'herbivore', 3800, 280, 10),
('dog', 'omnivore', 8, 20, 1),
('panda', 'herbivore', 80, 90, 2),
('pig', 'omnivore', 70, 45, 5);

-- 다음 zoo라는 테이블에서 weight < 100을 만족하는 레코드를 제거하는데
BEGIN;
  DELETE FROM zoo
  WHERE weight < 100;
ROLLBACK;
-- rollback에 의해 처음 시점으로 복원한다
-- 레코드를 삭제하지 않은 처음 시점으로 복원

-- 다시 zoo에서 eat = 'omnivore'를 만족하는 레코드를 모두 제거
-- commit에 의해 실제로 테이블에 반영시킴
-- eat='omnivore'라는 레코드는 3개이므로, zoo 테이블에는 3개의 레코드만 남음
BEGIN;
  DELETE FROM zoo
  WHERE eat = 'omnivore';
COMMIT;

-- zoo 테이블에서 레코드의 수를 센다
-- 위에서 레코드가 3개 남았으므로 COUNT(*)에는 3이 들어가있을것
SELECT COUNT(*)
FROM zoo;
