#!/usr/bin/python3
"""Create a new view for State objects that
handles all default RESTFul API actions
"""
from models.base_model import BaseModel
from api.v1.views import app_views
from models import storage
from flask import jsonify, make_response, abort
from models.state import State

@app_views.route("/states/<state_id>", methods=['GET'], strict_slashes=False)
def state_get(state_id):
    """Retrieves the list of all State objects
    GET /api/v1/states
    """




 

# @app_views.route("/states/<state_id>",
#                             strict_slashes=False,
#                             methods=['DELETE'])
# def delete_state(state_id):
#     """Deletes a State object:: DELETE /api/v1/
#     states/<state_id>

#     If the state_id is not linked to any State object,
#     raise a 404 error

#     Returns an empty dictionary with the status code 200
#     """
#     obj_to_delete = storage.all(State)

#     for key, value in obj_to_delete.items():
#         state_name, state_idd = key.split('.')
#         if state_idd == state_id:
#             delete_them = {state_name:value}
#             storage.delete(delete_them)

#             response = make_response(jsonify({"status": "ok"}))
#             return response
#         else:
#             abort(404)
