# coding=utf-8


import hashlib
import urllib
import random
import requests
import json
import types  

appid = ''
secretKey = ''

 
httpClient = None
myurl = '/api/trans/vip/translate'
q = 'hello world'
fromLang = 'en'
toLang = 'zh'
salt = random.randint(32768, 65536)

sign = appid+q+str(salt)+secretKey
m1  = hashlib.md5()  
m1.update(sign.encode("utf-8"))
sign = m1.hexdigest()
baseUrl = 'http://api.fanyi.baidu.com'
myurl = baseUrl + myurl+'?appid='+appid+'&q='+urllib.parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign

print(myurl)
r = requests.get(myurl, headers={'Connection':'close'})
print(r.headers)
print(r.json())
print(r.json()["trans_result"][0]['dst'])



