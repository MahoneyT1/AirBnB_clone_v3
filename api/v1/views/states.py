#!/usr/bin/python3
"""view for State objects that handles all default RESTFul API actions
"""
from api.v1.views import app_views
from flask import make_response, jsonify, abort, request
from models import storage
from models.state import State
import json

maped_cls = {
    "state": State
}

@app_views.route('/states', methods=['GET'], strict_slashes=False)
def all_state():
    """List all sate object"""

    all_state = storage.all(State)
    list_of_state = []

    for state in all_state.values():
        dict_state = state.to_dict()
        list_of_state.append(dict_state)

    response = make_response(jsonify(list_of_state), 200)
    return response


@app_views.route('/states/<state_id>',
                 methods=['GET'], strict_slashes=False)
def get_state(state_id):
    """Gets state obj by id"""

    state = storage.get(State, state_id)

    if state is None:
        abort(404)

    state_json = state.to_dict()

    response = make_response(jsonify(state_json), 200)
    return response


@app_views.route('/states/<state_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_state(state_id):
    """Delete state obj"""

    state = storage.get(State, state_id)

    if state is None:
        abort(404)

    storage.delete(state)
    storage.save()

    return jsonify({}), 200


@app_views.route('/states/', methods=['POST'], strict_slashes=False)
def post_data():
    """Post data to api state"""
    data = request.get_json()

    if data is not None:
        new_state = State()

        for item, v in data.items():
            setattr(new_state, item, v)

        storage.new(new_state)
        storage.save()

        response = make_response(jsonify(new_state.to_dict()), 201)

        return response


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """Updates a state object"""

    state = storage.get(State, state_id)

    if state is None:
        abort(404)

    data = request.get_json()
    if data is None:
        abort(404, message='Not a Json')

    for k, v in data.items():
        if k in ['created_at', 'updated_at, id']:
            continue
        setattr(state, k, v)

    storage.new(state)
    storage.save()
    response = make_response(state.to_dict(), 200)
    return response
