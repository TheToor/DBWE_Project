from typing import List
from app.db.db import db
from app.models.School import School
from app.models.User import User

class TeacherController:
    def index(self):
        return User.query.order_by(User.name).all()
    
    def get(self, id):
        return User.query.get_or_404(id)
    
    def update_schools(self, id, selection):
        teacher:User = User.query.get_or_404(id)

        teacher.schools = []
        for school_id in selection.keys():
            value = selection[school_id]
            if(value == 0):
                continue

            school = School.query.get_or_404(school_id)
            teacher.schools.append(school)

        if(len(list(teacher.schools)) == 0):
            teacher.is_teacher = False
        else:
            teacher.is_teacher = True

        db.session.commit()
