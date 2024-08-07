#!/usr/bin/python3
"""Flask app """

from flask import Flask
from models import storage
from api.v1.views import app_views
import os
from flask_cors import CORS


# instance of flask
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

flask_host = os.getenv('HBNB_API_HOST')
f_port = int(os.getenv('HBNB_API_PORT'))

app.register_blueprint(app_views)


@app.teardown_appcontext
def close_con(exception):
    """close session"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """catches error 404"""
    return {'error': 'Not found'}, 404


if __name__ == "__main__":
    app.run(host=flask_host, port=f_port, threaded=True, debug=True)
