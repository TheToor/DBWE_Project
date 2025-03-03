from flask import Flask, jsonify, make_response
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from app.config.config import get_config_by_name
from app.initialize_functions import initialize_route, initialize_db, initialize_swagger
from flask_login import LoginManager

from app.models.User import User

def create_app(config=None) -> Flask:
    """
    Create a Flask application.

    Args:
        config: The configuration object to use.

    Returns:
        A Flask application instance.
    """
    app = Flask(__name__)
    if config:
        app.config.from_object(get_config_by_name(config))

    # Initialize extensions
    initialize_db(app)

    # Register blueprints
    initialize_route(app)

    # Initialize Swagger
    initialize_swagger(app)

    bcrypt = Bcrypt(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    jwt = JWTManager(app)

    @jwt.unauthorized_loader
    def my_invalid_token_callback(expired_token):
        return make_response(jsonify(message='Missing Authorization Header'), 401)

    return app
