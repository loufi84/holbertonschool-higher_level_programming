#!/usr/bin/python3
"""

"""
import sys
import MySQLdb


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <mysql username> <mysqlpassword> <database name> "
              " <state name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()

    query = """
    SELECT cities.id, cities.name
    FROM cities
    JOIN states ON cities.stae_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name, ))

    rows = cursor.fetchall()

    print(", ".join([row[0] for row in rows]))

    cursor.close()
    db.close()
