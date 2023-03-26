import os
from pathlib import Path

from dotenv import load_dotenv

dot_env = Path(__file__).resolve().parent.parent.parent / '.env'
load_dotenv(dot_env)

# Data base
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = (os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', 'False') == 'True')

# Flask setup
SECRET_KEY = os.getenv('SECRET_KEY')
ADMIN_EMAIL = os.getenv('ADMIN_EMAIL')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')
WTF_CSRF_ENABLED = os.getenv('WTF_CSRF_ENABLED')
FLASK_ADMIN_SWATCH = os.getenv('FLASK_ADMIN_SWATCH')

# Open Api
OPENAPI_URL_PREFIX = os.getenv('OPENAPI_URL_PREFIX')
OPENAPI_SWAGGER_UI_PATH = os.getenv('OPENAPI_SWAGGER_UI_PATH')
OPENAPI_SWAGGER_UI_VERSION = os.getenv('OPENAPI_SWAGGER_UI_VERSION')
