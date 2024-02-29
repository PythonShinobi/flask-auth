"This file contains configuration settings for the application."

import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

env = '.env'
load_dotenv(env)

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or \
        f'sqlite:///{os.path.join(basedir, "app.db")}'
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = int(os.getenv('MAIL_PORT') or 25)
    MAIL_USERNAME = os.getenv('ADMIN_EMAIL')
    MAIL_PASSWORD = os.getenv('ADMIN_EMAIL_PASSWORD')