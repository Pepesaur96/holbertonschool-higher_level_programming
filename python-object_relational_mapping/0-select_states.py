#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials from command line arguments
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL server running on localhost at port 3306
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database_name
    )

    # Create a cursor to execute SQL queries
    cursor = connection.cursor()

    # Execute the SELECT query
    query = "SELECT * FROM states ORDER BY id"
    cursor.execute(query)

    # Fetch all rows
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and connection
    cursor.close()
    connection.close()
