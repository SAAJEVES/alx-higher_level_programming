#!/usr/bin/python3
"""a script that lists all states with a name starting with
    N (upper N) from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


def filter_N():
    """Filters through to get states that starts with N"""
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1]
                           passwd=sys.argv[2], db=sys.argv[3],
                           port=3306, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE states.name LIKE 'N%' ORDER BY
                states.id ASC")
    query_row = cur.fetchall()
    for row in query_row:
        print(row)
    cur.close()
    conn.close()


if __name__ = "__main__":
    filter_N()
