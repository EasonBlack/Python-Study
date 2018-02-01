from flask import Flask, render_template,request, send_file
from flask.json import jsonify
from PIL import Image
import glob
import base64


app = Flask(__name__)

types = ('*.png', '*.jpg')

@app.route("/all")
def getall():
    folderpath = request.args.get('path')
    files_grabbed = []
    for files in types:
        files_grabbed.extend(glob.glob(folderpath + '/' + files))
    # folderpath = 'C:/Users/Eason/Desktop/blead UI'
    image_list = []
    print('start get pic')
    for filename in files_grabbed: 
        im = open(filename, "rb").read()
        base = base64.b64encode(im)
        image_list.append('data:image/png;base64,'+str(base)[2:-1])
    print(len(image_list))
    return jsonify(image_list)


@app.route("/")
def hello():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)