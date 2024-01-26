#!/usr/bin/python3
'''flask airbnb'''
from flask import Flask, abort

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


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False, defaults={'text': 'is_cool'})
def python_txt(text):
    '''return python is text'''
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route("/number/<n>", strict_slashes=False)
def number(n):
    '''check if n is an int'''
    try:
        int(n)
        return "{} is a number".format(n)
    except ValueError:
        abort(404)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
