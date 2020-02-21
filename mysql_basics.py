"""
1. Append more data
2. Display the teacher table
3. Display the teacher table sorted on descending bsal
4. Search for a teacher on code
5. Find teachers of a department
6. Increase bsal of every teacher by 5%
7. Delete record on code
"""

import MySQLdb

conn = MySQLdb.connect(host='localhost', user='root', passwd='')
chitty = conn.cursor()
chitty.execute('drop database school')
chitty.execute('create database if not exists school')
chitty.execute('use school')


def append():
    chitty.execute("create table if not exists teacher(CODE int, NAME char(20), DEPT char(15), NOP int, BSAL float)")
    data = [[2011, 'MR. JATIN', 'MATHEMATICS', 27, 150000],
            [2012, 'MR. ADITYA', 'PHYSICS', 24, 136500],
            [2013, 'MR. PRANAV', 'CHEMISTRY', 26, 147000],
            [2014, 'MS. ROOPA', 'PHYSICS', 25, 178500],
            [2015, 'MS. GEETA', 'PHYSICS', 27, 139125],
            [2016, 'MS. MALATI', 'MATHEMATICS', 24, 141750],
            [2017, 'MS. MARIA', 'CHEMISTRY', 24, 131250],
            [2018, 'MR. DEEPAK', 'CHEMISTRY', 27, 173250],
            [2019, 'MS. PARUL', 'MATHEMATICS', 25, 120750],
            [2020, 'MR. KUNAL', 'PHYSICS', 27, 131250],
            [2021, 'MS. TANIA', 'CHEMISTRY', 26, 143850],
            [2022, 'MR. PRADIP', 'PHYSICS', 24, 126000],
            [2023, 'MS. ANCHAL', 'MATHEMATICS', 25, 136500],
            [2024, 'MS. SAMEER', 'CHEMISTRY', 27, 147000]]
    for i in data:
        query = "insert into teacher values({},'{}','{}',{},{})".format(i[0], i[1], i[2], i[3], i[4])
        chitty.execute(query)
        conn.commit()
    print('Records Appended\n')


def display():
    query = 'select * from teacher'
    chitty.execute(query)
    data = chitty.fetchall()
    for rec in data:
        print(rec[0], rec[1], rec[2], rec[3], rec[4], sep='\t')
    print()


def bsal():
    query = 'select * from teacher order by bsal desc'
    chitty.execute(query)
    for rec in chitty:
        print(rec[0], rec[1], rec[2], rec[3], rec[4], sep='\t')
    print()


def search():
    code = int(input('Enter code: '))
    query = 'select * from teacher where code={}'.format(code)
    chitty.execute(query)
    if chitty == 0:
        print('No such record')
    else:
        for rec in chitty:
            print(rec[0], rec[1], rec[2], rec[3], rec[4], sep='\t')
    print()


def dept():
    dept = input('Enter department: ')
    query = 'select * from teacher where dept="{}"'.format(dept)
    chitty.execute(query)
    if chitty == 0:
        print('No such record')
    else:
        for rec in chitty:
            print(rec[0], rec[1], rec[2], rec[3], rec[4], sep='\t')
    print()


def update():
    query = 'update teacher set bsal = 1.05*bsal'
    chitty.execute(query)
    print('Records updated\n')


def delete():
    code = int(input('Enter code: '))
    query = 'delete from teacher where code = {}'.format(code)
    chitty.execute(query)
    print('Record deleted\n')


print('''
1. Append more data
2. Display the teacher table
3. Display the teacher table sorted on descending bsal
4. Search for a teacher on code
5. Find teachers of a department
6. Increase bsal of every teacher by 5%
7. Delete record on code
8. Exit the menu
''')
opt = 0
while opt != 8:
    opt = int(input('Enter your option: '))
    if opt == 1:
        append()
    elif opt == 2:
        display()
    elif opt == 3:
        bsal()
    elif opt == 4:
        search()
    elif opt == 5:
        dept()
    elif opt == 6:
        update()
    elif opt == 7:
        delete()
