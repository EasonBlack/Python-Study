import MySQLdb



db=MySQLdb.connect(passwd='root', db='demo', user='root', host='localhost')
cur=db.cursor()
row =db.cursor()

cur.execute('SHOW DATABASES')
print(cur.fetchall())

cur.execute('SHOW TABLES')

tbList = []
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
           _r[col[0]] = r[i]
        tb['row'].append(_r)

print(tbList)

for tb in tbList:
    with open(tb["name"] + '.json', 'w') as f:
        f.write("[\n")
        for row in tb["row"]:
            f.write(str(row).replace("\'", "\"")+ ",\n" ) 
        f.write("]")
   
db.close()
