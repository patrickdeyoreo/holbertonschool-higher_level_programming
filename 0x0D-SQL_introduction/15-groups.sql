-- list all records of the table second_table of the data
SELECT `score`, COUNT(*) as number
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
