#!/usr/bin/python3
'''states_list'''
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def states_list():
    '''route to states_list'''
    st = storage.all("State")
    return render_template('8-cities_by_states.html', st=st)


@app.teardown_appcontext
def teardown(self):
    '''teardown close all'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
