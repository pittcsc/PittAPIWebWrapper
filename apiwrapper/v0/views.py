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
from flask import  make_response
from flask_restful import Resource
from apiwrapper.PittAPI.PittAPI import course, lab, laundry, people, shuttle, textbook, news
from apiwrapper.v0 import rest_api
import json


@rest_api.representation('application/json')
def output_json(data, code, headers=None):
    """Makes a Flask response with a JSON encoded body"""
    resp = make_response(json.dumps(data), code)
    resp.headers.extend(headers or {})
    return resp


@rest_api.errorhandler(404)
def page_not_found(e):
    return output_json({'error': 'Invalid request'}, 404)


class CourseGetAPI(Resource):
    def get(self, term, code):
        try:
            return course.get_courses(term, code)
        except Exception as e:
            return {'error': str(e)}


class ClassAPI(Resource):
    def get(self, term, class_number):
        try:
            return course.get_class(term, class_number)
        except Exception as e:
            return {'error': str(e)}


class LabStatusAPI(Resource):
    def get(self, lab_name):
        try:
            return lab.get_status(lab_name)
        except Exception as e:
            return {'error': str(e)}


class LaundryStatusAPI(Resource):
    def get(self, location):
        try:
            return laundry.get_status_simple(location)
        except Exception as e:
            return {'error': str(e)}


class LaundryStatusDetailedAPI(Resource):
    def get(self, location):
        try:
            return laundry.get_status_detailed(location)
        except Exception as e:
            return {'error': str(e)}


class PeopleAPI(Resource):
    def get(self, query):
        try:
            return people.get_person(query)
        except Exception as e:
            return {'error': str(e)}


class TextbookAPI(Resource):
    def get(self, department_code, course_name, instructor, term):
        try:
            return textbook.get_books_data([{'department_code': department_code, 'course_name': course_name, 'instructor': instructor, 'term': term}])
        except Exception as e:
            return {'error': str(e)}


class TextbookNoTermAPI(Resource):
    def get(self, department_code, course_name, instructor, term='2600'):
        try:
            return textbook.get_books_data([{'department_code': department_code, 'course_name': course_name, 'instructor': instructor, 'term': term}])
        except Exception as e:
            return {'error': str(e)}


class ShuttleRoutesAPI(Resource):
    def get(self):
        try:
            return shuttle.get_routes()
        except Exception as e:
            return {'error': str(e)}


class ShuttleVehiclePointsAPI(Resource):
    def get(self):
        try:
            return shuttle.get_map_vehicle_points()
        except Exception as e:
            return {'error': str(e)}


class ShuttleStopArrivalsAPI(Resource):
    def get(self, times_per_stop=1):
        try:
            return shuttle.get_route_stop_arrivals("8882812681",times_per_stop)
        except Exception as e:
            return {'error': str(e)}


class ShuttleStopEstimatesAPI(Resource):
    def get(self, vehicle_id, quantity=2):
        try:
            return shuttle.get_vehicle_route_stop_estimates(vehicle_id, quantity)
        except Exception as e:
            return {'error': str(e)}


class NewsAPI(Resource):
    def get(self, feed, max_news_items):
        try:
            max_news_items = int(max_news_items)
            return news.get_news(feed, max_news_items)
        except Exception as e:
            return {'error': str(e)}


rest_api.add_resource(CourseGetAPI, '/courses/<term>/<code>')
rest_api.add_resource(ClassAPI, '/class/<class_number>/<term>')
rest_api.add_resource(LabStatusAPI, '/lab_status/<lab_name>')
rest_api.add_resource(LaundryStatusAPI, '/laundry/simple/<location>')
rest_api.add_resource(LaundryStatusDetailedAPI, '/laundry/detailed/<location>')
rest_api.add_resource(PeopleAPI, '/people/<query>')
rest_api.add_resource(ShuttleRoutesAPI, '/shuttle/routes')
rest_api.add_resource(ShuttleVehiclePointsAPI, '/shuttle/points')
rest_api.add_resource(ShuttleStopArrivalsAPI, '/shuttle/arrivals/<times_per_stop>')
rest_api.add_resource(ShuttleStopEstimatesAPI, '/shuttle/estimates/<vehicle_id>/<quantity>')
rest_api.add_resource(TextbookAPI, '/textbook/<department_code>/<course_name>/<instructor>/<term>')
rest_api.add_resource(TextbookNoTermAPI, '/textbook/<department_code>/<course_name>/<instructor>/')
rest_api.add_resource(NewsAPI, '/news/<feed>/<max_news_items>')
