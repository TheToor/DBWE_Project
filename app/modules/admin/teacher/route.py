from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import login_required

from app.models.User import User
from app.modules.school.controller import SchoolController
from .controller import TeacherController


teacher_admin_bp = Blueprint('admin_teacher', __name__)
teacher_controller = TeacherController()
school_controller = SchoolController()
@teacher_admin_bp.route('/', methods=['GET'])
def index():
    teachers = teacher_controller.index()
    return render_template("admin/teacher/index.html", teachers=teachers)

@teacher_admin_bp.route('/edit/<int:id>', methods=['GET'])
@login_required
def edit(id):
    teacher:User = teacher_controller.get(id)
    schools = school_controller.index()

    if(teacher is None or schools is None):
        return redirect(url_for('admin_teacher.index'))
    
    return render_template("admin/teacher/edit.html", teacher=teacher, schools=schools)

@teacher_admin_bp.route('/edit/<int:id>', methods=['POST'])
@login_required
def edit_post(id):
    teacher:User = teacher_controller.get(id)
    if(teacher is None):
        return redirect(url_for('admin_teacher.index'))
    
    school_selection = dict((key, request.form.getlist(key) if len(
            request.form.getlist(key)) > 1 else request.form.getlist(key)[0])
            for key in request.form.keys())
    
    teacher_controller.update_schools(id, school_selection)
    
    return redirect(url_for('admin_teacher.index'))