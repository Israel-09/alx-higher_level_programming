-- a script that lists all records of the table second_table of the database hbtn_0c_0

SELECT name, score FROM second_table WHERE name is NOT NULL 
ORDER BY score DESC
