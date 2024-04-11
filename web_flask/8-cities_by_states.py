#!/usr/bin/python3
"""
Functions:
    app.route '/states_list'
Returns:
    text
"""

from flask import Flask, render_template
from models import storage
from models import *

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display a sorted list in alphabetical with all cities in a states"""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage at the end of the request."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
