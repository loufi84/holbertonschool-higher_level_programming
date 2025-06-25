-- This script will lists all shows by their ratings
SELECT CONCAT(tv_shows.title, ' - ', SUM(tv_show_ratings.rating)) AS result
FROM tv_shows
JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_shows.title
ORDER BY SUM(tv_show_ratings.rating) DESC;