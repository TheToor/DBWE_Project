from flask import Blueprint, redirect, render_template, url_for
from flask_login import login_required

from app.forms.teacher.RateTeacherForm import RateTeacherForm
from .controller import TeacherController


teacher_bp = Blueprint('teacher', __name__)
teacher_controller = TeacherController()
@teacher_bp.route('/', methods=['GET'], defaults={'school_id': 0})
@teacher_bp.route('/<int:school_id>', methods=['GET'])
@login_required
def index(school_id):
    teachers = teacher_controller.index(school_id)
    return render_template("teacher/index.html", teachers=teachers)

@teacher_bp.route('/view/<int:teacher_id>', methods=['GET'])
@login_required
def view(teacher_id):
    teacher = teacher_controller.get(teacher_id)
    return render_template("teacher/view.html", teacher=teacher)

@teacher_bp.route('/rate/<int:teacher_id>/<int:school_id>', methods=['GET'])
@login_required
def rate(teacher_id, school_id):
    rate_teacher_form = RateTeacherForm()
    teacher = teacher_controller.get(teacher_id)
    return render_template("teacher/rate.html", form=rate_teacher_form, teacher=teacher, school_id=school_id)

@teacher_bp.route('/rate/<int:teacher_id>/<int:school_id>', methods=['POST'])
@login_required
def rate_post(teacher_id, school_id):
    rate_teacher_form = RateTeacherForm()
    if not rate_teacher_form.validate():
        return redirect(url_for('teacher.rate', teacher_id=teacher_id, school_id=school_id))
    
    teacher_controller.rate(teacher_id, school_id, rate_teacher_form)

    return redirect(url_for('teacher.index', school_id=school_id))