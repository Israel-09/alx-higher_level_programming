-- a script that creates the database hbtn_0d_usa and the table cities
-- (in the database hbtn_0d_usa) on your MySQL server.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE if NOT EXISTS cities(
	id INT AUTO_INCREMENT NOT NULL PRIMARY KEY UNIQUE,
	state_id INT NOT NULL, FOREIGN KEY(state_id) REFERENCES states(id),
	name VARCHAR(256) NOT NULL
);

-- FOREIGN KEY (foreign_key_column) REFERENCES another_table (id)

