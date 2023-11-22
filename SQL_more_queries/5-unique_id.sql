-- create a table unique_id
-- id=INT, default value 1 and must be unique, name=VARCHAR(256)
CREATE TABLE IF NOT EXISTS `unique_id` (`id` INT NOT NULL DEFAULT 1 UNIQUE, `name` VARCHAR(256));