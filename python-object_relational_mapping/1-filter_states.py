#!/usr/bin/python3
"""
This module will print the list of states beginning with a N.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()

    toolng = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    cursor.execute(toolng)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
