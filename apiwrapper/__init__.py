from flask import Flask
from flask_cors import CORS

cors = CORS()


def create_app():
    app = Flask(__name__)

    cors.init_app(app)

    from .v0 import restapi_blue
    app.register_blueprint(restapi_blue)

    return app