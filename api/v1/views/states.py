#!/usr/bin/python3
"""Create a new view for State objects that
handles all default RESTFul API actions
"""
from models.base_model import BaseModel
from api.v1 import app, app_views
from models import storage
from flask import jsonify, make_response, abort
from models.state import State

@app_views.route("/states", methods=['GET'], strict_slashes=False)
def state_get():
    """Retrieves the list of all State objects
    GET /api/v1/states
    """
    # object to extract information from the
    # storage in dict form
    new_obj = {}
    list_of_states = []

    # loop through values and extract
    # using the to_dict method of BaseModel
    for value in storage.all(State).values():
        list_of_states.append(value.to_dict())

    # using the make_response method and customise
    # a response

    response = make_response(jsonify(list_of_states), 200)
    return response

string_uri = "/states/<state_id>"
@app_views.route(string_uri, methods=['GET'], strict_slashes=False)
def get_state_id(state_id):
    """Retrieves a State object: GET /api/v1/states
    /<state_id>
    """
    # using the get method of db storage, extract State
    # by state_id
    state_obj = storage.get(State, state_id)

    # check if state_obj is None and return 404
    if state_obj is None:
        abort(404)
    else:
        response = make_response(jsonify(state_obj), 200)
        return response

@app_views.route("/api/v1/states/<int:state_id>",
                            strict_slashes=False,
                            methods=['DELETE'])
def delete_state(state_id):
    """Deletes a State object:: DELETE /api/v1/
    states/<state_id>

    If the state_id is not linked to any State object,
    raise a 404 error

    Returns an empty dictionary with the status code 200
    """
    obj_to_delete = storage.all(State)

    for key, value in obj_to_delete.items():
        state_name, state_idd = key.split('.')
        if state_idd == state_id:
            delete_them = {state_name:value}
            storage.delete(delete_them)

            response = make_response(jsonify({"status": "ok"}))
            return response
        else:
            abort(404)
