#!/usr/bin/python3
"""File that instantiates the blueprint
of a custom route
"""

from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views import state
