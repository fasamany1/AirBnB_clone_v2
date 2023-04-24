#!/usr/bin/python3
"""Display "Hello HBNB!", "HBNB", and "C <text>".
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
def cText(text):
    """This function returns "C <text>" when the '/c/<text>' URL is requested.
    The underscore '_' symbols in the text variable are replaced with spaces.
    """
    return "C {}".format(escape(text.replace("_", " ")))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
