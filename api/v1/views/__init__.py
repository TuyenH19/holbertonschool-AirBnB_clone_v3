#!/usr/bin/python3
"""Create a Blueprint from flask and import views module"""

from flask import Blueprint

# Create a Blueprint named 'app_views'
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Importing views modules;
# PEP8 will complain about wildcard import, but it's necessary here

# Import the route defined in all files
from .index import *  # noqa: E402
from .states import *  # noqa: E402
from .cities import *  # noqa: E402
from .amenities import *  # noqa: E402
from .users import *  # noqa: E402
from .places import *  # noqa: E402
from .places_reviews import *  # noqa: E402
