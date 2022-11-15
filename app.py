from flask import Flask, render_template, flash, redirect, url_for
from forms import LoginForm, RegistrationForm


app = Flask(__name__)

app.config['SECRET_KEY'] = 'b97a0fb6e78773671b40ab10cf5133ea'

@app.route('/')
@app.route("/home")
def home():
    return render_template('home.html', title='Home')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)