-- a script that lists all Comedy shows in the database hbtn_0d_tvshows.

SELECT s.title FROM tv_show_genres AS t
JOIN tv_shows AS s ON t.show_id = s.id
JOIN tv_genres AS g ON t.genre_id = g.id
WHERE g.name = 'Comedy'
ORDER BY s.title;
