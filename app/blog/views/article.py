from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

from blog.models import Article, User

# Инициализация blueprint для article
article_app = Blueprint('article_app', __name__, url_prefix='/article', static_folder='../static')


@article_app.route('/', endpoint='list')
def article_list():
    '''
        Контроллер для article list
        :return: html template
    '''
    articles = Article.query.all()
    return render_template(
        'article_app/article_list.html',
        article_list=articles,
    )


@article_app.route('/<int:article_id>', endpoint='detail')
def get_article(article_id: int):
    '''
        Контроллер для article_detail
        :return: html template
    '''

    article_ = Article.query.filter_by(id=article_id).one_or_none()
    user = User.query.filter_by(id=article_.creator).one_or_none()
    if article_ is None:
        raise NotFound(f"User #{article_id} doesn't exist!")
    return render_template(
        'article_app/article_detail.html',
        article=article_,
        user=user,
    )
