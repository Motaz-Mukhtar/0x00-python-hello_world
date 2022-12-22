#!/usr/bin/python3
"""displays all values in the states table
of hbtn_0e_0_usa where name matches the argument,
but it safe from MySQL injections!
"""

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    curs.execute("select * from `states`")
    data = curs.fetchall()
    for i in data:
        if i[1] == sys.argv[4]:
            print(i)
