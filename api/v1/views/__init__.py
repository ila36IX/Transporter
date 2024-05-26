from flask import Blueprint

app_views = Blueprint("app_routes", __name__, url_prefix='/api/v1')
from api.v1.views.index import *
from api.v1.views.cities import *
from api.v1.views.locations import *
from api.v1.views.users import *
from api.v1.views.images import *
