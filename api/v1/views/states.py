from models.base_model import BaseModel
from flask import make_response, jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.state import State

@app_views.route("/states", methods=['GET'], strict_slashes=False)
def check_status():
    """retrieves the list of state object
    """
    # fetch all the data of state from database
    all_data = storage.all(State)

    new_list = []

    for v in all_data.values():
        new_list.append(v.to_dict())

    response = make_response(jsonify(new_list), 200)
    return response


@app_views.route("states/<state_id>", methods=['GET', 'DELETE'], strict_slashes=False)
def get_state_by_id(state_id):
    """Gets the state by id
    """
    if request.method == 'GET':
        # Get the state from the storage
        state = storage.get(State, state_id)
        # Check if the return result is None
        if state is None:
            abort(404)
        json_state = state.to_dict()
        response = make_response(json_state, 200)
        return response
    
    elif request.method == 'DELETE':
        """Deletes state class by Id
        """
        state_to_delete = storage.get(State, state_id)
        print(state_to_delete)
        
        if state_to_delete is None:
            abort(404)
        storage.delete(state_to_delete)
        storage.save()
        return make_response(jsonify({}), 200)



# @app_views.route("/states/<state_id>", methods=['DELETE'], strict_slashes=False)
# def delete_class_by_id(state_id):
#     """Deletes state class by Id
#     """
#     state_to_delete = storage.get(State, state_id)
#     print(state_to_delete)
#     if state_to_delete is None:
#         abort(404)
#     storage.delete(state_to_delete)
#     storage.save()
#     return make_response(jsonify({}), 200)
