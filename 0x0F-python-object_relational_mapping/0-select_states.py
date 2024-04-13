#!/usr/bin/python3
if __name__ == '__main__':
    import MySQLdb
    """MySQLdb is  a python interface for connecting to databases. """
    db = MySQLdb.connect(host='localhost', user='root', password='password',
                         port=3306, db='hbtn_0e_0_usa')
    cur = db.cursor()

    cur.execute("select * from states")
    result = cur.fetchall()  # to fetch result from cur.execute
    for data in result:
        print(data)
    db.close()
