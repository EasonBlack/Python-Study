# coding=utf-8

import urllib2
import urlparse
from bs4 import BeautifulSoup

import MySQLdb
db=MySQLdb.connect(passwd='root', db='demo', user='root', host='localhost')
c=db.cursor()

reqUrl =  'https://github.com/search?p=%s&q=vue&type=Repositories'
reqCount = 3

print reqUrl % (1, )
vals = []
for num in range(1,reqCount + 1):
  theUrl = reqUrl % (num,)
  response = urllib2.urlopen(theUrl)
  html = response.read()
  soup = BeautifulSoup(html)
  links = soup.select('.repo-list .repo-list-item h3 a')
  for link in links:
    vals.append((link.get_text(),))
   
print vals

com = "insert into demo.store (title) VALUES (%s)"
c.executemany(com, vals)

print 'the process is over!'
db.commit()
db.close()
