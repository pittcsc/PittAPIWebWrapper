"""
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
"""
import inspect
import sys

from flask_restful import Resource

from apiwrapper.PittAPI.PittAPI import course, lab, laundry, people, shuttle, textbook, news


class CourseGet(Resource):
    PATH = '/courses/<term>/<code>'

    def get(self, term, code):
        try:
            return course.get_courses(term, code)
        except Exception as e:
            return {'error': str(e)}


class Class(Resource):
    PATH = '/class/<class_number>/<term>'

    def get(self, term, class_number):
        try:
            return course.get_class(term, class_number)
        except Exception as e:
            return {'error': str(e)}


class LabStatus(Resource):
    PATH = '/lab_status/<lab_name>'

    def get(self, lab_name):
        try:
            return lab.get_status(lab_name)
        except Exception as e:
            return {'error': str(e)}


class LaundryStatus(Resource):
    PATH = '/laundry/simple/<location>'

    def get(self, location):
        try:
            return laundry.get_status_simple(location)
        except Exception as e:
            return {'error': str(e)}


class LaundryStatusDetailed(Resource):
    PATH = '/laundry/detailed/<location>'

    def get(self, location):
        try:
            return laundry.get_status_detailed(location)
        except Exception as e:
            return {'error': str(e)}


class People(Resource):
    PATH = '/people/<query>'

    def get(self, query):
        try:
            return people.get_person(query)
        except Exception as e:
            return {'error': str(e)}


class Textbook(Resource):
    PATH = '/textbook/<department_code>/<course_name>/<instructor>/<term>'

    def get(self, department_code, course_name, instructor, term):
        try:
            return textbook.get_books_data([{'department_code': department_code, 'course_name': course_name,
                                             'instructor': instructor, 'term': term}])
        except Exception as e:
            return {'error': str(e)}


class ShuttleRoutes(Resource):
    PATH = '/shuttle/routes'

    def get(self):
        try:
            return shuttle.get_routes()
        except Exception as e:
            return {'error': str(e)}


class ShuttleVehiclePoints(Resource):
    PATH = '/shuttle/points'

    def get(self):
        try:
            return shuttle.get_map_vehicle_points()
        except Exception as e:
            return {'error': str(e)}


class ShuttleStopArrivals(Resource):
    PATH = '/shuttle/arrivals/<times_per_stop>'

    def get(self, times_per_stop=1):
        try:
            return shuttle.get_route_stop_arrivals("8882812681", times_per_stop)
        except Exception as e:
            return {'error': str(e)}


class ShuttleStopEstimates(Resource):
    PATH = '/shuttle/estimates/<vehicle_id>/<quantity>'

    def get(self, vehicle_id, quantity=2):
        try:
            return shuttle.get_vehicle_route_stop_estimates(vehicle_id, quantity)
        except Exception as e:
            return {'error': str(e)}


class News(Resource):
    PATH = '/news/<feed>/<max_news_items>'

    def get(self, feed, max_news_items):
        try:
            max_news_items = int(max_news_items)
            return news.get_news(feed, max_news_items)
        except Exception as e:
            return {'error': str(e)}


def add_resources():
    from apiwrapper.v0 import rest_api
    clsmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    clsmembers = [cls[1] for cls in clsmembers if cls[0] != 'Resource']
    for cls in clsmembers:
        rest_api.add_resource(cls, cls.PATH)
