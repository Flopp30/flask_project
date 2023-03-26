from flask_admin import Admin
from flask_bcrypt import Bcrypt
from flask_combo_jsonapi import Api
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from combojsonapi.spec import ApiSpecPlugin


# Api
def create_api_spec_plugin(app):
    api_spec_plugin = ApiSpecPlugin(
        app=app,
        # Declaring tags list with their descriptions,
        # so API gets organized into groups. it's optional.
        tags={
            "Tag": "Tag API",
            "User": "User API",
            "Author": "Author API",
            "Article": "Article API",
        }
    )
    return api_spec_plugin


api = Api()

# Login manager
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
