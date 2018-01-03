import ConfigParser
import json

cf = ConfigParser.ConfigParser()  
cf.read('app.config')

print(cf.sections())

for c in cf.sections():
    print cf.options(c)    

aa = cf.get('test', 'aa')
print(json.loads(aa))

bb = cf.get('test', 'bb')
print(json.loads(bb)[0])

cc = cf.get('test', 'cc')
print(json.loads(cc))
print(json.loads(cc)['x'])

dd = cf.get('test', 'dd')
print(dd)
