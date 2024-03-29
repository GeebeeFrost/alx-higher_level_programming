#!/usr/bin/python3
"""
This script lists all states with name starting with N
from the database hbtn_0e_0_usa.
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost", user=argv[1], passwd=argv[2], db=argv[3]
            )
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE \
                BINARY '{}' ORDER BY id ASC".format(argv[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
