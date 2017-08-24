from flask import Flask, render_template, send_file
import pandas as pd
from pandas import  DataFrame
from altair import datasets, Chart
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/fig')
def fig():
    data = pd.DataFrame({'a': [21, 17, 14, 31, 12, 36, 48, 24, 7],
                         'b': [2, 7, 4, 1, 2, 6, 8, 4, 7]})
    data.plot.scatter(x='a', y='b');
    plt.savefig('pic.png', size=(300, 300))
    return send_file('pic.png', mimetype='image/png')


@app.route("/")
def hello():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()