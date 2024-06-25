#!/usr/bin/python3
"""This is the status file that returns ok
if status is 200
"""

from api.v1.views import app_views
from flask import jsonify
from flask import request, make_response
from models import storage
from models import user, city, place, amenity, review, state


@app_views.route("/status", strict_slashes=False,
                 methods=["GET"])
def status_of():
    """ status route """

    status = "Ok"
    response = make_response(jsonify({"status": status}))
    response.headers['content-type'] = "application/json"

    return response

@app_views.route("/api/v1/stats", strict_slashes=False,
                 methods=['GET'])
def stats_check():
    """ populates the statistics """
    all_obj = {"User": storage.count(user.User),
               "Place": storage.count(place.Place),
               "State": storage.count(state.State),
               "Review": storage.count(review.Review),
               "Amenity": storage.count(amenity.Amenity),
               "City": storage.count(city.City)
               }
    response = make_response(jsonify(all_obj))
    return response