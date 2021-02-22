from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Length, Email
from werkzeug.utils import secure_filename


class ContactForm(FlaskForm):
    name = StringField('name', validators=[InputRequired(), Length(max=70)])
    email = EmailField('email', validators=[Email(), InputRequired(), Length(max=80)])
    subject = StringField('subject', validators=[InputRequired(), Length(max=70)])
    message = TextAreaField('message', validators=[InputRequired(), Length(max=80)])

