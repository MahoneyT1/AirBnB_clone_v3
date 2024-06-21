#!/usr/bin/python3
"""
The app server that serves our Flask application.
This module parses environment variables for configuration.

Environment variables:
    HBNB_API_HOST: The hostname or IP address where the app
    will run (default: '0.0.0.0')
    HBNB_API_PORT: The port where the app will run
    (default: 5000)
"""

from flask import Flask
from flask import Blueprint
import os

# get environment variables
host = os.getenv('HBNB_API_HOST')
port = os.getenv('HBNB_API_PORT')

# create the instance of flask
app = Flask(__name__)

# import some libries here to avoid circuller imports
from models import storage
from api.v1.views import app_views

# register the blueprint created
app.register_blueprint(app_views, url_prefix='/api/v1')

# connection close for any request sent
@app.teardown_appcontext
def close_c(exception=None):
    if exception:
        app.logger.error('Teardown called with exception: %s', exception)
    storage.close()

if __name__ == "__main__":
    app.run(host=host, port=port, threaded=True)
