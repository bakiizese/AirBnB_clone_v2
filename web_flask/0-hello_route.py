#!/usr/bin/python3
'''tyring flask'''
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def root():
    '''this is to return helloe hbnb'''
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
