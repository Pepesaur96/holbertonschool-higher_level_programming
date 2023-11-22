-- create database hbtn_0d_usa and table cities
-- id=INT, unique, auto-generated, can't be null and primary key
-- state-id=INT, can't be null, must be foreign key that references to id of states table
-- name=VARCHAR(256)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS `cities` (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY, `state_id` INT NOT NULL, `name` VARCHAR(256) NOT NULL);