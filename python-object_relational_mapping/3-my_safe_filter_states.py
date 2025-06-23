#!/usr/bin/python3
"""
Script that displays all values in the states table matching the argument.
Prevents SQL injection.
"""
import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    searched_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (searched_name, ))

    states = cursor.fetchall()

    for state in states:
        print("({}, '{}')".format(state[0], state[1]))

    cursor.close()
    db.close()
