#!/usr/bin/python3
"""a script that lists all cities
from the database hbtn_0e_4_usa"""

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
    cur.execute("""
        SELECT
            cities.id, cities.name, states.name
        FROM
            cities
        JOIN
            states
        ON
            cities.state_id = states.id
        ORDER BY
            cities.id ASC;""")
    result = cur.fetchall()
    for city in result:
        print(city)
    db.close()
