from flask import render_template, url_for, flash, redirect, request
from dash.forms import RegistrationForm, LoginForm, TaskForm
from dash import app, bcrypt
from dash.models import db, User, Task
from flask_login import login_user, logout_user, current_user
from datetime import datetime as dt


@app.route('/', methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    form = TaskForm()
    if request.method == "POST" and form.validate_on_submit():
        combined_date = dt.combine(form.date.data, form.time.data)
        task = Task(title=form.title.data, date=combined_date, content=form.contents.data, user_id=current_user.id)
        db.session.add(task)
        db.session.commit()
        flash('Task created!', 'success')
        return redirect(url_for('home'))
    if current_user.is_authenticated:
        tasks = Task.query.filter_by(user_id=current_user.id)
        return render_template('home.html', title='Home', form=form, tasks=tasks)
    return render_template('home.html', title='Home', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        pw_hash = bcrypt.generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password=pw_hash)
        db.session.add(user)
        db.session.commit()
        flash('Account created!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password ,form.password.data):
            login_user(user, remember=form.remember.data)
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash('Logout successful', 'success')
    return redirect(url_for('home'))

@app.route('/account')
def account():
    return render_template('account.html', title='Account')