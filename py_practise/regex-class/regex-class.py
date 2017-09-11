
import os 
from getClassFromFile import *
from getClassFromExist import * 


output = open('output.txt', 'w')

existList = getClassFromExist(os.getcwd())
classList = getClassFromFile('test.txt')
classList = [val for val in classList if val not in existList]

classList = list(sorted(set(classList)))

for line in classList: 
  str = '.%s {\n\n}\n\n' % (line)
  output.write(str)
  print line
