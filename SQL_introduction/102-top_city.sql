-- This script will display the top 3 cities temperatures during July and August
-- and order them by descending
SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE month IN ('July', 'August')
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;