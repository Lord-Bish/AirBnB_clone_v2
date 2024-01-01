#!/usr/bin/python3
"""Starts a Flask web application.
starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
You must use storage for fetching data from the storage engine
.....
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """returns main HBnB filters HTML page."""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    return render_template("100-hbnb.html",
                           states=states, amenities=amenities, places=places)


@app.teardown_appcontext
def teardown(exc):
    """Remove current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
