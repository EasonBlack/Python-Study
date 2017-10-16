# coding=utf-8


import os 
import re


string1 = '''.marvel-device .bottom-bar { asdfasdf asdfasfd asdf }
  .top-bar {asdfadsf}
'''

string2 = '''
  .contained {
    max-width: 780px;
    margin: 0 auto;
    padding-left: 12px;
    padding-right: 12px; }
'''

array1 = ['marvel-device', 'top-bar']
arrayregex1 = "|".join(array1).replace('-', '\-')
print arrayregex1

# 阿斯蒂芬
# regex1 = re.compile(r"\.(?:marvel\-device|top\-bar).*{[\s\S]*?}")
regex1 = re.compile(r"\.(?:%s).*{[\s\S]*?}"%arrayregex1)
result1 = regex1.findall(string1)
print result1

result2 = regex1.findall(string2)
print result2