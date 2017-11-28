import os
import json

f = open('test.json','r')
content = json.loads(f.read())
print content['a']