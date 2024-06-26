#!/usr/bin/python3
"""MySQLdb is  a python interface for connecting to databases. """
import MySQLdb
import sys
if __name__ == '__main__':
    user_name = sys.argv[1]
    user_password = sys.argv[2]
    database = sys.argv[3]
    search = sys.argv[4]
    db = MySQLdb.connect(host='localhost', user=user_name,
                         password=user_password,
                         port=3306, db=database)
    cur = db.cursor()
    query = """SELECT *
           FROM states
           WHERE name = BINARY '{}'
           ORDER BY id;
        """.format(search)
# you can't order a clause, unless it has been grouped
# the group clause takes duplicates together
    cur.execute(query)
    # ABOVE.. This select unique entries by choosing based on min. id,
    # as id is unique
    result = cur.fetchall()  # to fetch result from cur.execute
    for data in result:
        print(data)
    cur.close()  # closing a particular cursor object
    db.close()   # closing entire db conection to mysql
