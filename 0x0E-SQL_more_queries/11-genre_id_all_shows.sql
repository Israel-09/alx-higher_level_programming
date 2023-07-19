--  a script that lists all shows contained in the database hbtn_0d_tvshows.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- If a show doesn’t have a genre, display NULL.

SELECT s.title, t.genre_id FROM tv_shows AS s
LEFT JOIN tv_show_genres AS t
ON t.show_id = s.id
ORDER BY s.title, t.genre_id;
