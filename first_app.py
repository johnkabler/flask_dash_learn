from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'This is the home page.  It does nothing.'

if __name__ == '__main__':
    app.run(debug=True)
