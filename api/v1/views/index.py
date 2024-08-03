#!/usr/bin/python3
"""Index view"""
from api.v1.views import app_views
from flask import make_response, jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Deplays the status of the api"""

    return make_response({'status': "ok"}, 200)
