from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

from blog.models import User, Article

# Инициализация blueprint для user
user_app = Blueprint('user_app', __name__, url_prefix='/users', static_folder='../static')


@user_app.route('/', endpoint='list')
def user_list():
    '''
        Контроллер для user list
        :return: html template
    '''
    users = User.query.filter_by(is_staff=False)
    return render_template(
        'user_app/list.html',
        user_list=users,
    )


@user_app.route('/<int:user_id>', endpoint='detail')
def get_user(user_id: int):
    '''
        Контроллер для user detail
        :return: html template
    '''
    user_ = User.query.filter_by(id=user_id).one_or_none()
    if user_ is None:
        raise NotFound(f"User #{user_id} doesn't exist!")
    articles = Article.query.filter_by(author_id=user_id)
    return render_template(
        'user_app/detail.html',
        user=user_,
        articles=articles,
    )
