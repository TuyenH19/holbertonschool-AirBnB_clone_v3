#!/usr/bin/python3
"""Create a route on the object app_view that return a JSON response"""

from . import app_views
from flask import request, jsonify, abort
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'])
def get_states():
    """Retrieve the list of all State objects"""
    all_states = storage.all(State).values()
    return jsonify([state.to_dict() for state in all_states])


@app_views.route('/states/<state_id>', methods=['GET'])
def get_state(state_id):
    """Retrieve a specific State object base on state_id"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    """Delete a specific State object"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    storage.delete(state)
    return jsonify({}), 200  # Return empty dictionary with the status code 200


@app_views.route('/states', methods=['POST'])
def create_state():
    """Create a state"""
    req_data = request.get_json()
    if not req_data:
        abort(400, description="Not a JSON")
    if 'name' not in req_data:
        abort(400, description="Missing name")
    new_state = State(**req_data)
    storage.new(new_state)
    storage.save()
    return jsonify(new_state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'])
def update_state(state_id):
    """ Updates a State object """
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    req_data = request.get_json()
    if not req_data:
        abort(400, description="Not a JSON")
    for key, value in req_data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(state, key, value)
    storage.save()
    return jsonify(state.to_dict()), 200
