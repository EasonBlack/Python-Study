# coding=utf-8


import hashlib
import urllib
import random
import requests
import json
import types  

appid = '20180206000121301'
secretKey = '3yP2yC5CNWNhHzA3UILu'

 
httpClient = None
myurl = '/api/trans/vip/translate'
q = 'hello'
fromLang = 'en'
toLang = 'zh'
salt = random.randint(32768, 65536)

sign = appid+q+str(salt)+secretKey
m1  = hashlib.md5()  
m1.update(sign.encode("utf-8"))
sign = m1.hexdigest()
baseUrl = 'https://api.fanyi.baidu.com'
myurl = baseUrl + myurl+'?appid='+appid+'&q='+urllib.parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign

print(myurl)
r = requests.get(myurl)
print(r.json())
print(r.json()["trans_result"][0]['dst'])



