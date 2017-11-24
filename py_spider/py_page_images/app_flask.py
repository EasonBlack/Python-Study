
import os
from flask import Flask, render_template, send_file, request
from flask.json import jsonify
from flask_cors import CORS, cross_origin

import uuid
import urllib
import urllib2
import urlparse
import requests
import re
from bs4 import BeautifulSoup


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
@cross_origin()
def index():

    reqUrl = request.args.get('url')
    print reqUrl
    req = urllib2.Request(reqUrl, headers={'User-Agent' : "Mozilla/5.0"}) 
    response = urllib2.urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html)
   
    # htmlChecker = open('files/html.txt',"wb")
    # htmlChecker.write(html)
    # htmlChecker.close()

    imgs = soup.select('img')
    print len(imgs)
    
    fileRegex = re.compile(r"(\w*\.\w*)$")
    fileList = []
    for img in imgs:
        _content = img.get('src')   
        _url = urlparse.urljoin(reqUrl, _content)
        fileList.append(_url)
    print fileList
    for img in imgs:
        _content = img.get('src')   
        _url = urlparse.urljoin(reqUrl, _content)
        _fileRes = fileRegex.findall(str(_url))
        _filename = ''
        if len(_fileRes):
            _filename = _fileRes[0]
        else:
           _filename = str(uuid.uuid4()) + '.png'

        print _url, _filename
        _urlReq = urllib2.Request(_url, headers={'User-Agent' : "Mozilla/5.0"}) 
        resource = urllib2.urlopen(_urlReq)
        output = open('files/' + _filename,"wb")
        output.write(resource.read())
        output.close()
    return 'Success!!'

if __name__ == '__main__':
    app.run(debug=True)