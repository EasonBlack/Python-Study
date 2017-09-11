import re
import os

def getClassFromExist(path):
  classList = []
  for obj in os.walk(path):
    strFiles = ','.join(obj[2])
    cssFiles = re.findall(r'([\w]*\.css),', strFiles)
    for file in cssFiles:
      content = open(file).read()
      result = re.findall(r'.([\w]*)\s{1,}\{',content)
      classList.extend(result)
  return classList