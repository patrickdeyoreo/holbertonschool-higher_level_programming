-- list all shows
SELECT tg.name AS genre, COUNT(*) as number_of_shows
FROM tv_genres tg
INNER JOIN tv_show_genres tsg
ON tg.id = tsg.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
