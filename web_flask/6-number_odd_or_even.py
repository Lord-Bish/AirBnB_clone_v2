#!/usr/bin/python3
"""script that starts a Flask web application:
must be listening on 0.0.0.0, port 5000
Routes:
/: display Hello HBNB!
/hbnb: display HBNB
/c/<text>: display C followed by value of the text variable
/python/<text>: display Python, followed by value of text variable
(The default value of text is 'is cool')
(replace underscore _ symbols with a space for both)
/number/<n>: display 'n is a number' only if n is an integer
/number_template/<n>: display a HTML page only if n is an integer:
(H1 tag: 'Number: n' inside the tag BODY)
/number_odd_or_even/<n>: display a HTML page only if n is an integer:
(H1 tag: 'Number: n is even|odd' inside the tag BODY)
must use option strict_slashes=False in route definition
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


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


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """returns 'Python' followed by the value of <text>."""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """returns 'n is a number' only if n is an int."""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """returns an HTML page only if n is an int."""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """returns an HTML page only if n is an int."""
    return render_template("6-number_odd_or_even.html", n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
