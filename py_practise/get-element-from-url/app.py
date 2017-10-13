import urllib2
import urlparse
from bs4 import BeautifulSoup
import re
import os 

url ='https://frontendfoc.us/'
response = urllib2.urlopen(url)
html = response.read()

soup = BeautifulSoup(html)
iphoneHtml = soup.find("div" , { "class": 'sideground'})

classList = []
classRegex = re.compile(r"class=[\'\"](.*?)[\'\"]")
classRes = classRegex.findall(str(iphoneHtml))
for c in classRes:
  clist = c.split()
  classList.extend(clist)
print classList

file = '''
  <link href='asdf.css' />
  <link href='SDD.css' />
'''

cssFileList = []
cssFileRegex = re.compile(r"href=[\'\"](.*?\.css)[\'\"]")
cssFileRes = cssFileRegex.findall(str(html))
cssFileAll = ''
for cssFile in cssFileRes: 
  # print cssFile
  _url = urlparse.urljoin(url, cssFile)
  cssFileContent = urllib2.urlopen(_url)
  cssFileContentHtml = cssFileContent.read()
  cssFileAll += cssFileContentHtml
  #print cssFileAll


doneClassList = []  # the class has finished regex
cssList = []
for c in classList: 
  cssRegex = re.compile(r"\n.*?\.%s.*{[\s\S]*?}"%c)
  classRes = cssRegex.findall(cssFileAll)
  # print classRes
  for cr in classRes:
    # print cr
    _match = 0
    for l in doneClassList:
      # print l, cr
      if re.search(l, cr):
        _match = 1
        break
    if _match == 0:
      cssList.append(cr)      
      
  doneClassList.append(c)


# print cssList


output = open('output.css', 'w')
for line in cssList: 
  # print line
  output.write(line)


