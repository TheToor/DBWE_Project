from app.db.db import db
from app.forms.school.RateSchoolForm import RateSchoolForm
from app.models.SchoolRating import SchoolRating
from app.models.School import School
from flask_login import current_user

class SchoolController:
    def index(self):
        return School.query.order_by(School.name).all()
    
    def get(self, id):
        return School.query.get_or_404(id)

    def rate(self, id, form: RateSchoolForm):
        school = self.get(id)

        existing_rating = SchoolRating.query.where(SchoolRating.school_id == school.id and SchoolRating.user_id == current_user.id).first()
        if existing_rating is None:
            new_rating = SchoolRating(rating=form.rating.data, comment=form.comment.data)
            new_rating.user = current_user
            new_rating.school = school
            db.session.add(new_rating)
        else:
            existing_rating.rating = form.rating.data
            existing_rating.comment = form.comment.data

        db.session.commit()