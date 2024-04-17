#!/usr/bin/python3

from flask import Flask
from os import getenv

# Importing storage and the app_views blueprint
from models import storage
from api.v1.views import app_views

# Create an instance of Flask
app = Flask(__name__)

# Register the blueprint
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_storage(exception):
    """ Close the storage session """
    storage.close()


if __name__ == "__main__":
    # Get host and port from environment variables, with defaults
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = getenv('HBNB_API_PORT', '5000')
    # Run the Flask app with threading enabled
    app.run(host=host, port=port, threaded=True)
