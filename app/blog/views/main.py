from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

# Инициализация blueprint для user
main_app = Blueprint('main_app', __name__, url_prefix='/', static_folder='../static')


@main_app.route('/', endpoint='index')
def index():
    '''
        Контроллер для  index
        :return: html template
    '''
    return render_template(
        'main_app/index.html',
    )


@main_app.route('/contacts', endpoint='contacts')
def contacts():
    '''
        Контроллер для  contacts
        :return: html template
    '''
    return render_template(
        'main_app/contacts.html',
    )


@main_app.route('/about', endpoint='about_us')
def about_us():
    '''
        Контроллер для  contacts
        :return: html template
    '''
    return render_template(
        'main_app/about.html',
    )
