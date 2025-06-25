-- This script will compute the average temperature in Farenheit of different cities
-- And order them by descending order
USE hbtn_0c_0
SELECT city, AVG(value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;