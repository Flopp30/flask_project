'''
Основной файл с контролерами
'''

from flask import Flask

from blog.models.commands import db_app
from blog.models.database import db
from blog.views.article import article_app
from blog.views.auth import auth_app, login_manager
from blog.views.user import user_app


def create_app() -> Flask:
    '''
    Фабрика Flask приложений
    :return: Flask application
    '''
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    db.init_app(app)
    login_manager.init_app(app)

    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    '''
    Регистрирует все blueprints к указанному приложению
    :param app: Flask application
    :return:
    '''
    app.register_blueprint(db_app)
    app.register_blueprint(user_app)
    app.register_blueprint(article_app)
    app.register_blueprint(auth_app)
