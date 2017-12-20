from flask import Blueprint
from flask_restful import Api

restapi_blue = Blueprint('rest_api', __name__)
rest_api = Api(restapi_blue)
