-- a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.

SELECT g.name AS genre, COUNT(*) AS number_of_shows
FROM tv_show_genres AS s JOIN tv_genres AS g
ON s.genre_id = g.id GROUP BY s.genre_id
ORDER BY number_of_shows DESC;

