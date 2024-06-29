#!/usr/bin/python3
"""Create a new view for State objects that
handles all default RESTFul API actions
"""
from models.base_model import BaseModel
from api.v1.views import app_views
from models import storage
from flask import jsonify, make_response, abort
from models.state import State

@app_views.route("/states", methods=['GET'], strict_slashes=False)
def state_get():
    """Retrieves the list of all State objects
    GET /api/v1/states
    """

    # create a list to extract list of all states in
    list_of_states = []
    # get the copy of States from storage
    all_data = storage.all(State)

    for key, value in all_data.items():
        list_of_states.append({key:value.to_dict()})

    # construct a response
    response = make_response(jsonify(list_of_states), 200)
    return response

@app_views.route("/states/<state_id>",  methods=["GET"], strict_slashes=False)
def state_by_id(state_id):
    """
    gets a specific State object by ID
    :param state_id: state object id
    :return: state obj with the specified id or error
    """
    # using the get method of db_storage
    # and extract the state and id
    fetched_obj = storage.get(State, state_id)

    obj = fetched_obj
    # using the make_reponse of flask to generate a response
    obj_b = make_response(jsonify(obj), 200)

    return obj

@app_views.route("/states/<state_id>", methods=['DELETE'], strict_slashes=False)
def delete_cls_by_id(state_id):
    """deletes a class if id matches any in db
    """
    state = storage.get(State, state_id)
    #del storage.all()[state]
    bbb = state

    storage.delete(bbb)
    storage.save()

   # return jsonify({})

