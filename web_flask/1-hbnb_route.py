#!/usr/bin/python3
"""
This script starts a Flask web application that listens on 0.0.0.0, port 5000.
It defines routes:
- /: displays "Hello HBNB!"
- /hbnb: displays "HBNB"
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return "HBNB"


if __name__ == "__main__":
