#!/usr/bin/python3
"""displays all values in the states table
of hbtn_0e_0_usa where name matches the argument"""

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    curs.execute("select * from `states` where binary `name` = '{}'"
                 .format(sys.argv[4]))
    [print(i) for i in curs.fetchall()]
