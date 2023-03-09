from sqlite3 import IntegrityError

from flask import Blueprint, render_template, request, current_app, redirect, url_for
from flask_login import login_required, current_user
from werkzeug.exceptions import NotFound

from blog.extensions import db
from blog.forms.article import CreateArticleForm
from blog.models import Article, User, Author

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
        'article_app/list.html',
        article_list=articles,
    )


@article_app.route('/<int:article_id>', endpoint='detail')
def get_article(article_id: int):
    '''
        Контроллер для article_detail
        :return: html template
    '''

    article_ = Article.query.filter_by(id=article_id).one_or_none()
    if article_ is None:
        raise NotFound(f"Article #{article_id} doesn't exist!")
    return render_template(
        'article_app/detail.html',
        article=article_,
    )


@article_app.route("/create/", methods=["GET", "POST"], endpoint="create")
@login_required
def create_article():
    error = None
    form = CreateArticleForm(request.form)

    if request.method == "POST" and form.validate_on_submit():
        article = Article(title=form.title.data.strip(), desc=form.body.data)
        db.session.add(article)
        if current_user.author:
            article.author = current_user.author
        else:
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.flush()
            article.author = current_user.author
        try:
            db.session.commit()
        except IntegrityError:
            current_app.logger.exception("Could not create a new article!")
            error = "Could not create article!"
        else:
            return redirect(url_for("article_app.detail", article_id=article.id))
    return render_template("article_app/create.html", form=form, error=error)
