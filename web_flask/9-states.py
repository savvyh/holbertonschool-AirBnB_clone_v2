#!/usr/bin/python3
"""
Functions:
    app.route '/states/<id>'
    app.route '/states'
Returns:
    text
"""

from flask import Flask, render_template
from models import storage
from models import *

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def list_states():
    """display the states and cities listed in alphabetical order"""
    states = storage.all(State).values()
    return render_template('9-states.html', states=states, id=None)


@app.route('/states/<id>', strict_slashes=False)
def list_states_id(id):
    """display the states and cities listed in alphabetical order, with id"""
    states = storage.all(State).values()
    state = None
    for s in states:
        if s.id == id:
            state = s
            break
    return render_template('9-states.html', state=state)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage at the end of the request."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
