#!/usr/bin/python3
"""
This script defines routes for the API.

It contains routes for retrieving status information and other functionalities.
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route("/status", strict_slashes=False)
def status():
    """
    Return the status of the API.

    This route returns a JSON object indicating the status of the API.
    """
    json_data = {"status": "OK"}
    return jsonify(json_data)


@app_views.route("/stats", strict_slashes=False)
def stats():
    """
    Get statistics about the API.

    - endpoint that retrieves the number of each objects by type
    """
    objs = {
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User),
    }
    return jsonify(objs)
