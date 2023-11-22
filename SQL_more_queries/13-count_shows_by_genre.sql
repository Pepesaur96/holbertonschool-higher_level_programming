-- lists all genres and display the number of shows linked to each

-- display <TV Show genre> - <Number of shows linked to this genre>

-- first column must be called genre

-- second column must be called number_of_shows

-- don’t display a genre that doesn’t have any shows linked

SELECT
    tv_genres.name AS genre,
    COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_show_genres
    INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY genre
ORDER BY number_of_shows DESC;