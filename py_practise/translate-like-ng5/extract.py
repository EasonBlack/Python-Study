
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

# print files

keys={}
for _file in files:
    vue = open(_file['dirpath'] +'/' + _file['name']).read()
    result = re.findall(r'(<.*i18n.*</.*>)',vue)
    _fileKey = _file['dirpath'] +'/' + _file['name']

    for _r in result:
        _paramKey = {}
        param = re.findall(r'>(.*)<', _r)
        _param = param[0].replace(' ', '_')
        _paramKey[_param] = ''
        
    keys[_fileKey] = _paramKey

# print keys
f = open('./message.yaml', "w")  
yaml.dump(keys, f, default_flow_style=False)  
f.close()  


