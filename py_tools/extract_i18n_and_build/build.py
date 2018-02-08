# coding=utf-8

import os
import re
import yaml 


f = open('translate.yaml')
msgDict = yaml.load(f)


for (_file, msgs) in msgDict.items():

    vue = open(_file).read()  
    resultVue = vue
   
    _targetFile = _file.replace('components', 'target')
    _path = os.path.dirname(_targetFile) 
    if not os.path.exists(_path):
        os.makedirs(_path)

    for msgKey, msgValue in msgs.items():
        realMsg = msgKey.replace('_', ' ')
        # resultVue = re.sub(r'(<.*?i18n.*?>)(' + realMsg +')(?=</.*>)', r'\1' +msgValue, resultVue)
        resultVue = re.sub(r'(<.*?i18n.*?>)(.*?)('+ realMsg +')(.*?)(?=</.*>)',
     lambda m: m.group(1) +  m.group(2) +msgValue + m.group(4),   resultVue)
        # print resultVue
    
    resultVue = resultVue.encode('utf-8')
    f = open(_targetFile, "w")
    f.write(resultVue)
    f.close()  







