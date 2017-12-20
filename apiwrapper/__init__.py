from flask import Flask
from flask_cors import CORS

from apiwrapper.v0 import restapi_blue

cors = CORS()


def create_app():
    app = Flask(__name__)

    cors.init_app(app)

    app.register_blueprint(restapi_blue,
                           url_prefix='/v{version}'.format(
                               version=0))
    return app
