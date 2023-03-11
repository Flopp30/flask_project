from random import choice

import click

from blog import settings
from blog.extensions import db
from blog.models import Article, Author
from blog.models import User
from blog.models.article import Tag


@click.command('create_users')
def create_users():
    Article.query.filter().delete()
    User.query.filter().delete()
    db.session.commit()
    for i in range(10):
        user = User(first_name=f"user{i}", last_name=f'last_name{i}', password='111', email=f'email{i}@local.blog')
        db.session.add(user)

    db.session.commit()
    click.echo("done! users created")


@click.command('create_articles')
def create_articles():
    users = User.query.all()
    for i in range(10):
        art_ = Article(title=f"About python{i}", desc='Some desk for article about python')
        art_.author_id = choice(users).id
        author = Author(user_id=art_.author_id)
        db.session.add(art_)
        db.session.add(author)

    db.session.commit()
    click.echo("done! articles created")


@click.command('create_admin')
def create_admin():
    admin = User(first_name="admin", last_name='1', password=settings.ADMIN_PASSWORD, email=settings.ADMIN_EMAIL,
                 is_staff=True)
    db.session.add(admin)
    db.session.commit()
    click.echo("done! admin user created")


@click.command('create_init_tags')
def create_init_tags():
    tags = ('python', 'flask', 'django', 'javascript', 'docker')
    for name in tags:
        tag = Tag(name=name)
        db.session.add(tag)
    db.session.commit()
    click.echo('done! tags created: ' + ', '.join(tags))
