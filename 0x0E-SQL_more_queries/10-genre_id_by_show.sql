-- a script that lists all shows contained in hbtn_0d_tvshows
--  Each record should display: tv_shows.title - tv_show_genres.genre_id

SELECT tv_shows.title, tv_show_genres.genre_id -- Query to join cities and states
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
