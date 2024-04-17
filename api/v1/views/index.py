#!/usr/bin/python3
"""Create a route on the object app_view that return a JSON response"""

from . import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status', methods=['GET'])
def status():
    """Return a JSON response indicating the status is OK."""
    return jsonify(status="OK")


@app_views.route('/stats', methods=['GET'])
def count():
    """Retrieve the number of each objects by type"""
    object_counts = {
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User)
    }
    return jsonify(object_counts)
