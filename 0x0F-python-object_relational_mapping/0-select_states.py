#!/usr/bin/python3
import MySQLdb
import sys
connection = MySQLdb.connect(host='localhost', user=sys.argv[1],
        passwd=sys.argv[2], db=sys.argv[3],
        port=3306)
cursor = connection.cursor()
cursor.execute("SELECT * FROM states ORDER BY id ASC")
states = cursor.fetchall()
for state in states:
    print(state)


