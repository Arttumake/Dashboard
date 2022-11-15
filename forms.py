from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, PasswordField, BooleanField
from wtforms.validators import Length, Email, InputRequired, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=3, max=16)])
    email = EmailField('Email', validators=[InputRequired(),Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    confirm_password = PasswordField('Password', validators=[InputRequired(), EqualTo("password")])
    submit = SubmitField('Sign up')
    
class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[InputRequired(),Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign in')    
    