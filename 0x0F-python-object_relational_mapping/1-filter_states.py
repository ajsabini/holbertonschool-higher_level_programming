#!/usr/bin/python3
""" list states that star with N"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    user_name = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host='localhost', port=3306, user=user_name,
                         passwd=password, db=db_name, charset='utf8')

    cursor = db.cursor()
    if (db):
        cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'" +
                       "ORDER BY states.id")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    else:
        print("could not connect")
