#!/usr/bin/python3
"""Cities endpoint"""
from api.v1.views import app_views
from flask import jsonify, abort
from models import storage


@app_views.route(
    "/images",
    strict_slashes=False,
    methods=["GET"]
)
def get_images():
    """Get list of all images"""
    return jsonify(storage.all("Image"))
    

@app_views.route(
    "/images/<int:id>",
    strict_slashes=False,
    methods=["GET"]
)
def get_image(id):
    """Get image by id or ebort 404"""
    image = storage.get("Image", id)
    if image is None:
        abort(404)
    return jsonify(image.to_dict())


@app_views.route(
    "/items/<int:id>/images/",
    strict_slashes=False,
    methods=["GET"]
)
def item_images(id):
    """Get all driver's images by id of driver or ebort 404"""
    item = storage.get("Item", id)
    if item is None:
        abort(404)
    images = storage.dictify(item.images)
    return jsonify(images)


@app_views.route(
    "/vehicles/<int:id>/images/",
    strict_slashes=False,
    methods=["GET"]
)
def vehicle_images(id):
    """Get all vehicle's images by id of vehicle or abort 404"""
    vehicle = storage.get("Vehicle", id)
    if vehicle is None:
        abort(404)
    images = storage.dictify(vehicle.images)
    return jsonify(images)
