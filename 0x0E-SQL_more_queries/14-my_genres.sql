-- a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.

SELECT g.name FROM tv_show_genres AS t
JOIN tv_genres AS g ON t.genre_id = g.id
JOIN tv_shows AS s ON t.show_id = s.id
WHERE s.title = 'Dexter'
ORDER BY g.name;
