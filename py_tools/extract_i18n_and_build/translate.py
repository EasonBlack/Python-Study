# coding=utf-8

import yaml  
import random
import requests
import hashlib
import json
import urllib

appid = ''
secretKey = ''

httpClient = None
myurl = '/api/trans/vip/translate'
fromLang = 'en'
toLang = 'zh'
salt = random.randint(32768, 65536)

baseUrl = 'http://api.fanyi.baidu.com'


def getUrl(word):
    sign = appid+word+str(salt)+secretKey
    m1  = hashlib.md5()  
    m1.update(sign.encode("utf-8"))
    sign = m1.hexdigest()
    return baseUrl + myurl+'?appid='+appid+'&q='+word+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign


f = open('message.yaml')
x = yaml.load(f)
for (d,o) in x.items():
    for k in o.keys():
        _url = getUrl(k.replace('_', ' '))
        r = requests.get(_url, headers={'Connection':'close'})
        o[k] = r.json()["trans_result"][0]['dst']
       

f = open('./translate.yaml', "w")  
yaml.dump(x, f, default_flow_style=False, allow_unicode=True)  
f.close()  
  

