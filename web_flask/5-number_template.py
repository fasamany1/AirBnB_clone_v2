#!/usr/bin/python3
"""This is a simple Flask web application that displays "Hello HBNB!", "HBNB", "C <text>",
"Python <text>" with default value of "is cool", and "n is a number".
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ This function returns "Hello HBNB!" when the root URL is requested."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """This function returns "HBNB" when the '/hbnb' URL is requested."""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """This function returns "C <text>" when the '/c/<text>' URL is requested,
    with any underscores in the <text> variable replaced with spaces.
    """
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """display Python followed by the value of the text variable"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def is_Number(n):
    """display “n is a number” only if n is an integer"""
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n=None):
    """display a HTML page only if n is an integer"""
    if isinstance(n, int):
        return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run()
