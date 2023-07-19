-- a script that lists all Comedy shows in the database hbtn_0d_tvshows.

SELECT s.title, g.name FROM tv_shows AS s
LEFT JOIN tv_show_genres AS t ON t.show_id = s.id
LEFT JOIN tv_genres AS g ON t.genre_id = g.id
ORDER BY s.title, g.name;
