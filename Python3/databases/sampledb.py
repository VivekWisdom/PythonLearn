#/usr/bin/python3

import sqlite3

def main():
    db = sqlite3.connect('test.db')
    db.execute('drop table if exists test')
    db.execute('create table test (name text, num int)')
    db.execute('insert into test (name, num) values (?, ?)', ('Test1', 12345))
    db.execute('insert into test (name, num) values (?, ?)', ('Test2', 23456))
    db.execute('insert into test (name, num) values (?, ?)', ('Test3', 34567))
    db.execute('insert into test (name, num) values (?, ?)', ('Test4', 45678))

    db.commit()

    cursor = db.execute('select * from test order by num')

    for row in cursor:
        print(row)

if __name__ == '__main__':
    main()