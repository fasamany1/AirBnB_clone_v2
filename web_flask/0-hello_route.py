#!/usr/bin/python3
"""A simple web Flask application that displays "Hello HBNB!
and listen on 0.0.0.0, port 5000
"""

from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """This function returns "Hello HBNB!" when the root URL is requested."""
    return ("Hello HBNB!")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
