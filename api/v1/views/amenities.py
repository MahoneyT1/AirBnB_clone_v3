#!/usr/bin/python3
"""The amenities view"""

from api.v1.views import app_views
from flask import make_response, abort, request, jsonify
from models import storage
from models.amenity import Amenity


@app_views.route('/amenities', methods='GET', strict_slashes=False)
def get_amenity():
    """List all amenity"""

    new_list = []
    amenity = storage.all(Amenity)
    if amenity is None:
        abort(404)
    
    for each_state in amenity.items():
        new_list.append(each_state.to_dict())

    response = make_response(jsonify(new_list), 200)
    return response

@app_views.route('/amenities/<amenity_id>', methods=['GET'], strict_slashes=False)
def amenity_ob(amenity_id):
    """Gets an obj with an Id"""

    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)

    response = make_response(jsonify(amenity), 200)
    return response


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'], strict_slashes=False)
def amenities_del(amenity_id):
    """Gets amenity my id"""

    amenity_to_del = storage.new(Amenity, amenity_id)

    if amenity_to_del is None:
        abort(404)

    storage.delete(amenities_del)
    storage.save()

    response = make_response({}, 200)
    return response


@app_views.route('/amenities/', methods=['POST'], strict_slashes=False)
def amenity_post():
    """Handles post request"""
    data = request.get_json()

    if data is None:
        abort(404, message='Not a JSON')

    if 'name' in data:
        abort(404, message='Missing name')
    
    new_amenity = Amenity(**data)
    storage.new(new_amenity)
    storage.save()
    response = make_response(new_amenity, 201)
    return response
    

@app_views.route('/amenities/<amenity_id>', methods=['PUT'], strict_slashes=False)
def amenity_put(amenity_id):
    """Updates amenities"""

    amenity = storage.get(Amenity, amenity_id)
    data = request.get_json()

    if amenity is None:
        abort(404)
    
    if data is None:
        abort(400, 'Not a Json')
    
    for k, v in data.items():
        setattr(amenity, k, v)
    storage.new(amenity)
    storage.save()

    response = make_response(jsonify(amenity.to_dict()), 200)
    return response






