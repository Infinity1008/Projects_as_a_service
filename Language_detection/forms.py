from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired,Length

class Languageinput(FlaskForm):
    lang_input = StringField('Text',validators=[DataRequired(),Length(min=2)])
    submit = SubmitField('Detect')