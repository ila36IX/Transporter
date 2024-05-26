#!/usr/bin/python3
"""Cities endpoint"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage


@app_views.route(
    "/cities",
    strict_slashes=False,
    methods=["GET"]
)
def get_cities():
    """Get list of all cities if q parmater doesn't included
    Searching in cities by names using a prefix
    The query should be included with the argument q
    """
    q = request.args.get("q")
    if not q:
        return jsonify(storage.all("City"))
    cities = storage.starts_with("City", "name", q)
    return jsonify(cities)
    

@app_views.route(
    "/cities/<int:id>",
    strict_slashes=False,
    methods=["GET"]
)
def get_city(id):
    """Get city by id or ebort 404"""
    city = storage.get("City", id)
    if city is None:
        abort(404)
    return jsonify(city.to_dict())
