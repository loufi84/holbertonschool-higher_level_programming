-- List the number of records with same score
SELECT score, COUNT(*) AS number
FROM second_table
GROUP_BY score
ORDER BY number DESC;