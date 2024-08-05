#!/usr/bin/python3
"""The Place View"""

from api.v1.views import app_views
from flask import make_response, abort, request, jsonify
from models import storage
from models.city import City
from models.place import Place


@app_views.route('cities/<city_id>/places',
                 methods=['GET'], strict_slashes=False)
def city_place(city_id):
    """City place"""

    city = storage.get(City, city_id)
    if city is None:
        abort(404)

    list_of_place = city.places
    response = make_response(jsonify(list_of_place), 200)
    return response


@app_views.route('places/<place_id>',
                 methods=['GET'], strict_slashes=False)
def place_obj(place_id):
    """Gets a lace obj"""

    place = storage.get(Place, place_id)

    if place is None:
        abort(404)

    response = make_response(jsonify(place), 200)
    return response


@app_views.route('places/<place_id>',
                 methods=['GET'], strict_slashes=False)
def delete_place(place_id):
    """Deletean obj by Id"""

    place_del = storage.get(Place, place_id)

    if place_id is None:
        abort(404)

    storage.delete(place_del)
    storage.save()

    response = make_response({}, 200)
    return response


@app_views.route('cities/<city_id>',
                 methods=['POST'], strict_slashes=False)
def post_place(city_id):
    """creates a new place obj"""

    city = storage.get(City, city_id)
    if city is None:
        abort()

    data = request.get_json()
    if data is None:
        abort(400, 'Not a Json')

    place = city.places

    if place is None:
        abort(400, message='Missing user_id')

    if 'name' not in data:
        abort(400, message='Not a Json')

    new_place = Place()

    for k, v in data.items():
        setattr(new_place, k, v)

    storage.new(new_place)
    storage.save()

    response = make_response(jsonify(new_place.to_dict()), 201)
    return response


@app_views.route('places/<place_id>', methods=['POST'],
                 strict_slashes=False)
def put_place(place_id):
    """Puts place obj"""

    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    data = request.get_json()

    if data is None:
        abort(404, 'Not a JSON')

    new_place = Place()

    for k, v in data.items():
        if k in ['id', 'user_id', 'city_id', 'created_at', 'updated_at']:
            setattr(new_place, k, v)

    storage.new(new_place)
    storage.save()

    response = make_response(jsonify(new_place), 200)
    return response
