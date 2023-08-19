#!/usr/bin/python3
'''select specific column in database'''

if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(user=argv[1], password=argv[2],
                         db=argv[3], host='localhost',
                         port=3306)
    cur = db.cursor()
    cur.execute(f"""SELECT id, name FROM states
            WHERE name='{argv[4]}' ORDER BY id;""")
    rows = cur.fetchall()
    for row in rows:
        print(f"{row}")
    cur.close()
    db.close()
