#!/usr/bin/python3
'''
This module will print the list of states beginning with a N.
'''
import MySQLdb
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.atgv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, pwd=passwd, database=db_name)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name"
                   "LIKE 'N%' ORDER BY is ASC;")
    rows = cursor.fetchall()

    for id, name in rows:
        print("({}, '{}')".format(id, name))

    cursor.close()
    db.close()
