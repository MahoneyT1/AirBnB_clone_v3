#!/usr/bin/python3
"""place review"""

from api.v1.views import app_views
from flask import make_response, abort, request, jsonify
from models import storage
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User



@app_views.route('places/<place_id>/reviews', methods=['GET'], strict_slashes=False)
def place_review(place_id):
    """Place review view"""

    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    review = place.reviews

    response = make_response(jsonify(review), 200)
    return response


@app_views.route('reviews/review_id', methods=['GET'], strict_slashes=False)
def review_place(review_id):
    """Review place"""

    review = storage.get(Review, review_id)
    if review is None:
        abort(404)

    response = make_response(jsonify(review), 200)
    return response


@app_views.route('reviews/review_id', methods=['GET'], strict_slashes=False)
def review_del(review_id):
    """Review delete"""

    review = storage.get(Review, review_id)
    if review is None:
        abort(404)

    storage.delete(review)
    storage.save()

    return make_response({}, 200)


@app_views.route('places/<place_id>/reviews', methods=['POST'], strict_slashes=False)
def review_post(place_id):
    """Post review"""

    data = request.get_json()
    if data is None:
        abort(400, messages='Not a Json')

    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    user_id = data.get('user_id')

    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    if 'text' not in data:
        abort(400, message='Not a Json')

    new_review_post = Review()

    for k, v in data.items():
        setattr(new_review_post, k, v)

    storage.new(new_review_post)
    storage.save()

    response = make_response(jsonify(new_review_post), 201)
    return response


@app_views.route('reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def update_review(review_id):
    """updates the """

    data = request.get_json()
    if data is None:
        abort(400, 'Not a Json')

    review = storage.get(Review, review_id)

    for k, v in data:
        if k in ['id', 'user_id', 'place_id', 'created_at', 'updated_at']:
            continue
        setattr(review, k, v)
    storage.save()

    response = make_response(jsonify(review), 200)
    return response
