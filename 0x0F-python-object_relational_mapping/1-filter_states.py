#!/usr/bin/python3

import MySQLdb
import sys

db = MySQLdb.connec\
 t(host='localhost', user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
curs = db.cursor()
curs.execute("select * from states")
data = curs.fetchall()

for i in data:
    if i[1][0] == 'N':
        print(i)
