#!/usr/bin/python3
"""Place - Amenity"""

from models import storage
from flask import Flask, make_response, abort, jsonify
from api.v1.views import app_views
from models.place import Place
from os import getenv
from models.amenity import Amenity


@app_views.route('places/<place_id>/amenities',
                 methods=['GET'], strict_slashes=False)
def place_f(place_id):
    """Get amenities """

    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    if getenv('HBNB_TYPE_STORAGE') == 'id':
        amenities = place.amenities
    else:
        amenities = [storage.get(Amenity, amenity_id) for amenity_id in place.amenity_ids]
    
    amenity_list = [amenity.to_dict() for amenity in amenities]
    response = make_response(jsonify(amenity_list), 200)
    return response
