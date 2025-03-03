from app.db.db import db
from app.forms.admin.school.SchoolEditForm import SchoolEditForm
from app.forms.admin.school.SchoolNewForm import SchoolNewForm
from app.models.School import School
from app.modules.school.controller import SchoolController


class SchoolAdminController(SchoolController):    
    def update(self, id, form: SchoolEditForm):
        school = self.get(id)
        school.name = form.name.data
        school.address = form.address.data
        school.phone = form.phone.data
        school.email = form.email.data
        school.website = form.website.data

        db.session.commit()

    def new(self, form: SchoolNewForm):
        school = School()
        school.name = form.name.data
        school.address = form.address.data
        school.phone = form.phone.data
        school.email = form.email.data
        school.website = form.website.data

        db.session.add(school)
        db.session.commit()

    def delete(self, id):
        school = self.get(id)
        db.session.delete(school)
        db.session.commit()
        
