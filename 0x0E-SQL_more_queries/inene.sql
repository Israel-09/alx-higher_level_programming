-- a script that creates the MySQL server user user_0d_1.

CREATE USER IF NOT EXISTS inene@localhost IDENTIFIED BY 'User_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO inene@localhost WITH GRANT OPTION;
