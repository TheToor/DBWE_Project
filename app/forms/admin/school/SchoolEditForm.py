from wtforms import HiddenField
from wtforms.validators import DataRequired

from app.forms.admin.school.SchoolNewForm import SchoolNewForm
from app.models.School import School

class SchoolEditForm(SchoolNewForm):
    isNew = False

    id = HiddenField('ID', validators=[DataRequired()])

    def set(self, school: School):
        self.id.data = school.id
        self.name.data = school.name
        self.address.data = school.address
        self.phone.data = school.phone
        self.email.data = school.email
        self.website.data = school.website