from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, PasswordField, BooleanField, TextAreaField, DateField, TimeField
from wtforms.validators import Length, Email, DataRequired, EqualTo, ValidationError
from dash.models import User
from datetime import datetime as dt

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=16)])
    email = EmailField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField('Sign up')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('User name is already taken')
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That Email is already associated with an account')        
    
class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign in')
    
class TaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=40)])
    date = DateField('Date', validators=[DataRequired()], format='%Y-%m-%d', default=dt.now())
    time = TimeField('Time', validators=[DataRequired()], default=dt.now())
    contents = TextAreaField('Task Description', validators=[Length(max=120)])
    