#!/usr/bin/python3
"""
API Blueprint .

entry point for the Flask application.
"""
from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
from api.v1.views.index import *
from api.v1.views.states import *
