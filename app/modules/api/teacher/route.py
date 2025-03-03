from flask import Blueprint, make_response, jsonify
from flask_jwt_extended import jwt_required
from app.modules.teacher.controller import TeacherController

teacher_api_bp = Blueprint('teacher_api', __name__)
teacher_controller = TeacherController()
@teacher_api_bp.route('/', methods=['GET'])
@jwt_required()
def get():
    teachers = teacher_controller.index()
    return make_response(jsonify(data=teachers))

@teacher_api_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_id(id):
    teacher = teacher_controller.get(id)
    return make_response(jsonify(data=teacher))

@teacher_api_bp.route('/<int:id>/ratings', methods=['GET'])
@jwt_required()
def get_id_ratings(id):
    teacher = teacher_controller.get(id)
    return make_response(jsonify(data=teacher.my_teacher_ratings))