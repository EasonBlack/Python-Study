import re
import os 

def getClassFromFile(filePath):
  classList = []
  classRegex = re.compile(r"class=[\'\"](.*?)[\'\"]")
  tabRegex = re.compile(r"^\s{2,}")
  lines = open(filePath).readlines()
  for line in lines:
    classRes = classRegex.findall(line)
    tabRes = tabRegex.findall(line)
    if(classRes.__len__()):
      for classSingle in classRes: 
        if(classSingle.split().__len__() > 1):
          classList.extend(classSingle.split())
        else:
          classList.append(classSingle)
  return classList