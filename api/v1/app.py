#!usr/bin/python3
""" The app-server blueprint

Makes use of env to serve status ok!
"""

from flask import Flask
from os import environ

# create an instance of flask-app
app = Flask(__name__)
from models import storage
from api.v1.views import app_views

# environment variables
host = environ.get("HBNB_API_HOST")
port = environ.get("HBNB_API_PORT")

app.register_blueprint(app_views, url_prefix="/api/v1")

@app.teardown_appcontext
def close_connection(exception):
    """Closes connection incase of an Exception"""
    if exception:
        storage.close()


if __name__ == "__main__":
    app.run(host, port, threaded=True)