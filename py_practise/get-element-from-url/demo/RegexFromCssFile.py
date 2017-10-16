import os 
import re


output = open('demo.css', 'r')
outputContent = output.read()

classString = 'marvel-device'

classRegex = re.compile(r"\n.*?\.%s.*{[\s\S]*?}"%classString)
classRes = classRegex.findall(outputContent)
print classRes