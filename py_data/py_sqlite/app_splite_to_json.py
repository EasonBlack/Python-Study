

import sqlite3
import json

cx = sqlite3.connect("test.db")
cu=cx.cursor()

langs = ['cn', 'us']
for lan in langs:
    f = open('{0}.json'.format(lan),'w')
    cu.execute("select name, {0} from languages".format(lan)) 
    f.write('{\n')
    for t in cu.fetchall():
        # f.write("   \"{0}\":\"{1}\",\n".format(t[0], t[1]))   # py 3
        f.write("   \"{0}\":\"{1}\",\n".format(t[0], t[1].encode('utf-8')))   # py 2
    f.write('}')
    f.close()
