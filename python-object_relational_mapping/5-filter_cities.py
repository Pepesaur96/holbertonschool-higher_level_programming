#!/usr/bin/python3
"""a script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    # Connect to MySQL server running on localhost at port 3306
    # and get MySQL credentials from command line arguments
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3])

    # Create a cursor to execute SQL queries
    cursor = connection.cursor()

    # Execute the SELECT query
    cursor.execute("SELECT cities.name FROM cities \
    INNER JOIN states ON cities.state_id = states.id \
    WHERE states.name = %s ORDER BY cities.id ASC", (argv[4],))

    # Print all rows
    print(", ".join([row[0] for row in cursor.fetchall()]))

    # Close the cursor and connection
    cursor.close()
    connection.close()
