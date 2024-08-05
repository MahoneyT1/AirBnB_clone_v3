#!/usr/bin/python3
"""User Views"""

from api.v1.views import app_views
from flask import request, abort, make_response, jsonify
from models import storage
from models.user import User


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def list_user():
    """List the list of users"""

    user_list = []

    users = storage.all(User)
    for user in users:
        user_list.append(user.to_dict())
    
    response = make_response(jsonify(user_list), 200)
    return response


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """Get user by Id"""

    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    
    return make_response(jsonify(user), 200)


@app_views.route('/users/<user_id>', methods=['GET'],
                 strict_slashes=False)
def user_delete(user_id):
    """Deletes an obj by id"""

    user_del = storage.get(User, user_id)
    if user_del is None:
        abort(400)
    storage.delete(user_del)
    storage.save()

    response = make_response({}, 200)
    return response


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_post():
    """Create Post"""

    data = request.get_json()
    if data is None:
        abort(400, message='Not a JSON')
    if not 'email' in data:
        abort(400, message='Missing email')
    if not 'password' in data:
        abort(400, message='Missing password')
        
        