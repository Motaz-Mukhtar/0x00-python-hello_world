#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


db = MySQLdb.connec\
 t(host='localhost', user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
curs = db.cursor()

data = curs.execute("select * from states")
dat = curs.fetchall()

for i in dat:
    print(i)
