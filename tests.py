
import jwt
import pytest
from flask import current_app
from datetime import datetime, timedelta, timezone

from app import create_app
from app.models import User

@pytest.fixture
def app():
    app = create_app()  # Create a Flask application instance.
    app_context = app.app_context()  # Create an application context.
    app_context.push()  # Push the application context onto the stack
    yield app  # Provide the application to the tests.
    app_context.pop()  # Pop the application context from the stack.

@pytest.fixture
def user():
    return User(id=1, name='Test User', email='test@example.com')

def test_user_representation(user):
    assert repr(user) == 'Test User'

def test_set_password(user):
    user.set_password('password123')
    assert user.password is not None
    assert user.password != 'password123'  # Password should be hashed

def test_get_reset_password_token(app, user):
    token = user.get_reset_password_token()
    decoded_token = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
    assert decoded_token['reset_password'] == 1

def test_get_verify_email_token(app, user):
    token = user.get_verify_email_token()
    decoded_token = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
    assert decoded_token['verify_email'] == 1

def test_verify_reset_password_token_valid(app, user):
    token = jwt.encode({'reset_password': user.id, 'exp': datetime.now(timezone.utc) + timedelta(seconds=600)}, 
                       current_app.config['SECRET_KEY'], algorithm='HS256')
    verified_user = User.verify_reset_password_token(token)
    assert verified_user == user

def test_verify_reset_password_token_expired(app, user):
    token = jwt.encode({'reset_password': user.id, 'exp': datetime.now(timezone.utc) - timedelta(seconds=600)}, 
                       current_app.config['SECRET_KEY'], algorithm='HS256')
    verified_user = User.verify_reset_password_token(token)
    assert verified_user is None

def test_verify_email_token_valid(app, user):
    token = jwt.encode({'verify_email': user.id, 'exp': datetime.now(timezone.utc) + timedelta(seconds=600)}, 
                       current_app.config['SECRET_KEY'], algorithm='HS256')
    verified_user = User.verify_email_token(token)
    assert verified_user == user

def test_verify_email_token_expired(app, user):
    token = jwt.encode({'verify_email': user.id, 'exp': datetime.now(timezone.utc) - timedelta(seconds=600)}, 
                       current_app.config['SECRET_KEY'], algorithm='HS256')
    verified_user = User.verify_email_token(token)
    assert verified_user is None