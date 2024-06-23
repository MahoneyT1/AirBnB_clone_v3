#!/usr/bin/python3
"""This is the status file that returns ok
if status is 200
"""

from api.v1.views import app_views
from flask import jsonify

@app_views.route("/status")
def status():
    """ status route """
    obj_to_return = {
        "status": "ok"
    }
    return jsonify(obj_to_return)