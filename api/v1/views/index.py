#!/usr/bin/python3
"""This is the status file that returns ok
if status is 200
"""

from api.v1.views import app_views
from flask import jsonify
from flask import request, make_response


@app_views.route("/status", strict_slashes=False ,methods=["GET"])
def status_of():
    """ status route """

    status = "Ok"
    response = make_response(jsonify({"status": status}))
    response.headers['content-type'] = "application/json"


    return response