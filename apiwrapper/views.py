from flask import Flask, jsonify, Response
from flask_cors import CORS, cross_origin

from .PittAPI.PittAPI import course, lab, laundry

api_wrapper = Flask(__name__)
CORS(api_wrapper)


@api_wrapper.errorhandler(404)
def page_not_found(e):
    return jsonify({'error': 'invalid request'})


@api_wrapper.route('/')
def index():
    di = {'status': 'Up! Good work team'}
    print(di['status'])
    return jsonify(di)


@api_wrapper.route('/courses/<term>/<code>', strict_slashes=False)
def get_courses(term=None, code=None):
    if term is None and code is None:
        raise ValueError()

    try:
        return jsonify(course.get_courses(term, code))
    except ValueError:
        return jsonify({'error': 'Subject or term entered is invalid.'})


@api_wrapper.route('/class_description/<class_number>/<term>', strict_slashes=False)
def get_class_description(class_number=None, term=None):
    if term is None or class_number is None:
            raise ValueError()

    return jsonify(course.get_class_description(class_number, term))


@api_wrapper.route('/lab_status/<lab_name>', strict_slashes=False)
def get_lab_status(lab_name=None):
    if lab_name is None:
        raise ValueError()

    return jsonify(lab.get_status(lab_name))


@api_wrapper.route('/laundry_simple/<loc>', strict_slashes=False)
def get_laundry_status_simple(loc=None):
    if loc is None:
        raise ValueError()

    return jsonify(laundry.get_status_simple(loc))


@api_wrapper.route('/laundry_detailed/<loc>', strict_slashes=False)
def get_laundry_status_detailed(loc=None):
    if loc is None:
        raise ValueError()

    return jsonify(laundry.get_status_detailed(loc))


if __name__ is '__main__':
   api_wrapper.run(debug=True, port=8000)
