'''
Основной файл с контролерами
'''
from flask import Flask

from blog.user.views import userapp
from blog.article.views import articleapp


def create_app() -> Flask:
    '''
    Фабрика Flask приложений
    :return: Flask application
    '''
    app = Flask(__name__)
    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    '''
    Регистрирует все blueprints к указанному приложению
    :param app: Flask application
    :return:
    '''
    app.register_blueprint(userapp)
    app.register_blueprint(articleapp)
