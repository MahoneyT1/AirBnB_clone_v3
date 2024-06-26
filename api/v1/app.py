#!/usr/bin/python3
"""The app-server blueprint
Makes use of env to serve status ok!
"""

from flask import Flask
from os import getenv
from flask_cors import CORS

# create an instance of flask-app
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

from api import storage
from api.v1.views import app_views

# environment variables
app.register_blueprint(app_views)

@app.teardown_appcontext
def close_connection(exception):
    """Closes connection incase of an Exception"""
    if exception:
        storage.close()


if __name__ == "__main__":
    # check if enviroment variable was passed
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(getenv("HBNB_API_PORT", "5000"))
    app.run(host="0.0.0.0", port=5050, debug=True)
