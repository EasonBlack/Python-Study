
import os
from flask import Flask, render_template, send_file, request
from flask.json import jsonify
from flask_cors import CORS, cross_origin

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
    # output = open('files/aaa.txt',"wb")
    # output.write('asdafs')
    # output.close()

    reqUrl = request.args.get('url')
    print reqUrl
    response = urllib2.urlopen(reqUrl)
    html = response.read()
    soup = BeautifulSoup(html)
    fileRegex = re.compile(r"(\w*\.\w*)$")
    imgs = soup.select('img')
    for img in imgs:
        _content = img.get('src')   
        _url = urlparse.urljoin(reqUrl, _content)
        _filename = fileRegex.findall(str(_url))[0]
        print _url, _filename
        resource = urllib2.urlopen(_url)
        output = open('files/' + _filename,"wb")
        output.write(resource.read())
        output.close()
    return 'Success!!'

if __name__ == '__main__':
    app.run(debug=True)