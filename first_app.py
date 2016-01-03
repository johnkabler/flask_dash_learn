from flask import Flask, render_template
import pandas as pd
import pandas.io.data as web
import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return 'This is the home page.  It does nothing.'

@app.route('/pandas_test')
def pandas_test():
    start = datetime.datetime(2008, 5, 1)
    end = datetime.datetime(2014, 8, 1)
    f = web.DataReader('F', 'google', start, end)
    return render_template('pandas.html', data=f.to_html())
    #return f.to_html()

if __name__ == '__main__':
    app.run(debug=True)
