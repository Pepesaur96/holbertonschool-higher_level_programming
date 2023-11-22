#!/usr/bin/python3
""" takes in arguments and displays all values in the
states table of hbtn_0e_0_usa where name matches the
argument. But this time, write one that is safe from
MySQL injections! """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """Connect to MySQL server running on localhost at port 3306
    and get MySQL credentials from command line arguments"""
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3])

    # Create a cursor to execute SQL queries
    cursor = connection.cursor()

    # Execute the SELECT query
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY %s \
    ORDER BY id ASC", (argv[4],))

    # Fetch all rows whose name matches the argument
    for row in cursor.fetchall():
        if row[1] == argv[4]:
            print(row)

    # Close the cursor and connection
    cursor.close()
    connection.close()
