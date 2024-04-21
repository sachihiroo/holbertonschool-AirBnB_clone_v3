#!/usr/bin/python3
"""
This script defines routes for the API.

It contains routes for retrieving status information and other functionalities.
"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route("/status", strict_slashes=False)
def status():
    """
    Return the status of the API.

    This route returns a JSON object indicating the status of the API.
    """
    json_data = {"status": "OK"}
    return jsonify(json_data)
