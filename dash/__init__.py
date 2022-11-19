from flask import Flask
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
# Configure app

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SECRET_KEY"] = "dev"

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
db.init_app(app)
migrate.init_app(app, db)


# To avoid circular import
from dash import routes