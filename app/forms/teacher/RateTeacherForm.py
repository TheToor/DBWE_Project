from flask_wtf import FlaskForm
from wtforms import DecimalRangeField, TextAreaField
from wtforms.validators import DataRequired, NumberRange

class RateTeacherForm(FlaskForm):
    rating = DecimalRangeField('Rate', validators=[NumberRange(min=0, max=5)], render_kw={'step': '0.5', 'min': '0', 'max': '5'})
    comment = TextAreaField('Comment', validators=[DataRequired()])