
import os
from flask import Flask, render_template, send_file
from flask.json import jsonify
from fun import *

app = Flask(__name__)

@app.template_filter('autoversion')
def autoversion_filter_func(filename):
    return autoversion_filter(filename)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/info/<path>")
def getFolders(path):
    arr = list_files(path)
    return arr

if __name__ == '__main__':
    app.run(debug=True)