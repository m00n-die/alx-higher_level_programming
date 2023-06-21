#!/usr/bin/python3


import MySQLdb
import sys


if __name__ == "__main__":
    username = str(sys.argv[1])
    password = str(sys.argv[2])
    dbName = str(sys.argv[3])

    db = MySQLdb.connect(host = "localhost", user = "{}".format(username),
                        password = "{}".format(password), database = "{}".format(dbName))
    cur = db.cursor()
    cur.execute("""
            SELECT
                cities.id, cities.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            WHERE
                states.name LIKE BINARY %(state_name)s
            ORDER BY
                cities.id ASC
        """, {
            'state_name': sys.argv[4]
        })

    result = cur.fetchall()

    if result is not None:
        print(", ".join([row[1] for row in result]))
