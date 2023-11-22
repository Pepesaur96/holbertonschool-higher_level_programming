# GENERAL TOPICS

# What's a database?

A database is a structured collection of data organized in a way that a computer program can quickly select and retrieve specific pieces of data. It can store and manage large amounts of information efficiently.

# What's a relational database?

A relational database is a type of database that stores and organizes data into tables with predefined relationships between them. The relationships are established using keys, and this structure allows for efficient querying and retrieval of information.

# What does SQL stand for?

SQL stands for Structured Query Language. It is a domain-specific language used to manage and manipulate relational databases. SQL is used for tasks such as querying data, updating data, and defining the structure of a database.

# What's MySQL?

MySQL is an open-source relational database management system (RDBMS). It uses SQL for managing and manipulating data. MySQL is widely used for web applications and is known for its reliability, performance, and ease of use.

# How to create a database in MySQL:

    CREATE DATABASE your_database_name;

# What does DDL and DML stand for?

DDL stands for Data Definition Language, and it is used to define and manage the structure of a database, such as creating or modifying tables.
DML stands for Data Manipulation Language, and it is used to manipulate the data stored in a database, such as querying, inserting, updating, or deleting data.

# How to CREATE or ALTER a table:

- To create a table:

  CREATE TABLE your_table_name (
  column1 datatype1,
  column2 datatype2,
  ...
  );

- To alter a table (add a new column, for example):

  ALTER TABLE your_table_name
  ADD COLUMN new_column datatype;

# How to SELECT data from a table:

- Basic SELECT statement:

  SELECT column1, column2, ...
  FROM your_table_name
  WHERE condition;

# How to INSERT, UPDATE, or DELETE data:

- Inserting data:

  INSERT INTO your_table_name (column1, column2, ...)
  VALUES (value1, value2, ...);

- Updating data:

  UPDATE your_table_name
  SET column1 = value1, column2 = value2, ...
  WHERE condition;

- Deleting data:

  DELETE FROM your_table_name
  WHERE condition;

# What are subqueries:

A subquery is a query nested inside another query. It can be used to retrieve data that will be used in the main query's condition or to perform operations based on the results of the subquery.

# How to use MySQL functions:

MySQL provides a variety of built-in functions for performing operations on data. Examples include:

- Mathematical functions (e.g., SUM, AVG, COUNT)
- String functions (e.g., CONCAT, SUBSTRING)
- Date and time functions (e.g., NOW, DATE_FORMAT)

Example:

    SELECT AVG(column1) AS average_value
    FROM your_table_name;
