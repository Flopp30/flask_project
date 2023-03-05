import os
from pathlib import Path

from dotenv import load_dotenv

dot_env = Path(__file__).resolve().parent.parent.parent / '.env'
load_dotenv(dot_env)

SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = (os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', 'False') == 'True')
SECRET_KEY = os.getenv('SECRET_KEY')
