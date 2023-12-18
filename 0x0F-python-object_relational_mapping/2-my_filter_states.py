#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
"""
import sys
import MySQLdb


def search():
    conn = MySQLdb.connect(hostname="localhost", username=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3],
                           port=3306)
    cur = conn.cursor()

    cur.execute("SELECT * FROM states WHERE states.name = '{}'\
                ORDER BY states.id".format(sys.argv[4]))
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    search()
