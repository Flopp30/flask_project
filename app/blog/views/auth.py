from sqlite3 import IntegrityError

from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user

from blog.extensions import login_manager, db
from blog.forms.user import UserRegisterForm, UserLoginForm
from blog.models import User

auth_app = Blueprint("auth_app", __name__, url_prefix='/auth')


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).one_or_none()


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("auth_app.login"))


@auth_app.route("/login/", methods=["GET", "POST"], endpoint="login")
def login():

    if current_user.is_authenticated:
        return redirect(url_for("article_app.list"))
    form = UserLoginForm(request.form)
    if request.method == "POST" and form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).one_or_none()
        if user is None or not user.validate_password(form.password.data):
            return render_template("auth_app/login.html", form=form, error="invalid email or password")
        login_user(user)
        return redirect(url_for("article_app.list"))

    return render_template("auth_app/login.html", form=form)


@auth_app.route("/logout/", endpoint="logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("article_app.list"))


@auth_app.route('/register/', methods=['GET', 'POST'], endpoint='register')
def register():
    if current_user.is_authenticated:
        return redirect(url_for('user_app.detail', user_id=current_user.id))

    form = UserRegisterForm(request.form)
    errors = []
    if request.method == 'POST' and form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).count():
            form.email.errors.append('Email not unique')
            return render_template('auth_app/register.html', form=form)

        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password=form.password.data,
        )
        db.session.add(user)
        try:
            db.session.commit()
        except IntegrityError:
            errors.append('Проблема с доступом к базе')
        else:
            login_user(user)
            return redirect(url_for('user_app.detail', user_id=current_user.id))

    return render_template(
        'auth_app/register.html',
        form=form,
        errors=errors
    )
