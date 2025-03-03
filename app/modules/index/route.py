from http.client import HTTPException
from flask import Blueprint, app, render_template
from flask_login import login_required, current_user
from .controller import IndexController


index_bp = Blueprint('index', __name__)
index_controller = IndexController()
@index_bp.route('/', methods=['GET'])
@index_bp.route('/index', methods=['GET'])
@login_required
def index():
    return render_template("index.html", user=current_user)
