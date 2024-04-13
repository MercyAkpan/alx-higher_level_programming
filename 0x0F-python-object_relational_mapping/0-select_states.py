#!/usr/bin/python3
"""MySQLdb is  a python interface for connecting to databases. """
import MySQLdb
import sys
if __name__ == '__main__':
    user_name = sys.argv[1]
    user_password = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(host='localhost', user=user_name,
                         password=user_password,
                         port=3306, db=database)
    cur = db.cursor()

    cur.execute("SELECT * FROM states")
    result = cur.fetchall()  # to fetch result from cur.execute
    for data in result:
        print(data)
    cur.close()
    db.close()
