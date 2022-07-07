-- script creates database hbtn_0d_usa and table cities in database
CREATE DATABASE if not exists hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE if not exists hbtn_0d_usa.cities (id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY, state_id INT NOT NULL, FOREIGN KEY(state_id) REFERENCES states(id), name VARCHAR(256) NOT NULL)
