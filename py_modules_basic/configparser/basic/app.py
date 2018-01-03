import ConfigParser
import json

cf = ConfigParser.ConfigParser()  
cf.read('app.config')

print(cf.sections())

for c in cf.sections():
    print cf.options(c)    

cc = cf.get('test', 'cc')
print(json.loads(cc))
print(json.loads(cc)['x'])