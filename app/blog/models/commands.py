from random import choice

from flask import Blueprint

from blog import settings
from blog.extensions import db
from blog.models import Article, Author
from blog.models import User

db_commands_app = Blueprint('custom_commands', __name__)


@db_commands_app.cli.command('create_users')
def create_users():
    Article.query.filter().delete()
    User.query.filter().delete()
    db.session.commit()
    for i in range(10):
        user = User(first_name=f"user{i}", last_name=f'last_name{i}', password='111', email=f'email{i}@local.blog')
        db.session.add(user)

    db.session.commit()
    print("done! users created")


@db_commands_app.cli.command('create_articles')
def create_articles():
    users = User.query.all()
    for i in range(10):
        art_ = Article(title=f"About python{i}", desc='Some desk for article about python')
        art_.author_id = choice(users).id
        author = Author(user_id=art_.author_id)
        db.session.add(art_)
        db.session.add(author)

    db.session.commit()
    print("done! articles created")


@db_commands_app.cli.command('create_admin')
def create_admin():
    admin = User(first_name="admin", last_name='1', password=settings.ADMIN_PASSWORD, email=settings.ADMIN_EMAIL,
                 is_staff=True)
    db.session.add(admin)
    db.session.commit()
    print("done! admin user created")
