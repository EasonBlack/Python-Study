
import os
import re
import yaml  

files = []
for dirpath,_,filenames in  os.walk('./components'):
    for name in filenames:
        if name.endswith('.vue'):
            _file = {
                'name':name, 
                'dirpath' :dirpath
            }
            files.append(_file)

print files

keys={}
for _file in files:
    vue = open(_file['dirpath'] +'/' + _file['name']).read()
    result = re.findall(r'(<.*i18n.*</.*>)',vue)
    for _r in result:
        key = re.findall(r'>(.*)<', _r)
        _key = key[0].replace(' ', '_')

        keys[_key]=''

print keys
f = open('./message.yaml', "w")  
yaml.dump(keys, f, default_flow_style=False)  
f.close()  


