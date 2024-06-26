#!/usr/bin/python3
"""The app-server blueprint
Makes use of env to serve status ok!
"""

from flask import Flask, make_response, jsonify
from os import getenv
from flask_cors import CORS

# create an instance of flask-app
app = Flask(__name__)
cors = CORS(app, resources={
                            r"/*": {"origins": "0.0.0.0"}
                            })

from api import storage
from api.v1.views import app_views

# environment variables
app.register_blueprint(app_views)

@app.teardown_appcontext
def close_connection(exception):
    """Closes connection incase of an Exception"""

    if exception:
        storage.close()

@app.errorhandler(404)
def not_found(error):
    """In api/v1/app.py, create a handler
    for 404 errors that returns a JSON-formatted
    404 status code response. The content should
    be: "error": "Not found".
    """
    status_obj = {"error": "Not found"}
    response = make_response(jsonify(status_obj), 404)
    response.status = 200
    return response


if __name__ == "__main__":
    # check if enviroment variable was passed
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(getenv("HBNB_API_PORT", "5000"))
    app.run(host="0.0.0.0", port=5000, debug=True)
