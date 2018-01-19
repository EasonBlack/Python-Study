import MySQLdb
import os


# Database:  demo
# Table:  customer
# customer.json will be created in file fold
# if without table param it will create all json from the db

p = 'Database: '
_db = raw_input(p).strip()
t = 'Tabel: '
_table = raw_input(t).strip()


db=MySQLdb.connect(passwd='root', db=_db, user='root', host='localhost')
cur=db.cursor()
row =db.cursor()

cur.execute('SHOW DATABASES')
print(cur.fetchall())

cur.execute('SHOW TABLES')

tbList = []

if(_table):
    tbList.append({'name': _table, 'col': [], 'row': []})
else: 
    for tb in cur.fetchall():
        tbList.append({'name': tb[0], 'col': [], 'row': []})
        print(tb[0])



for tb in tbList:
    n = cur.execute('SHOW COLUMNS FROM ' + tb["name"])
    cols = cur.fetchmany(n)

    row.execute('select * from ' + tb['name'])
    for col in cols:
        tb['col'].append(col[0])
    for r in row.fetchall():
        _r = {}
        for i,col in enumerate(cols):
           _r[col[0]] = str(r[i])
        tb['row'].append(_r)

print("xxxxxxxxxxxxxxxxxxxx")

if not os.path.exists('file'):
  os.makedirs('file')

for tb in tbList:
    with open("file/" + tb["name"] + '.json', 'w') as f:
        f.write("[\n")
        for row in tb["row"]:
            f.write('\t')
            f.write(str(row).replace("\'", "\"")+ ",\n" ) 
        f.write("]")
   
db.close()
