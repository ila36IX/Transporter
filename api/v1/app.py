from models import storage
from api.v1.views import app_views
from flask_cors import CORS
from flask import Flask, Blueprint, jsonify

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

@app.teardown_appcontext
def teardown_app(exception):
    """This used to keep always the data up to date:
    The session that created by SQLAchemy is always keeping a connection that
    is isolated to other possible existing connections. Here we forced it to
    return to the connection pool within the Engine, ensuring that every
    changes made by other pools are reloaded
    """
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """handeling not found page (error 404)"""
    response = jsonify({"error": "Not found"})
    response.status_code = 404
    return response


if __name__ == "__main__":
    API_HOST = storage.get_vars()[4]
    API_PORT = storage.get_vars()[5]
    print(f"API({API_HOST}:{API_PORT}) OK")
    app.run(host=API_HOST, port=API_PORT, threaded=True)
