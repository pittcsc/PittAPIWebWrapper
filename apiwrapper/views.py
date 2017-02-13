from flask import Flask, jsonify, Response
from flask_cors import CORS, cross_origin

from .PittAPI.PittAPI import course, lab, laundry

api_wrapper = Flask(__name__)
CORS(api_wrapper)


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
def get_class_description(class_number='-1', term='-1'):
    if term == '-1' or class_number == '-1':
            raise ValueError()

    return jsonify(course.get_class_description(class_number, term))


@api_wrapper.route('/lab_status/<lab_name>', strict_slashes=False)
def get_lab_status(lab_name='-1'):
    if lab_name == '-1':
        raise ValueError()

    return jsonify(lab.get_status(lab_name))


@api_wrapper.route('/laundry_simple/<loc>', strict_slashes=False)
def get_laundry_status_simple(loc='-1'):
    if loc == '-1':
        raise ValueError()

    return jsonify(laundry.get_status_simple(loc))


@api_wrapper.route('/laundry_detailed/<loc>', strict_slashes=False)
def get_laundry_status_detailed(loc='-1'):
    if loc == '-1':
        raise ValueError()

    return jsonify(laundry.get_status_detailed(loc))


if __name__ == '__main__':
   api_wrapper.run(debug=True, port=8000)
