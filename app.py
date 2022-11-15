from flask import Flask, render_template
from forms import LoginForm, RegistrationForm


app = Flask(__name__)

app.config['SECRET_KEY'] = 'b97a0fb6e78773671b40ab10cf5133ea'

@app.route('/')
@app.route("/home")
def initial():
    return render_template('home.html', title='Home')

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)