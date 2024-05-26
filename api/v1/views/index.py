#!/usr/bin/python3
"""index file"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route("/status", strict_slashes=False)
def attain_status():
    """Give a user a way to make sure the api is working perfectly"""
    return jsonify(status='OK')

@app_views.route("/stats", strict_slashes=False)
def stats():
    """Get the amount the records of every model"""
    status = {
        "cities" : storage.count("City"),
        "images" : storage.count("Image"),
        "locations": storage.count("Location"),
        "users": storage.count("User"),
        "customers": storage.count("Customer"),
        "vehicles": storage.count("Vehicle"),
        "drivers": storage.count("Driver"),
        "deliveries": storage.count("Delivery"),
        "items": storage.count("Item"),
        "ratings": storage.count("Rating")
    }
    return jsonify(status)
