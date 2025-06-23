#!/usr/bin/python3
"""

"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Récupère les arguments en stdin
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connecte la base SQL server
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Ouverture du curseur
    cursor = db.cursor()

    query = ("SELECT * FROM states WHERE name = '{}' "
             "ORDER BY id ASC".format(state_name))

    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    # Nettoyage
    cursor.close()
    db.close()
