# coding=utf-8

import time
import urllib2
import urlparse
import re


start = time.time()

reqUrl =  'https://stackoverflow.com/'
response = urllib2.urlopen(reqUrl)
html = response.read()

dictTags = {}
tagRegex = re.compile(r"<(\w+?)[\s\/>]")
tagRes = tagRegex.findall(html)
# print tagRes
for i in range(len(tagRes)):
  dictTags[tagRes[i]] = (dictTags.get(tagRes[i]) or 0) + 1

maxTag = max(dictTags.items(), key=lambda value: value[1])

end = time.time()

print end - start

print maxTag