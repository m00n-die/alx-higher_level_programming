#!/usr/bin/python3
"""a script that lists all states
from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


if __name__ == "__main__":
    """prevents code execution when imported"""
    username = str(sys.argv[1])
    password = str(sys.argv[2])
    dbName = str(sys.argv[3])

    db = MySQLdb.connect(host="localhost", user="{}".format(username),
                         password="{}".format(password),
                         database="{}".format(dbName))
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id ASC;")
    result = cur.fetchall()
    for state in result:
        print(state)
    db.close()
