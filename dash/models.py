from datetime import datetime as dt
from flask_login import UserMixin
from dash import login_manager, db

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(24), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False) 
    tasks = db.relationship('Task', backref='author', lazy=True)   
    password = db.Column(db.String(60), nullable=False)
    
    def __repr__(self) -> str:
        return f"User ('{self.username}', '{self.email}')"

class Task(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=dt.now())
    content = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self) -> str:
        return f"'{self.title}' date: {self.date} by id: {self.user_id}'"