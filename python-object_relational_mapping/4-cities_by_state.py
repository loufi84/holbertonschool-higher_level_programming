#!/usr/bin/python3
"""
Script to list all cities from the DB, including corresponding state name.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()

    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """
    cursor.execute(query)

    results = cursor.fetchall()

    for row in results:
        print("({}, '{}')".format(row[0], row[1], row[2]))

    cursor.close()
    db.close()
