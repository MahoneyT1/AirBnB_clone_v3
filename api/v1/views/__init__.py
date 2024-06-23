#!/usr/bin/python3
"""File that instantiates the blueprint
of a custom route
"""

from flask import Blueprint

app_views = Blueprint("app_views", __name__)
from api.v1.views.index import *