#!/usr/bin/env python3
"""
flask app that has a rout of / and return an html template
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def get_index() -> str:
    """
    return html index html template
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
