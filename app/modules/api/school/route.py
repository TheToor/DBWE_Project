from flask import Blueprint, make_response, jsonify
from flask_jwt_extended import jwt_required

from app.modules.school.controller import SchoolController


school_api_bp = Blueprint('school_api', __name__)
school_controller = SchoolController()
@school_api_bp.route('/', methods=['GET'])
@jwt_required()
def get():
    schools = school_controller.index()
    for school in schools:
        school.calculate_rating()
    return make_response(jsonify(data=schools), 200)

@school_api_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_id(id):
    school = school_controller.get(id)
    school.calculate_rating()
    return make_response(jsonify(data=school), 200)

@school_api_bp.route('/<int:id>/ratings', methods=['GET'])
@jwt_required()
def get_id_rating(id):
    school = school_controller.get(id)
    return make_response(jsonify(data=school.ratings), 200)