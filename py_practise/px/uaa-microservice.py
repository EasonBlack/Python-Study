

from flask import Flask, request ,redirect ,session
from flask.json import jsonify
from uuid import uuid4
import requests
import requests.auth
import urllib
import base64
import os
import json

CLIENT_ID ="login_client_id"
APP_CLIENT_ID="app_client_id"
port = int(os.getenv("PORT", 5100))
APP_URL = 'http://localhost:' + str(port)
REDIRECT_URI = "http://localhost:"+str(port)+"/callback"
UAA_URL=  ""
BASE64ENCODING = ""
APPBASE64ENCODING = "=="
ASSET_URL = ''
ASSET_ZONE_ID = ''

app = Flask(__name__)
# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/')
def home():
  if 'access_token' in session:
    print 'has session'
  else:
    print 'no session'
  print 'Calling root resource'
  text = '<br> <a href="%s">Authenticate with Predix UAA </a>'
  return 'Hello from Python microservice template!'+text % getUAAAuthorizationUrl()

@app.route('/logout')
def logout():
  print 'logout'
  if 'access_token' in session:
    session.pop('access_token',None)
  logoutUrl = UAA_URL + '/logout?redirect=' + APP_URL
  return redirect(logoutUrl)

@app.route('/secureapi')
def securepage():
    print 'securepage '
    if 'access_token' in session:
      print session['access_token']
      text = '<br> <a href="%s">Logout </a>'
      return 'This is a secure page,gated by UAA' + text % '/logout'  #logoutUrl
    else :
      text = '<br> <a href="%s">Authenticate with Predix UAA </a>'
      return 'Token not found, You are not logged in to UAA '+text % getUAAAuthorizationUrl()

@app.route('/testapi')
def testapi():
  post_data = {
		'grant_type': 'client_credentials',
		'client_id': APP_CLIENT_ID
	}
  headers =  {
		'Authorization': 'Basic ' + APPBASE64ENCODING
	}
 
  if 'client_token' in session:
    print 'already has client_token'
  else: 
    response = requests.post(UAA_URL + "/oauth/token",
                             headers=headers,
                             data=post_data)
    client_token_json = response.json()
    session['client_token'] = client_token_json['access_token']
    print 'get client_token'
  #print session['client_token']
  asset_headers =  {
		'Predix-Zone-Id': ASSET_ZONE_ID,
    'Authorization' : 'Bearer ' + session['client_token']
	}
  r = requests.get(ASSET_URL, headers=asset_headers)
  print r.json()
  return jsonify(r.json())

@app.route('/callback')
def UAAcallback():
    print 'callback '
    code = request.args.get('code')
    print code
    post_data = {"grant_type": "authorization_code",
                 "code": code,
                 "redirect_uri": REDIRECT_URI,
                 "state":"secure"
                 }
    headers =  {"Authorization": "Basic "+BASE64ENCODING }
    response = requests.post(UAA_URL+"/oauth/token",
                             headers=headers,
                             data=post_data)
    token_json = response.json()
    session['access_token'] = token_json['access_token']
    return redirect(APP_URL + "/secureapi")


def getUAAAuthorizationUrl():
  print 'uaa'
  state = 'secure'
  params = {"client_id": CLIENT_ID,
            "response_type": "code",
            "state": state,
            "redirect_uri": REDIRECT_URI
            }
  url = UAA_URL+"/oauth/authorize?" + urllib.urlencode(params)
  return url

if __name__ == '__main__':
    app.run(port=port, debug=True)