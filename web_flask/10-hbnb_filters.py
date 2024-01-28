#!/usr/bin/python3
'''stats with id'''
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb():
    '''real airbnb'''
    return render_template('10-hbnb_filters.html')

@app.route("/")
def trys():
    return "Hello bakii"


@app.teardown_appcontext
def teardown(self):
    '''teardown'''
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=1)
