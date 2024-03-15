from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField, validators
import email_validator
from wtforms.validators import DataRequired

class RegistrationForm(FlaskForm):
    password     = PasswordField('Password', [ validators.Length(min = 8,message= "8 characters required")])
    email        = StringField('Email Address', [validators.Email(message= "@ and . required"),validators.Length(min = 8,message= "8 characters required")])
    submit      = SubmitField("Log In")
