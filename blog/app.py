'''
Фабрика Flask приложения
'''
from combojsonapi.event import EventPlugin
from combojsonapi.permission import PermissionPlugin
from combojsonapi.spec import ApiSpecPlugin
from flask import Flask

from blog import commands
from blog.api.article import ArticleList, ArticleDetail
from blog.api.author import AuthorList, AuthorDetail
from blog.api.tag import TagList, TagDetail
from blog.api.user import UserList, UserDetail
from blog.extensions import login_manager, migrate, db, flask_bcrypt, csrf, admin, api
from blog.views.admin import admin_app
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
    register_api(app)

    return app


def register_extensions(app: Flask):
    '''
    Подключает расширения
    :param app: Flask application
    :return:
    '''
    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)
    admin.init_app(app)

    login_manager.init_app(app)
    flask_bcrypt.init_app(app)


def register_blueprints(app: Flask):
    '''
    Регистрирует все blueprints к указанному приложению
    :param app: Flask application
    :return:
    '''
    app.register_blueprint(main_app)
    app.register_blueprint(admin_app)
    app.register_blueprint(user_app)
    app.register_blueprint(article_app)
    app.register_blueprint(auth_app)
    app.register_blueprint(authors_app)


def register_api(app: Flask):
    api.plugins = [
        EventPlugin(),
        PermissionPlugin(strict=False),
        ApiSpecPlugin(
            app=app,
            tags={
                "Tag": "Tag API",
                "User": "User API",
                "Author": "Author API",
                "Article": "Article API",
            }
        ),
    ]
    api.init_app(app)

    api.route(TagList, "tag_list", "/api/tags/", tag='Tag')
    api.route(TagDetail, "tag_detail", "/api/tags/<int:id>/", tag='Tag')

    api.route(UserList, "user_list", "/api/users/", tag="User")
    api.route(UserDetail, "user_detail", "/api/users/<int:id>/", tag="User")

    api.route(AuthorList, "author_list", "/api/authors/", tag="Author")
    api.route(AuthorDetail, "author_detail", "/api/authors/<int:id>/", tag="Author")

    api.route(ArticleList, "article_list", "/api/articles/", tag="Article")
    api.route(ArticleDetail, "article_detail", "/api/articles/<int:id>/", tag="Article")


def register_commands(app: Flask):
    '''
    Регистрирует консольные команды
    :param app: Flask application
    '''

    app.cli.add_command(commands.create_users)
    app.cli.add_command(commands.create_admin)
    app.cli.add_command(commands.create_articles)
    app.cli.add_command(commands.create_init_tags)
