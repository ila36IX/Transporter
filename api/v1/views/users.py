#!/usr/bin/python3
"""users endpoint"""
from api.v1.views import app_views
from flask import jsonify, abort
from models import storage


@app_views.route(
    "/users",
    strict_slashes=False,
    methods=["GET"]
)
def get_users():
    """Get list of all users"""
    return jsonify(storage.all("User"))
    

@app_views.route(
    "/users/<int:id>",
    strict_slashes=False,
    methods=["GET"]
)
def get_user(id):
    """Get user by id or ebort 404"""
    user = storage.get("User", id)
    if user is None:
        abort(404)
    d = user.to_dict()
    d["avatar"] = user.image.img_url
    return jsonify(d)
