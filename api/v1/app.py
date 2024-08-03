#!/usr/bin/python3
"""Flask app """

from flask import Flask
from models import storage
from api.v1.views import app_views
import os

# instance of flask
app = Flask(__name__)


flask_host = os.getenv('HBNB_API_HOST')
f_port = os.getenv('HBNB_API_PORT')

app.register_blueprint(app_views)


@app.teardown_appcontext
def close_con(exception):
    """close session"""
    storage.close()


if __name__ == "__main__":
    app.run(host=flask_host, port=f_port, threaded=True, debug=True)
