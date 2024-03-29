#!/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa starting with N """

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
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all rows that start with N
    for row in cursor.fetchall():
        if row[1][0] == 'N':
            print(row)

    # Close the cursor and connection
    cursor.close()
    connection.close()
