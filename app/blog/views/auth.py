from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required

from blog.extensions import login_manager
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
    if request.method == "GET":
        return render_template("auth_app/login.html")

    username = request.form.get("username")
    if not username:
        return render_template("auth_app/login.html", error="Wrong username or password")

    user = User.query.filter_by(username=username).one_or_none()
    if user is None:
        return render_template("auth_app/login.html", error=f"Wrong username or password")
    login_user(user)
    return redirect(url_for("article_app.list"))


@auth_app.route("/logout/", endpoint="logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("article_app.list"))