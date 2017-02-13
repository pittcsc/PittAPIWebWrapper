'''
Web Wrapper for PittAPI, web app for REST endpoints for the PittAPI
Copyright (C) 2015 Ritwik Gupta

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
'''
from flask import Flask, jsonify, Response, make_response
from flask_cors import CORS, cross_origin
from .PittAPI.PittAPI import course, lab, laundry

api_wrapper = Flask(__name__)
CORS(api_wrapper)


@api_wrapper.errorhandler(404)
def page_not_found(e):
    return make_response(jsonify({'error': 'invalid request'}), 404)


@api_wrapper.route('/')
def index():
    di = {'status': 'Up! Good work team'}
    print(di['status'])
    return jsonify(di)


@api_wrapper.route('/courses/<term>/<code>', methods=['GET'], strict_slashes=False)
@cross_origin(allow_headers=['Content-Type'])
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
