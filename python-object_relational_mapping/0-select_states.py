#!usr/bin/python3
'''

'''
import MySQLdb
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=pwd, db=db_name)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC;")

    rows = cursor.fetchall()

    for id, name in rows:
        print(f"{id}, '{name}'")

    cursor.close()
    db.close()
