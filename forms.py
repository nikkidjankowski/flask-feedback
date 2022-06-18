"""Forms for flask-feedback."""

from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, NumberRange, Email, Optional
from flask_wtf import FlaskForm



class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email(), Length(max=50)])
    username = StringField("Username", validators=[
                       InputRequired(message="Username can't be blank"), Length(min=1, max=20)])
    password = PasswordField("Password", validators=[InputRequired(message="password can't be blank"), Length(min=6, max=55)])
    first_name = StringField("First Name",  validators=[
                       InputRequired(message="First Name can't be blank"), Length(max=30)])
    last_name = StringField("First Name",  validators=[
                       InputRequired(message="Last Name can't be blank"), Length(max=30)])
   

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[
                       InputRequired(message="Username can't be blank"), Length(min=1, max=20)])
    password = PasswordField("Password", validators=[InputRequired(message="password can't be blank"), Length(min=6, max=55)])
    