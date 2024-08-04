#!/usr/bin/python3
"""Index view"""
from api.v1.views import app_views
from flask import make_response, jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Deplays the status of the api"""

    return make_response({'status': "ok"}, 200)


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """Create an endpoint that retrieves the number of each objects by type
    """

    all_obj = {
        'amenities': storage.count(Amenity),
        'cities': storage.count(City),
        'places': storage.count(Place),
        'reviews': storage.count(Review),
        'states': storage.count(State),
        'user': storage.count(User)
    }

    response = make_response(jsonify(all_obj), 200)
    return response



