from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

# Инициализация blueprint для article
articleapp = Blueprint('article_app', __name__, url_prefix='/article', static_folder='../static')

ARTICLES = [1, 2, 3, 4, 5]


@articleapp.route('/', endpoint='list')
def article_list():
    '''
        Контроллер для article list
        :return: html template
    '''
    return render_template(
        'article/article_list.html',
        article_list=ARTICLES,
    )


@articleapp.route('/<int:article_id>', endpoint='detail')
def get_article(article_id: int):
    '''
        Контроллер для article_detail
        :return: html template
    '''

    try:
        article_ = ARTICLES[article_id - 1]
    except KeyError:
        raise NotFound(f"Article # {article_id} doesn't exist!")

    return render_template(
        'article/article_detail.html',
        article=article_,
    )
