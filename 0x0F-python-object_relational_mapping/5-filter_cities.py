#!/usr/bin/python3
'''
a script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
'''
import MySQLdb
import sys


def list_city():
    '''
    a script that takes in the name of a state as an argument and lists
    all cities of that state, using the database hbtn_0e_4_usa
    '''
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])
    cur = conn.cursor()

    cur.execute("SELECT cities.name FROM cities JOIN states ON\
                cities.state_id = states.id WHERE states.name =  %s\
                ORDER BY cities.id ASC", (sys.argv[4],))
    query_rows = cur.fetchall()
    list_row = [row[0] for row in list_row]

    print(*list_row, sep=', ')
    cur.close()
    conn.close()


if __name__ == "__main__":
    list_city()
