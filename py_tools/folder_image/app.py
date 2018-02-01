from flask import Flask, render_template,request, send_file
from PIL import Image
import glob
import base64


app = Flask(__name__)



@app.route("/")
def hello():
    folderpath = 'xxxxx'
    image_list = []
 
    for filename in glob.glob( folderpath + '/*.png'): 
        im = open(filename, "rb").read()
        base = base64.b64encode(im)
        image_list.append(base)
    return render_template("index.html", image_list=image_list)


if __name__ == '__main__':
    app.run(debug=True)