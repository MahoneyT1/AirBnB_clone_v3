"""
Summary or Description of the Function
Parameters:
  argument1 (int): Description of arg1
Returns:
  int: Returning value.
"""
from api.v1.views import app_views
from dotenv import load_dotenv
from models import storage
import os
from flask import Flask

load_dotenv()
# get environment variables
host = os.getenv('HBNB_API_HOST')
port = os.getenv('HBNB_API_PORT')

# create the instance of flask
app = Flask(__name__)

# import some libries here to avoid circuller imports
app.register_blueprint(app_views, url_prefix='/api/v1')

# connection close for any request sent
@app.teardown_appcontext
def close_c(exception=None):
    """ all of the avove"""
    if exception:
      app.logger.error('Teardown called with exception: %s',
                        exception)
    storage.close()


if __name__ == "__main__":
  app.run(host=host, port=port, threaded=True)