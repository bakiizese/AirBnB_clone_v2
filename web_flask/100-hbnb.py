#!/usr/bin/python3
'''stats with id'''
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnbs():
    '''route to whole airbnb'''
    states = storage.all("State")
    ame = storage.all("Amenity")
    place = storage.all("Place")
    user = storage.all("User")
    return render_template('100-hbnb.html', states=states, ame=ame, place=place, user=user)


@app.teardown_appcontext
def teardown(self):
    '''teardown'''
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=1)
