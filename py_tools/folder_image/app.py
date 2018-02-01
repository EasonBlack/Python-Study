from flask import Flask, render_template,request, send_file
from PIL import Image
import glob
import base64
import cStringIO


imgFolder = "d:/testnpm"


app = Flask(__name__)



@app.route("/")
def hello():
    return render_template("index.html")


@app.route('/folder')
def getall():

    folderpath = request.args.get('path')

    image_list = []
    for filename in glob.glob( folderpath + '/*.png'): 
        im = open(filename, "rb").read()
        base = base64.b64encode(im)
        image_list.append(base)
        print 'xxxx'
        # print image_list
    return render_template("index.html", image_list=image_list)

if __name__ == '__main__':
    app.run(debug=True)