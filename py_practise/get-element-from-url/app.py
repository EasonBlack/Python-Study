import urllib2
import urlparse
from bs4 import BeautifulSoup
import re
import os 

url ='https://frontendfoc.us/'
response = urllib2.urlopen(url)
html = response.read()

# get html by selector
soup = BeautifulSoup(html)
iphoneHtml = soup.find("div" , { "class": 'sideground'})
outputHtml = open('output.html', 'w')
outputTemplate = '''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Demo</title>
    <link href='output.css' rel='stylesheet' />
  </head>
  <body>
   {html}
  </body>
</html>
'''
obj = {
  "html": iphoneHtml
}
outputHtml.write(outputTemplate.format(**obj))

# get sub class by selector
classList = []
classRegex = re.compile(r"class=[\'\"](.*?)[\'\"]")
classRes = classRegex.findall(str(iphoneHtml))
for c in classRes:
  clist = c.split()
  classList.extend(clist)
print classList


# get all css files
cssFileList = []
cssFileRegex = re.compile(r"href=[\'\"](.*?\.css)[\'\"]")
cssFileRes = cssFileRegex.findall(str(html))
cssFileAll = ''
for cssFile in cssFileRes: 
  _url = urlparse.urljoin(url, cssFile)
  cssFileContent = urllib2.urlopen(_url)
  cssFileContentHtml = cssFileContent.read()
  cssFileAll += cssFileContentHtml


doneClassList = []  # the class has finished regex
cssList = []
classListReString = '|'.join(classList).replace('-', '\-')
print classListReString
cssRegex = re.compile(r"\n.*?\.(?:%s).*{[\s\S]*?}"%classListReString)
cssList = cssRegex.findall(cssFileAll)


# for c in classList: 
#   cssRegex = re.compile(r"\n.*?\.%s.*{[\s\S]*?}"%c)
#   classRes = cssRegex.findall(cssFileAll)
#   # print classRes
#   for cr in classRes:
#     # print cr
#     _match = 0
#     for l in doneClassList:
#       # print l, cr
#       if re.search(l, cr):
#         _match = 1
#         break
#     if _match == 0:
#       cssList.append(cr)          
#   doneClassList.append(c)


print cssList.__len__()
output = open('output.css', 'w')
for line in cssList: 
  # print line
  output.write(line)


