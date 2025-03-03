from flask_wtf import FlaskForm
from wtforms import EmailField, StringField
from wtforms.validators import DataRequired, Email

from app.models.School import School

class SchoolNewForm(FlaskForm):
    isNew = True

    name = StringField('Name', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    website = StringField('Website', validators=[DataRequired()])