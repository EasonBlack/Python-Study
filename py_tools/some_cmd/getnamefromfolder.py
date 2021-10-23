import os
import re

someRegex =re.compile(r"(.*).jpg")


for  f in os.listdir("/Users/eason/Downloads/ddd"):
  a = someRegex.findall(f)
  b = re.match(r"(.*).jpg", f)
  print(b.group(1))
  print(a)
