import urllib2
import urllib

fileName = "https://images2017.cnblogs.com/news/24442/201711/24442-20171122115835665-649671440.jpg"
#1
resource = urllib2.urlopen(fileName)
output = open("file01.jpg","wb")
output.write(resource.read())
output.close()

#2
urllib.urlretrieve(fileName, "file02.jpg")