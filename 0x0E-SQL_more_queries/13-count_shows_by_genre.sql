-- list all shows without a genre linked
SELECT tv_genres.name AS genre, COUNT(*) as number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
