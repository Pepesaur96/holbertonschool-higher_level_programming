#!/usr/bin/python3
"""a script that lists all cities from the database hbtn_0e_4_usa"""

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
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities \
    INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")

    # Print all rows
    for row in cursor.fetchall():
        print(row)

    # Close the cursor and connection
    cursor.close()
    connection.close()
