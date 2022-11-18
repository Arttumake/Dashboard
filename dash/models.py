from dash import db
from datetime import datetime as dt

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(24), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False) 
    tasks = db.relationship('Task', backref='author', lazy=True)   
    password = db.Column(db.String(60), nullable=False)
    
    def __repr__(self) -> str:
        return f"User('{self.username}', '{self.email}')"

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=dt.now())
    content = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)