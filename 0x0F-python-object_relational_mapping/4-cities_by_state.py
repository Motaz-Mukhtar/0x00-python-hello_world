#!/usr/bin/python3
""" Lists all cities from the database hbtn_0e_4_usa """

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    curs = db.cursor()
    curs.execute("SELECT `cities`.`id`, `cities`.`name`, `states`.`name`\
                    FROM `cities`\
                    INNER JOIN `states` ON `cities`.`state_id` = `states`.`id`\
                    ")
    [print(i) for i in curs.fetchall()]
