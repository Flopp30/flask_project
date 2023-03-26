from flask_admin import Admin
from flask_bcrypt import Bcrypt
from flask_combo_jsonapi import Api
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

# Объект логинов
login_manager = LoginManager()
login_manager.login_view = "auth_app.login"
# Инициализация миграций
migrate = Migrate()
# Инициализация бд
db = SQLAlchemy()
# Хэширование паролей
flask_bcrypt = Bcrypt()
# CSRF protect
csrf = CSRFProtect()
# Admin
admin = Admin(name='Blog Admin Panel', template_mode='bootstrap4')
# Api
api = Api()