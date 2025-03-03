from flask import Blueprint, redirect, render_template, url_for
from flask_login import login_required, current_user
from functools import wraps

from app.forms.admin.school.SchoolEditForm import SchoolEditForm
from app.forms.admin.school.SchoolNewForm import SchoolNewForm
from .controller import SchoolAdminController


school_admin_bp = Blueprint('admin_school', __name__)
school_controller = SchoolAdminController()

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_admin:
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

@school_admin_bp.route('/', methods=['GET'])
@school_admin_bp.route('/index', methods=['GET'])
@login_required
@admin_required
def index():
    schools = school_controller.index()
    return render_template("admin/school/index.html", schools=schools)

@school_admin_bp.route('/edit/<int:id>', methods=['GET'])
@login_required
@admin_required
def edit(id):
    school_edit_form = SchoolEditForm()
    school_edit_form.set(school_controller.get(id))
    return render_template("admin/school/edit.html", form=school_edit_form)

@school_admin_bp.route('/edit/<int:id>', methods=['POST'])
@login_required
@admin_required
def edit_post(id):
    school_edit_form = SchoolEditForm()
    if not school_edit_form.validate():
        return redirect(url_for('admin_school.edit', id=id))
    
    school_controller.update(id, school_edit_form)

    return redirect(url_for('admin_school.index'))

@school_admin_bp.route('/new', methods=['GET'])
@login_required
@admin_required
def new():
    school_new_form = SchoolNewForm()
    return render_template("admin/school/edit.html", form=school_new_form)

@school_admin_bp.route('/new', methods=['POST'])
@login_required
@admin_required
def new_post():
    school_new_form = SchoolNewForm()
    if not school_new_form.validate():
        return redirect(url_for('admin_school.new'))
    
    school_controller.new(school_new_form)

    return redirect(url_for('admin_school.index'))

@school_admin_bp.route('/delete/<int:id>', methods=['POST'])
@login_required
@admin_required
def delete_post(id):
    school_controller.delete(id)

    return redirect(url_for('admin_school.index'))