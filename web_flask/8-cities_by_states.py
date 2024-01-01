#!/usr/bin/python3
"""script that starts a Flask web application:
must be listening on 0.0.0.0, port 5000
must use storage for fetching data from storage engine
(FileStorage or DBStorage) => from models import storage and storage.all(...)
After each request you must remove the current SQLAlchemy Session:
Declare a method to handle @app.teardown_appcontext
Call in this method storage.close()

Routes:
/states_list: display a HTML page: (inside the tag BODY)
H1 tag: 'States'
UL tag: with the list of all State objects present in DBStorage sorted
LI tag: description of one State: <state.id>: <B><state.name></B>
must use option strict_slashes=False in route definition
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """returns an HTML page with a list of all states and related cities."""
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
