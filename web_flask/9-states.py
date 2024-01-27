#!/usr/bin/python3
'''stats with id'''
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False, defaults={"id": 1})
@app.route("/states/<id>", strict_slashes=False)
def states(id):
    '''states with ids and with none'''
    st = storage.all("State")
    name = "no"
    for stat in st.values():
        if stat.id == id:
            name = stat
    return render_template("9-states.html", st=st, id=id, name=name)


@app.teardown_appcontext
def teardown(self):
    '''teardown'''
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=1)
