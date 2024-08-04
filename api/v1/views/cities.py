#!/usr/bin/python3
"""City view"""

from api.v1.views import app_views
from flask import Flask, make_response, abort, request
from models import storage
from models.state import State
from models.city import City


@app_views.route('/states/<state_id>/cities', methods=['GET'],
                 strict_slashes=False)
def city_list(state_id):
    """List of city objects"""

    data_state = storage.get(State, state_id)
    if data_state is None:
        abort(404)
    city = data_state.cities

    response = make_response(city, 200)
    return response


@app_views.route('/cities/<city_id>', methods=['GET'],
                 strict_slashes=False)
def cities(city_id):
    """Get city obj"""
    city = storage.get(City, city_id)

    if city is None:
        abort(404)
    response = make_response(city.to_dict(), city_id)
    return response


@app_views.route('/cities/<city_id>', methods=['GET'],
                 strict_slashes=False)
def delete_city(city_id):
    """Deletes a particular"""

    city = storage.get(City, city_id)

    if city is None:
        abort(404)

    storage.delete(city)
    storage.save()

    response = make_response({}, 200)
    return response


@app_views.route('states/<state_id>/cities', methods=['POST'],
                 strict_slashes=False)
def post_city(state_id):
    """Posts data and updates in obj"""
    data = request.get_json()    
    state = storage.get(State, state_id)

    if state is None:
        abort(404)
    
    if data is None:
        abort(404, message='Not a Json')

    city = state.cities
    if not 'name' in data:
        abort(404, messages='Missing name')

    if city:
        for k, v in data.items():
            setattr(city, k, v)

        response = make_response(state, 200)
        return response


@app_views.route('cities/<city_id>', methods=['PUT'],
                 strict_slashes=False)
def put_city(city_id):
    """Updates an instance with new values"""

    city = storage.get(City, city_id)
    data = request.get_json()

    if data is None:
        abort(400, message='Not a JSON')
    
    for k, v in data.items():
        if k in ['id', 'state_id', 'created_at', 'updated_at']:
            continue
        setattr(city, k, v)
    storage.new(city)
    storage.save()

    response = make_response(city.to_dict(), 200)
    return response
