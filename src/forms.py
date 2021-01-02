from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from models.User import User
import email_validator

from flask_login import current_user

class RegistrationForm(FlaskForm):
    email = StringField("Email",
                        validators=[DataRequired(), Email()])
    password = PasswordField("Password",
                        validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password",
                        validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Sign Up")

class LoginForm(FlaskForm):
    email = StringField("Email",
                        validators=[DataRequired(), Email()])
    password = PasswordField("Password",
                        validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")

class UpdateProfileForm(FlaskForm):
    username = StringField("Username",
                          validators=[DataRequired(), Length(min=5, max=20)])
    email = StringField("Email",
                        validators=[DataRequired(), Email()])
    firstname = StringField("Firstname",
                            validators=[DataRequired(), Length(min=2, max=20)])
    lastname = StringField("Lastname",
                            validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField("Update")

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).fisrt()
            if user:
                raise ValidationError ("That username is taken. Please choose another name")

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')
    