#!/usr/bin/python3
"""View for City objects that handles all default
RESTFul API actions
"""
from models.city import City
from api.v1.views import app_views
from models import storage
from models.state import State
from flask import make_response, request, jsonify

@app_views.route("/states/<state_id>/cities", methods=['GET'],
                                          strict_slashes=False)
def list_of_cities(state_id):
    """Retrieves the list of all City objects of a State
    """
    list_of_cities = []
    state_city = storage.all(City)
    print(state_city)

    for key, value in state_city.items():
        list_of_cities.append(value.to_dict())
    response = make_response(jsonify(list_of_cities), 200)
    return response
