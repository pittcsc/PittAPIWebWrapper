from flask import Flask, jsonify, Response
from flask_cors import CORS, cross_origin

from PittAPI import *

apiwrapper = Flask(__name__)
CORS(apiwrapper)

@apiwrapper.route('/')
def index():
    di = {'status': 'Up! Good work team'}
    print(di['status'])
    return jsonify(di)

@apiwrapper.route('/courses/<term>/<subject>', strict_slashes=False)
def get_courses(term='-1', subject='-1'):
    if term == '-1' or subject == '-1':
        raise InvalidParameterException()

    return jsonify(course.get_courses(term, subject))

@apiwrapper.route('/courses_by_req/<term>/<req>', strict_slashes=False)
def get_courses_by_req(term='-1', req='-1'):
    if term == '-1' or req == '-1':
        raise InvalidParameterException()

    return jsonify(course.get_courses_by_req(term, req))

@apiwrapper.route('/class_description/<class_number>/<term>', strict_slashes=False)
def get_class_description(class_number='-1', term='-1'):
    if term == '-1' or class_number == '-1':
            raise InvalidParameterException()

    return jsonify(course.get_class_description(class_number, term))

@apiwrapper.route('/lab_status/<lab_name>', strict_slashes=False)
def get_lab_status(lab_name='-1'):
    if lab_name == '-1':
        raise InvalidParameterException()

    return jsonify(labs.get_status(lab_name))

@apiwrapper.route('/laundry_simple/<loc>', strict_slashes=False)
def get_laundry_status_simple(loc='-1'):
    if loc == '-1':
        raise InvalidParameterException()

    return jsonify(laundry.get_status_simple(loc))

@apiwrapper.route('/laundry_detailed/<loc>', strict_slashes=False)
def get_laundry_status_detailed(loc='-1'):
    if loc == '-1':
        raise InvalidParameterException()

    return jsonify(laundry.get_status_detailed(loc))

if __name__ == '__main__':
  apiwrapper.run(debug=True, port=8000)
