#!/usr/bin/python3
""" A simple Flask web application that displays "Hello HBNB!" and "HBNB"
AND listen on 0.0.0.0, port 5000
"""

from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """This function returns "Hello HBNB!" when the root URL is requested."""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """This function returns "HBNB" when the '/hbnb' URL is requested."""
    return ("HBNB")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
