
import os
import re
import yaml 


f = open('message.yaml')
msgDict = yaml.load(f)



def _matchKey(matched):
    print(matched)
    print(matched.groups()[0])
    return 'aaaa'


for (_file, msgs) in msgDict.items():

    vue = open(_file).read()  
    resultVue = vue
   
    _targetFile = _file.replace('components', 'target')
    _path = os.path.dirname(_targetFile) 
    if not os.path.exists(_path):
        os.makedirs(_path)

    for msgKey, msgValue in msgs.items():
        realMsg = msgKey.replace('_', ' ')
        resultVue = re.sub(r'(<.*?i18n.*?>)(' + realMsg +')(?=</.*>)', r'\1' +msgValue, resultVue)
        # resultVue = re.sub(r'(?:<.*i18n.*>)(?P<key>' + realMsg +')(?=</.*>)', msgValue, resultVue)
        # print(realMsg, msgValue)
        # print(resultVue)
    f = open(_targetFile, "w")
    f.write(resultVue)
    f.close()  






