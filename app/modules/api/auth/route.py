from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token

from app.modules.user.auth.controller import AuthenticationController


auth_api_bp = Blueprint('auth_api', __name__)
auth_controller = AuthenticationController()
@auth_api_bp.route('/login', methods=['POST'])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    user = auth_controller.login(username, password)

    if user is None:
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)
      