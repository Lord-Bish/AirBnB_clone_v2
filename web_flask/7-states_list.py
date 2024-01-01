#!/usr/bin/python3
"""script that starts a Flask web application:
must be listening on 0.0.0.0, port 5000
must use storage for fetching data from storage engine
(FileStorage or DBStorage) => from models import storage and storage.all(...)
Routes:
/states_list: display a HTML page: (inside the tag BODY)
H1 tag: 'States'
UL tag: with the list of all State objects present in DBStorage sorted
LI tag: description of one State: <state.id>: <B><state.name></B>
must use option strict_slashes=False in route definition
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """returns an HTML page with a list of all State objects in DBStorage."""
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """remove the current SQLAlchemy session."""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
