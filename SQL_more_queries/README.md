# GENERAL TOPICS:

# How to create a new MySQL user:

    CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';

# How to manage privileges for a user to a database or table:

- Granting privileges:

  GRANT privileges ON database.table TO 'username'@'localhost';

- Example granting all privileges:

  GRANT ALL PRIVILEGES ON database.\* TO 'username'@'localhost';

- Revoking privileges:

  REVOKE privileges ON database.table FROM 'username'@'localhost';

# What’s a PRIMARY KEY:

A PRIMARY KEY is a column or a set of columns in a table that uniquely identifies each row in that table. It must contain unique values, and it cannot have NULL values.

# What’s a FOREIGN KEY:

A FOREIGN KEY is a column or a set of columns in a table that refers to the PRIMARY KEY of another table. It establishes a link between the two tables, enforcing referential integrity.

# How to use NOT NULL and UNIQUE constraints:

To specify that a column cannot contain NULL values:

    CREATE TABLE your_table (
    column1 INT NOT NULL,
    ...
    );

To specify that a column must contain unique values:

    CREATE TABLE your_table (
    column1 INT UNIQUE,
    ...
    );

# How to retrieve data from multiple tables in one request:

Using JOIN operations, such as INNER JOIN, LEFT JOIN, or RIGHT JOIN:

    SELECT \*
    FROM table1
    INNER JOIN table2 ON table1.column = table2.column;

# What are subqueries:

A subquery is a query nested inside another query. It can be used to retrieve data that will be used in the main query's condition or to perform operations based on the results of the subquery.

# What are JOIN and UNION:

JOIN: Combines rows from two or more tables based on a related column between them.

    SELECT \*
    FROM table1
    INNER JOIN table2 ON table1.column = table2.column;

UNION: Combines the result sets of two or more SELECT statements into a single result set.

    SELECT column1 FROM table1
    UNION
    SELECT column1 FROM table2;
