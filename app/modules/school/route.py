from flask import Blueprint, redirect, render_template, url_for
from flask_login import login_required

from app.forms.school.RateSchoolForm import RateSchoolForm
from .controller import SchoolController


school_bp = Blueprint('school', __name__)
school_controller = SchoolController()
@school_bp.route('/', methods=['GET'])
@login_required
def index():
    schools = school_controller.index()
    for school in schools:
        school.calculate_rating()
    
    return render_template("school/index.html", schools=schools)

@school_bp.route('/view/<int:id>', methods=['GET'])
@login_required
def view(id):
    school = school_controller.get(id)
    return render_template("school/view.html", school=school)

@school_bp.route('/rate/<int:id>', methods=['GET'])
@login_required
def rate(id):
    school = school_controller.get(id)
    school_rate_form = RateSchoolForm()
    return render_template("school/rate.html", school=school, form=school_rate_form)

@school_bp.route('/rate/<int:id>', methods=['POST'])
@login_required
def rate_post(id):
    school_rate_form = RateSchoolForm()
    if not school_rate_form.validate():
        return redirect(url_for('school.rate', id=id))
    
    school_controller.rate(id, school_rate_form)
    return redirect(url_for('school.index'))