#!/usr/bin/python3
"""script that starts a Flask web application
must be listening on 0.0.0.0, port 5000
Routes: /: display Hello HBNB!
must use option strict_slashes=False in route definition
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """returns Hello HBNB!"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
