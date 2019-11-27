-- list all shows without a genre linked
SELECT tg.name AS genre, COUNT(*) as number_of_shows
FROM tv_show_genres tsg
LEFT JOIN tv_genres tg
ON tg.id = tsg.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
