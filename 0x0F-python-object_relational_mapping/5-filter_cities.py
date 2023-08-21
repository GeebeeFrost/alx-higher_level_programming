#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa
where name matches the argument provided.
This script is safe from SQL injection.
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost", user=argv[1], passwd=argv[2], db=argv[3]
            )
    cur = db.cursor()
    cur.execute(
            "SELECT cities.name\
            FROM cities JOIN states ON cities.state_id = states.id\
            WHERE states.name LIKE BINARY %(state_name)s\
            ORDER BY cities.id ASC",
            {'state_name': argv[4]}
            )
    query_rows = cur.fetchall()
    print(", ".join(row[0] for row in query_rows))
    cur.close()
    db.close()
