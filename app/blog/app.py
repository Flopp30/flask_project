'''
Основной файл с контролерами
'''

from flask import Flask

from blog import commands
from blog.extensions import login_manager, migrate, db, flask_bcrypt, csrf
from blog.views.article import article_app
from blog.views.auth import auth_app
from blog.views.author import authors_app
from blog.views.main import main_app
from blog.views.user import user_app


def create_app() -> Flask:
    '''
    Фабрика Flask приложений
    :return: Flask application
    '''
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
    register_commands(app)
    register_extensions(app)
    register_blueprints(app)

    return app


def register_extensions(app: Flask):
    '''
    Подключает расширения
    :param app: Flask application
    :return:
    '''
    login_manager.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)
    flask_bcrypt.init_app(app)


def register_blueprints(app: Flask):
    '''
    Регистрирует все blueprints к указанному приложению
    :param app: Flask application
    :return:
    '''
    app.register_blueprint(main_app)
    app.register_blueprint(user_app)
    app.register_blueprint(article_app)
    app.register_blueprint(auth_app)
    app.register_blueprint(authors_app)


def register_commands(app: Flask):
    '''
    Регистрирует консольные команды
    :param app: Flask application
    '''

    app.cli.add_command(commands.create_users)
    app.cli.add_command(commands.create_admin)
    app.cli.add_command(commands.create_articles)
    app.cli.add_command(commands.create_init_tags)
