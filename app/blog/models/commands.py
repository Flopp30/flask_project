from flask import Blueprint

from blog.models import db, Article
from blog.models import User

db_app = Blueprint('db', __name__)


@db_app.cli.command('init_db')
def init_db():
    db.create_all()
    print("done!")


@db_app.cli.command('create_users')
def create_users():
    admin = User(username="admin", password='111', email='admin@local.blog', is_staff=True)
    for i in range(10):
        user = User(username=f"user{i}", password='111', email=f'email{i}@local.blog')
        db.session.add(user)

    db.session.add(admin)
    db.session.commit()
    print("done! users created")


@db_app.cli.command('create_articles')
def create_articles():
    for i in range(10):
        art_ = Article(name=f"About python{1}", desc='Some desk for article about python', creator=i+1)
        db.session.add(art_)

    db.session.commit()
    print("done! articles created")
