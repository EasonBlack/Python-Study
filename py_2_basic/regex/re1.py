
# coding=utf-8

import re



keys =[ {"name": "hello", "result": "你好"},  {"name": "world" , "result": "世界"}]
resultHtml = 'aaaa<div i18n>hello world</div>bbbb'

for key in keys:
    _key = key["name"]
    _result = key["result"]
    _result = _result.decode('utf-8').encode('gbk')
  
    resultHtml = re.sub(r'(<.*?i18n.*?>)(.*?)('+ _key +')(.*?)(?=</.*>)',
     lambda m: m.group(1) +  m.group(2) +_result + m.group(4),   resultHtml)
print resultHtml