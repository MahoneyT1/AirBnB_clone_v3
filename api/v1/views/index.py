from api.v1.views import app_views
from flask import jsonify

@app_views.route("/status")
def status():
    obj_to_return = {
        "status": "ok"
    }
    return jsonify(obj_to_return)
