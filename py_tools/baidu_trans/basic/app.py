# coding=utf-8

# use py -3
import http.client
import hashlib
# import md5
import urllib
import random
import requests
import json
import types  

appid = ''
secretKey = ''

 
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
myurl = myurl+'?appid='+appid+'&q='+urllib.parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
print(myurl)

try:

    httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
    httpClient.request('GET', myurl)

    response = httpClient.getresponse()
 
    print(response.read().decode("utf-8"))
    txt = response.read().decode("utf-8")
    _j = json.loads(txt)
    print(_j)
    print(type(txt))  
    print(type(_j))


finally:
    if httpClient:
        httpClient.close()