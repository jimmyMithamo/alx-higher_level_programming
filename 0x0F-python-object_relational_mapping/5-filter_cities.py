#!/usr/bin/python3
"""this script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    sql_query = """SELECT GROUP_CONCAT(cities.name SEPARATOR ',') FROM cities
    JOIN states ON cities.state_id = states.id WHERE states.name = %s 
    ORDER BY cities.id"""
    cur.execute(sql_query, (sys.argv[4],))
    rows = cur.fetchone()
    if rows:
        print(rows[0])

    cur.close()
    db.close()