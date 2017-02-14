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
from flask import Flask, jsonify, make_response
from flask_restful import Api, Resource
from .PittAPI.PittAPI import course, lab, laundry


app = Flask(__name__)
api = Api(app)


@app.errorhandler(404)
def page_not_found(e):
    return make_response(jsonify({'error': 'Invalid request'}), 404)


class CourseGetAPI(Resource):
    def get(self, term, code):
        try:
            return jsonify(course.get_courses(term, code))
        except ValueError:
            return jsonify({'error': 'Invalid subject or term'})


class ClassDescriptionAPI(Resource):
    def get(self, term, class_number):
        try:
            return jsonify(course.get_class_description(term, class_number))
        except ValueError:
            return jsonify({'error': 'Invalid class_number or term'})


class LabStatusAPI(Resource):
    def get(self, lab_name):
        try:
            return jsonify(lab.get_status(lab_name))
        except ValueError:
            return jsonify({'error': 'Invalid class_number or term'})


class LaundryStatusAPI(Resource):
    def get(self, location):
        try:
            return jsonify(laundry.get_status_simple(location))
        except ValueError:
            return jsonify({'error': 'Invalid class_number or term'})


class LaundryStatusDetailedAPI(Resource):
    def get(self, location):
        try:
            return jsonify(laundry.get_status_detailed(location))
        except ValueError:
            return jsonify({'error': 'Invalid class_number or term'})

api.add_resource(CourseGetAPI, '/courses/<term>/<code>')
api.add_resource(ClassDescriptionAPI, '/class_description/<class_number>/<term>')
api.add_resource(LabStatusAPI, '/lab_status/<lab_name>')
api.add_resource(LaundryStatusAPI, '/laundry_simple/<location>')
api.add_resource(LaundryStatusDetailedAPI, '/laundry_detailed/<location>')

if __name__ is '__main__':
   app.run(debug=True, port=8000)
