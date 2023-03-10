from flask import Blueprint, render_template
from blog.models import Author

authors_app = Blueprint("author_app", __name__, url_prefix='/authors')


@authors_app.route("/", endpoint="list")
def authors_list():
    authors = Author.query.all()
    return render_template("author_app/list.html", author_list=authors)
