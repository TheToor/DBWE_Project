from flask_login import current_user
from app.db.db import db
from app.forms.teacher import RateTeacherForm
from app.models.School import School
from app.models.TeacherRating import TeacherRating
from app.models.User import User


class TeacherController:
    def index(self, school_id):
        query = User.query.filter(User.is_teacher)
        if(school_id != 0):
            school = School.query.get_or_404(school_id)
            query = query.filter(User.schools.contains(school))
        return query.all()
    
    def get(self, id):
        return User.query.get_or_404(id)
    
    def rate(self, teacher_id, school_id, form:RateTeacherForm):
        teacher = self.get(teacher_id)
        school = School.query.get_or_404(school_id)

        existing_rating = TeacherRating.query.where(TeacherRating.school_id == school_id, TeacherRating.teacher_id == teacher_id).first()
        if existing_rating is None:
            new_rating = TeacherRating(rating=form.rating.data, comment=form.comment.data)
            new_rating.teacher = teacher
            new_rating.school = school
            new_rating.user = current_user
            db.session.add(new_rating)
        else:
            existing_rating.rating = form.rating.data
            existing_rating.comment = form.comment.data

        db.session.commit()
