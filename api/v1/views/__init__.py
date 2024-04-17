from flask import Blueprint

# Create a Blueprint named 'app_views'
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Importing views modules;
# PEP8 will complain about wildcard import, but it's necessary here
from .index import *  # noqa: E402
