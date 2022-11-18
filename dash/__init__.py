from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Configure app
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SECRET_KEY"] = "dev"
db = SQLAlchemy()
db.init_app(app)

from dash import routes