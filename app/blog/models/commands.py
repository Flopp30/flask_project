from random import choice

from flask import Blueprint
from sqlalchemy.orm import sessionmaker

from blog.extensions import db
from blog.models import Article
from blog.models import User

db_commands_app = Blueprint('custom_commands', __name__)


@db_commands_app.cli.command('init_db')
def init_db():
    db.create_all()
    print("done!")


@db_commands_app.cli.command('create_users')
def create_users():
    Article.query.filter().delete()
    User.query.filter().delete()
    db.session.commit()
    admin = User(username="admin", password='111', email='admin@local.blog', is_staff=True)
    for i in range(10):
        user = User(username=f"user{i}", password='111', email=f'email{i}@local.blog')
        db.session.add(user)

    db.session.add(admin)
    db.session.commit()
    print("done! users created")


@db_commands_app.cli.command('create_articles')
def create_articles():
    users = User.query.all()
    for i in range(10):
        art_ = Article(name=f"About python{1}", desc='Some desk for article about python', creator=choice(users).id)
        db.session.add(art_)

    db.session.commit()
    print("done! articles created")
