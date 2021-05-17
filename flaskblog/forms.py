from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from email_validator import validate_email, EmailNotValidError
from flaskblog.models import User

class  RegistrationForm(FlaskForm):
    username=StringField('username', validators=[DataRequired(), Length(min=2,max=20)])
    email=StringField('email', validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired()])
    confirm_password=PasswordField('Confirm password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Sign up')

    def validate_username(self , username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('Username taken, please use another username')

    def validate_email(self , email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError('emial taken, please use another emial')

class  LoginForm(FlaskForm):
    
    email=StringField('email', validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired()])
    remember= BooleanField('Remember Me')
    submit=SubmitField('Login')