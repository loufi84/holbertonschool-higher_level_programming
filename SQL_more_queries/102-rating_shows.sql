-- This script will lists all shows by their ratings
SELECT tv_shows.title, COALESCE(SUM(tv_show_ratings.rate), 0) AS rating
FROM tv_shows
LEFT JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_shows.id
ORDER BY rating DESC;