from flask import Flask, jsonify, Response
from pittAPI import *

apiwrapper = Flask(__name__)
course = CourseAPI()
laundry = LaundryAPI()
labs = LabAPI()

@apiwrapper.route('/courses/<term>/<subject>', strict_slashes=False)
def get_courses(term='-1', subject='-1'):
    if term == '-1' or subject == '-1':
        raise InvalidParameterException()

    return Response(str(course.get_courses(term, subject)), mimetype='application/json')

@apiwrapper.route('/courses_by_req/<term>/<req>', strict_slashes=False)
def get_courses_by_req(term='-1', req='-1'):
    if term == '-1' or req == '-1':
        raise InvalidParameterException()

    return Response(str(course.get_courses_by_req(term, req)), mimetype='application/json')

@apiwrapper.route('/class_description/<class_number>/<term>', strict_slashes=False)
def get_class_description(class_number='-1', term='-1'):
    if term == '-1' or class_number == '-1':
            raise InvalidParameterException()

    return Response(str(course.get_class_description(class_number, term)), mimetype='text/plain')

@apiwrapper.route('/lab_status/<lab_name>', strict_slashes=False)
def get_lab_status(lab_name='-1'):
    if lab_name == '-1':
        raise InvalidParameterException()

    return Response(str(labs.get_status(lab_name)), mimetype='application/json')

@apiwrapper.route('/laundry_simple/<loc>', strict_slashes=False)
def get_laundry_status_simple(loc='-1'):
    if loc == '-1':
        raise InvalidParameterException()

    return Response(str(laundry.get_status_simple(loc)), mimetype='application/json')

@apiwrapper.route('/laundry_detailed/<loc>', strict_slashes=False)
def get_laundry_status_detailed(loc='-1'):
    if loc == '-1':
        raise InvalidParameterException()

    return Response(str(laundry.get_status_detailed(loc)), mimetype='application/json')
