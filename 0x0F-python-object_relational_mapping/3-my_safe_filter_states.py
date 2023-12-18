#!/usr/bin/python3
"""
write a script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument. But this time, write
one that is safe from MySQL injections!
"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        pass
    else:
        conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3],
                               port=3306)
        cur = conn.cursor()
        cur.execute("SELECT * FROM states WHERE states.name LIKE BINARY\
                    %s",(sys.argv[4],))
        query_rows = cur.fetchall()

        for row in query_rows:
            print(row)
        cur.close()
        conn.close()
