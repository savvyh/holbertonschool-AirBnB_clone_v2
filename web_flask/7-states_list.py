#!/usr/bin/python3
"""
Functions:
    app.route '/states_list'
Returns:
    text
"""

from flask import Flask, render_template
from models import storage
from models import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a sorted list in alphabetical order with all states"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage at the end of the request."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
