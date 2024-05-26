#!/usr/bin/python3
"""Locations endpoint"""
from api.v1.views import app_views
from flask import jsonify, abort
from models import storage


@app_views.route(
    "/locations",
    strict_slashes=False,
    methods=["GET"]
)
def get_locations():
    """Get list of all locations"""
    return jsonify(storage.all("Location"))
    

@app_views.route(
    "/cities/<int:id>",
    strict_slashes=False,
    methods=["GET"]
)
def get_location(id):
    """Get location by id or ebort 404"""
    location = storage.get("Location", id)
    if location is None:
        abort(404)
    return jsonify(location.to_dict())

@app_views.route(
    "cities/<int:id>/locations",
    strict_slashes=False,
    methods=["GET"]
)
def city_locations(id):
    """Get all locations in city by id or abort 404"""
    city = storage.get("City", id)
    if city is None:
        abort(404)
    locations = storage.dictify(city.locations)
    return jsonify(locations)
