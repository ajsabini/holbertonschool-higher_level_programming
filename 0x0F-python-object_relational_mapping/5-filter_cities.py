#!/usr/bin/python3
""" takes in an argument and display all values """

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
        cursor.execute("SELECT cities.namee FROM cities LEFT JOIN states\
                        ON states.id = cities.state_id WHERE states.name =%s\
                        ORDER BY cities.id ASC", (sys.argv[4],))
        rows = cursor.fetchall()
        print(", ".join([row[0] for in rows]))
        cursor.close()
        db.close()
    else:
        print("could not connect")
