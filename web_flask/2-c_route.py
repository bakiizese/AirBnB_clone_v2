#!/usr/bin/python3
'''flask airbnb'''
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def root():
    '''return hello hbnb'''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    '''return hbnb'''
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    '''return text'''
    text = text.replace('_', ' ')
    return "C {}".format(text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)