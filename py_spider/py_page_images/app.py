# coding=utf-8


import urllib
import urllib2
import urlparse
import requests
import re
from bs4 import BeautifulSoup

reqUrl =  'https://codility.com/programmers/'

response = urllib2.urlopen(reqUrl)
html = response.read()
soup = BeautifulSoup(html)
fileRegex = re.compile(r"(\w*\.\w*)")
imgs = soup.select('img')
for img in imgs:
    _content = img.get('src')
    _filename = fileRegex.findall(str(_content))[0]
    # print _content, _filename
    _url = urlparse.urljoin(reqUrl, _content)
    resource = urllib2.urlopen(_url)
    output = open('files/' + _filename,"wb")
    output.write(resource.read())
    output.close()
