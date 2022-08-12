-- script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
-- Each record should display: <TV Show genre> - <Number of shows linked to this genre> 

SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows -- Query to join tables
FROM tv_show_genres
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC, tv_genres.id ASC;
