from app.modules.teacher.route import teacher_bp
from app.modules.school.route import school_bp
from app.modules.admin.school.route import school_admin_bp
from app.modules.admin.teacher.route import teacher_admin_bp
from flask_migrate import Migrate
from app.modules.index.route import index_bp
from flask import Flask, render_template
from flasgger import Swagger
from app.db.db import db
from app.modules.user.auth.route import auth_bp


def initialize_route(app: Flask):
    with app.app_context():
        # Normal Routes
        app.register_blueprint(index_bp, url_prefix='/')
        app.register_blueprint(school_bp, url_prefix='/school')
        app.register_blueprint(teacher_bp, url_prefix='/teacher')

        # Admin Routes
        app.register_blueprint(school_admin_bp, url_prefix='/admin/school')
        app.register_blueprint(teacher_admin_bp, url_prefix='/admin/teacher')

        # Auth Routes
        app.register_blueprint(auth_bp, url_prefix="/user/auth")

        # Error handling
        app.register_error_handler(Exception, error_handler)

def error_handler(error):
    return render_template("error.html", error=error)

def initialize_db(app: Flask):
    with app.app_context():
        db.init_app(app)
        migrate = Migrate(app, db)
        db.create_all()

def initialize_swagger(app: Flask):
    with app.app_context():
        swagger = Swagger(app)
        return swagger