
# Import necessary modules
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from sqlalchemy.orm import DeclarativeBase

# Import configuration settings from config.py.
from config import Config

# Define your custom base class.
class Base(DeclarativeBase):
    pass

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
db = SQLAlchemy(model_class=Base)
migrate = Migrate()
mail = Mail()

# Define a function to create the Flask application.
def create_app(config_class=Config):
    # Initialize Flask application.
    flask_app = Flask(__name__, template_folder='templates', static_folder='static')
    # Load configuration settings from the Config class.
    flask_app.config.from_object(config_class)

    db.init_app(flask_app)
    migrate.init_app(flask_app, db)
    login_manager.init_app(flask_app)
    mail.init_app(flask_app)

    return flask_app

# Import modules at the bottom to avoid circular imports
from app import models