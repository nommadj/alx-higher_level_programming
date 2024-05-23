#!/usr/bin/python3
'''script that lists all cities from the database hbtn_0e_4_usa'''


import MySQLdb
from sys import argv

if __name__ == "__main__":
    username, password, database = argv[1], argv[2], argv[3]

    # connect to the database
    connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
    )
    # create a cursor to interact with the database
    cursor = connection.cursor()
    # execute the SQL query
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON states.id = cities.state_id
        ORDER BY cities.id ASC
    """
    cursor.execute(query)
    # fetch the results
    results = cursor.fetchall()
    # process the results
    for row in results:
        print(row)
    # close cursor and connection
    cursor.close()
    connection.close()
