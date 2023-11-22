-- lists all shows, all genres linked to that SHOW

-- if no genre, display NULL in genre column

-- display: tv_show.title - tv_genres.name

-- results must be sorted in ascending order by tv_shows.title and tv_genres.name

SELECT
    tv_shows.title,
    tv_genres.name
FROM tv_shows
    LEFT JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
    LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
ORDER BY
    tv_shows.title,
    tv_genres.name ASC;