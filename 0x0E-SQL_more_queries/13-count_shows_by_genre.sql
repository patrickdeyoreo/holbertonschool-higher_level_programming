-- list all shows without a genre linked
SELECT tv_genres.name AS genre, COUNT(*) as number_of_shows
FROM tv_show_genres
LEFT JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
