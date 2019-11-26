-- list all shows
SELECT tg.name as genre, COUNT(tsg.show_id) as number_of_shows
FROM tv_genres tg
INNER tv_show_genres tsg
ON tg.id = tsg.genre_id
WHERE number_of_shows > 0
GROUP BY genre
ORDER BY number_of_shows DESC;
