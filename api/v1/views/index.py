#!/usr/bin/python3
"""Create a route on the object app_view that return a JSON response"""

from . import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'])
def status():
    """Return a JSON response indicating the status is OK."""
    return jsonify(status="OK")
