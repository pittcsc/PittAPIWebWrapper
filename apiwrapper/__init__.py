from flask import Flask
from flask_restful import Api
from flask_cors import CORS

cors = CORS()
restful_api = Api()

def create_app():
    app = Flask(__name__)

    cors.init_app(app)
    restful_api.init_app(app)

    from .v0 import rest_api as api_v0
    app.register_blueprint(api_v0, url_prefix='/v0')

    return app