#!/usr/bin/python3
"""Create a route on the object app_view that return a JSON response"""
from . import app_views
from flask import request, jsonify, abort
from models import storage
from models.state import State
from models.city import City


@app_views.route('/states/<state_id>/cities', methods=['GET'],
                 strict_slashes=False)
def get_cities(state_id):
    """Retrieve the list of all City objects of a State object"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    cities = [city.to_dict() for city in state.cities]
    return jsonify(cities)


@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def get_city(city_id):
    """Retrieve a specific City object base on city_id"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    return jsonify(city.to_dict())


@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
def delete_city(city_id):
    """Delete a specific City object"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    try:
        storage.delete(city)
        storage.save()
        return jsonify({}), 200
    except Exception as e:
        # Log the exception details
        app_views.logger.error(f"Error deleting state: {e}")
        abort(500, description="Internal Server Error")


@app_views.route('/states/<state_id>/cities', methods=['POST'],
                 strict_slashes=False)
def create_city(state_id):
    """Create a city object base on state_id"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    # Retrieve request body as JSON
    city_data = request.get_json()
    if not city_data:
        abort(400, description="Not a JSON")
    if 'name' not in city_data:
        abort(400, description="Missing name")
    # Create new City instance
    new_city = City(name=city_data['name'], state_id=state_id)
    storage.new(new_city)
    storage.save()
    return jsonify(new_city.to_dict()), 201


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def update_city(city_id):
    """ Updates a City object """
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    req_data = request.get_json()
    if not req_data:
        abort(400, description="Not a JSON")
    for key, value in req_data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(city, key, value)
    storage.save()
    return jsonify(city.to_dict()), 200
