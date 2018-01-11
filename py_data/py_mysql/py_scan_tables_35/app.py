import MySQLdb

import MySQLdb
db=MySQLdb.connect(passwd='root', db='demo', user='root', host='localhost')
cur=db.cursor()

cur.execute('SHOW DATABASES')
print(cur.fetchall())

cur.execute('SHOW TABLES')
# print(cur.fetchall())
tbList = []
for tb in cur.fetchall():
    tbList.append({'name': tb[0], 'col': []})
    print(tb[0])

for tb in tbList:
    cur.execute('SHOW COLUMNS FROM ' + tb["name"])
    for col in cur.fetchall():
        tb['col'].append(col[0])
        
print(tbList)

db.close()
