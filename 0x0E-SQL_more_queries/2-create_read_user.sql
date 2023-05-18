-- a script that creates the database hbtn_0d_2 and the user user_0d_2.

CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'User_0d_2_pwd';
GRANT SELECT on *.* TO 'user_0d_2'@'localhost' WITH GRANT OPTION;
CREATE DATABASE IF NOT EXISTS hbtn_0d_2
