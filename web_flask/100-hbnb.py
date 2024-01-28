#!/usr/bin/python3
'''stats with id'''
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def states_list():
    '''route to states_list'''
    states = storage.all("State")
    ame = storage.all("Amenity")
    return render_template('10-hbnb_filters.html', states=states, ame=ame)


@app.teardown_appcontext
def teardown(self):
    '''teardown'''
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=1)
