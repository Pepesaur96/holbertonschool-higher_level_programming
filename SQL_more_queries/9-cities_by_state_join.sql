-- lists all cities contained database hbtn_0d_usa

-- display: cities.id - cities.name - states.name

-- results must be sorted in ascending order by cities.id

-- You can only use one SELECT statement

SELECT
    cities.id,
    cities.name,
    states.name
FROM cities
    INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;