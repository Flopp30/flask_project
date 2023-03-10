import os
from pathlib import Path

from dotenv import load_dotenv

dot_env = Path(__file__).resolve().parent.parent.parent / '.env'
load_dotenv(dot_env)

SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = (os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', 'False') == 'True')
SECRET_KEY = os.getenv('SECRET_KEY')
ADMIN_EMAIL = os.getenv('ADMIN_EMAIL')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')
WTF_CSRF_ENABLED = os.getenv('WTF_CSRF_ENABLED')
