#!/usr/bin/python3
"""MySQLdb is  a python interface for connecting to databases. """
import MySQLdb
import sys
if __name__ == '__main__':
    sr = sys.argv
    user_name = sr[1]
    user_password = sr[2]
    database = sr[3]
    search = sr[4]
    db = MySQLdb.connect(host='localhost', user=user_name,
                         password=user_password,
                         port=3306, db=database)
    cur = db.cursor()
# ABOVE..This creates an instance,to create multiple queries on the mysql db
    query = """SELECT
               cities.name AS city_name
               FROM cities
               INNER JOIN states ON cities.state_id = states.id
               WHERE states.name = BINARY %s;"""
    cur.execute(query, (search,))
# ABOVE.. This select unique entries by choosing based on min. id,
# as id is unique
    result = cur.fetchall()  # to fetch result from cur.execute
    city = map(lambda t: t[0], result)
    city = ", ".join(city)
    print(city)
    cur.close()  # closing a particular cursor object
    db.close()
