-- list all genres of the show Dexter
SELECT tg.name
FROM tv_genres tg
LEFT JOIN tv_show_genres tsg
ON tg.id = tsg.genre_id
INNER JOIN tv_shows ts
ON ts.id = tsg.show_id
WHERE ts.title = "DEXTER"
ORDER BY title;
