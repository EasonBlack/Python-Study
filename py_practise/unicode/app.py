
# coding=utf-8

a1 = '阿斯蒂芬'
a2 = u'阿斯蒂芬'
print a1
print a2

arr1=[]
arr1.append(a2)
arr1.append(a1.decode("utf-8"))
for _arr1 in arr1:
  print _arr1 

f = open("demo.yaml", "w")
f.write("阿什顿发的发斯蒂芬")