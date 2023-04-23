#!/usr/bin/python3
""" simple Flask web application that displays "Hello HBNB!", "HBNB", "C <text>",
and "Python <text>" with default value of "is cool".
Web application listen on 0.0.0.0, port 5000
"""

from flask import Flask, escape

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """This function returns "Hello HBNB!" when the root URL is requested."""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """This function returns "HBNB" when the '/hbnb' URL is requested."""
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """ This function returns "C <text>" when the '/c/<text>' URL is requested,
with any underscores in the <text> variable replaced with spaces.
    """
    return "C {}".format(escape(text.replace("_", " ")))


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """This function returns "Python <text>" when the '/python/<text>' URL is requested,
    with any underscores in the <text> variable replaced with spaces.
    If no <text> variable is provided, the default value "is cool" is used.
    """
    return "Python {}".format(escape(text.replace("_", " ")))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
