#!/usr/bin/python3
""" takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa  """

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    curs = db.cursor()
    curs.execute("SELECT `cities`.`id`, `cities`.`name`, `states`.`name`\
                    FROM `cities`\
                    INNER JOIN `states` ON `cities`.`state_id` = `states`.`id`\
                    ")
    for i in curs.fetchall():
        if i[2] == sys.argv[4]:
            print(i[1], end=", ")
    print()
