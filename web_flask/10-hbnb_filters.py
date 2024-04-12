#!/usr/bin/python3
"""
Functions:
    app.route /hbnb_filters
Returns:
    text
"""

from flask import Flask, render_template
from models import storage
from models import Amenity, State, City

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Display a HTML page like with State and Amenities"""
    states = storage.all(State)
    amenities = storage.all(Amenity).values()
    cities = storage.all(City)
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities, cities=cities)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
