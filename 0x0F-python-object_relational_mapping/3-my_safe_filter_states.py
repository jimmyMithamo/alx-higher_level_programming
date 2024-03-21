#!/usr/bin/python3
"""this script lists all states with a name  
matching the argument that is free from sql injections"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    sql_query = "SELECT * FROM states WHERE name = %s ORDER BY states.id"
    cur.execute(sql_query, (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()