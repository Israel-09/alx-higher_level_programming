-- a script that creates the database hbtn_0d_usa and the table cities
-- (in the database hbtn_0d_usa) on your MySQL server.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE if NOT EXISTS states(
	id INT AUTO_INCREMENT NOT NULL PRIMARY KEY UNIQUE,
	state_id INT NOT NULL, FOREIGN KEY(id) REFERENCES state(id),
	name VARCHAR(256) NOT NULL
);

