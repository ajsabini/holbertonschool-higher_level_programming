#!/usr/bin/python3
""" list all states """

if __name__ == '__main__':
    
    import MySQLdb
    import sys

    user_name = str(sys.argv[1])
    password = str(sys.argv[2])
    db_name = str(sys.argv[3])

    db = MySQLdb.connect(host='localhost', port=3306, user=user_name,
                         passwd=password, db=db_name, charset='utf8')

    cursor = db.cursor()
    if (db):
        cursor.execute("SELECT * FROM states ORDER BY states.id")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    else:
        print("could not connect")
