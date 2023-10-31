#!/usr/bin/env python3
"""
set Babel’s default locale ("en") and timezone ("UTC").
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


class Config():
    """
    configure available languages in our app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_TIMEZONE = "UTC"


@app.route('/', strict_slashes=False)
def get_index() -> str:
    """
    return html doc
    """
    return render_template('1-index.html')
