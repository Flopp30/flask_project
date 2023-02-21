from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

# Инициализация blueprint для user
userapp = Blueprint('user_app', __name__, url_prefix='/users', static_folder='../static')

USERS = [
    {
        'id': 1,
        'first_name': 'Artem',
        'last_name': 'P',
        'birthday_year': 19995,
    },
    {
        'id': 2,
        'first_name': 'Boris',
        'last_name': 'N',
        'birthday_year': 1980,
    },
    {
        'id': 3,
        'first_name': 'Maria',
        'last_name': 'S',
        'birthday_year': 1978,
    },
    {
        'id': 4,
        'first_name': 'Phill',
        'last_name': 'K',
        'birthday_year': 1975,
    },
    {
        'id': 5,
        'first_name': 'Daniil',
        'last_name': 'F',
        'birthday_year': 1981,
    },
]


@userapp.route('/', endpoint='list')
def user_list():
    '''
        Контроллер для user list
        :return: html template
    '''

    return render_template(
        'user/user_list.html',
        user_list=USERS,
    )


@userapp.route('/<int:user_id>', endpoint='detail')
def get_user(user_id: int):
    '''
        Контроллер для user detail
        :return: html template
    '''

    try:
        user_ = USERS[user_id]
    except KeyError:
        raise NotFound(f"User # {user_id} doesn't exist!")

    return render_template(
        'user/user_detail.html',
        user=user_,
    )
