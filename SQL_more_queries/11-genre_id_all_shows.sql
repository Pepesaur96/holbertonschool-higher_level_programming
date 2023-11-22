-- import database dump and lists all shows

-- display: tv_show.title - tv_show_genres.genre_id

-- results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id

SELECT
    tv_shows.title,
    tv_show_genres.genre_id
from tv_shows
    LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY
    tv_shows.title ASC,
    tv_show_genres.genre_id ASC;