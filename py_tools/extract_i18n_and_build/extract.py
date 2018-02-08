
import os
import re
import yaml  

pathList = []
pathList.append({"title":'1:All Path', "index":1})
pathListIndex = 2
for dirpath,_,filenames in os.walk('./components'):
    pathList.append({ "title": "{0}:{1}".format(pathListIndex, dirpath), "index": pathListIndex, "path": dirpath})
    pathListIndex += 1
for _path in pathList :
    print _path["title"]


# select path from the list
selectIndex =  raw_input("please select the path you want to exract i18n: ")
selectPath = ''
if selectIndex == "1":
    selectPath = './components'
else:
    selectPath = [x["path"] for x in pathList if str(x["index"]) == str(selectIndex)][0]

# get all vue files from the path
files = []
for dirpath,_,filenames in  os.walk(selectPath):
    for name in filenames:
        if name.endswith('.vue'):
            _file = {
                'name':name, 
                'dirpath' :dirpath
            }
            files.append(_file)




keys={}
for _file in files:
    vue = open(_file['dirpath'] +'/' + _file['name']).read()
    result = re.findall(r'(<.*i18n.*</.*>)',vue)
    _fileKey = _file['dirpath'] +'/' + _file['name']
    print result
    _paramKey = {}
    for _r in result:      
        # param = re.findall(r'>(.*)<', _r)
        param = re.findall(r'[>}]([^{}].*?)[<{]', _r)
        print param
        for _p in param:
            _param = _p.strip().replace(' ', '_')
            _paramKey[_param] = ''
        
    keys[_fileKey] = _paramKey

# print keys
f = open('./message.yaml', "w")  
yaml.dump(keys, f, default_flow_style=False)  
f.close()  

print '* Finish *'


