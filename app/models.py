
# Import necessary modules
import jwt
from time import time
from flask import current_app
from flask_login import UserMixin
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
from werkzeug.security import generate_password_hash

# Import SQLAlchemy instance from the app module.
from app import db, login_manager

# Define the User model class.
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    # Define columns with their types and properties.
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))

    # Define a representation method for easier debugging.
    def __repr__(self) -> str:
        return f'{self.name}'
    
    def set_password(self, password):
        self.password = generate_password_hash(
            password, method='pbkdf2:sha256', salt_length=8,
        )

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode({'reset_password': self.id, 'exp': time() + expires_in},
                          current_app.config['SECRET_KEY'], algorithm='HS256')
    
    def get_verify_email_token(self, expires_in=300):
        return jwt.encode({'verify_email': self.id, 'exp': time() + expires_in},
                          current_app.config['SECRET_KEY'], algorithm='HS256')
    
    @staticmethod
    def verify_reset_password_token(token):
        """Return the user with the obtained id after decoding the token."""
        try:
            decoded_token = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            id = decoded_token['reset_password']
            # Return a user with the obtained id from the User model.
            user = db.session.get(User, id)
            return user
        except jwt.ExpiredSignatureError:
            # Token has expired
            return None
        except jwt.InvalidTokenError:
            # Token is invalid
            return None
    
    @staticmethod
    def verify_email_token(token):
        """Return the id of a user after verifying the email."""
        try:
            decoded_token = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            id = decoded_token['verify_email']
            # Return a user with the obtained id from the User model.
            user = db.session.get(User, id)
            return user
        except jwt.ExpiredSignatureError:        
            # Token has expired
            return None
        except jwt.InvalidTokenError:
            # Token is invalid
            return None
    
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)