#!/usr/bin/python3
"""script that starts a Flask web application:
must be listening on 0.0.0.0, port 5000
Routes:
/: display Hello HBNB!
/hbnb: display HBNB
/c/<text>: display C followed by value of the text variable
(replace underscore _ symbols with a space )
must use option strict_slashes=False in route definition
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """returns 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """returns 'HBNB'."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """returns 'C' followed by value of <text>."""
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
