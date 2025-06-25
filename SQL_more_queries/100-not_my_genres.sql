-- This script will display all genres not linked to the show Dexter
SELECT name
FROM tv_genres
WHERE id NOT IN (
    SELECT tsg.genre_id
    FROM tv_show_genres AS tsg
    JOIN tv_shows as ts
    ON tsg.show_id = ts.id
    WHERE ts.title = 'Dexter'
)
ORDER BY name ASC;