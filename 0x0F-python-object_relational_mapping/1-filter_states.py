#!/usr/bin/python3
"""lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    curs.execute("select * from states")
    data = curs.fetchall()

    for i in data:
        if i[1][0] == 'N':
            print(i)
