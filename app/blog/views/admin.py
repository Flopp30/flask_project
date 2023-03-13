from flask import Blueprint, redirect, url_for
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

from blog.extensions import admin, db
from blog import models

admin_app = Blueprint("admin_app", __name__, url_prefix='/admin')


class CustomBaseView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_staff

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("auth_app.login"))


class TagAdminView(CustomBaseView):
    column_searchable_list = ("name",)
    column_filters = ("name",)
    can_export = True
    export_types = ["csv", "xlsx"]
    create_modal = True
    edit_modal = True


class UserAdminView(CustomBaseView):
    column_exclude_list = ("_password",)
    column_searchable_list = ("first_name", "last_name", "is_staff", "email")
    column_filters = ("first_name", "last_name", "is_staff", "email")
    column_editable_list = ("first_name", "last_name", "is_staff")
    can_export = True
    export_types = ["csv", "xlsx"]
    can_create = True
    can_edit = True
    can_delete = False
    create_modal = True
    edit_modal = True


class ArticleAdminView(CustomBaseView):
    column_hide_backrefs = False
    column_list = ('title', 'desc', 'author.id', 'tags.name')
    column_searchable_list = ("author_id", "title", "desc")
    column_filters = ("author_id", "title", "desc")
    column_editable_list = ("author_id", "title", "desc")
    can_export = True
    export_types = ["csv", "xlsx"]
    can_create = True
    can_edit = True
    can_delete = False
    create_modal = True
    edit_modal = True


class AuthorAdminView(CustomBaseView):
    column_hide_backrefs = False
    column_list = ('user.id', 'articles')
    column_searchable_list = ("user_id",)
    column_filters = ("user_id",)
    column_editable_list = ("user_id",)
    can_export = True
    export_types = ["csv", "xlsx"]
    can_create = True
    can_edit = True
    can_delete = False
    create_modal = True
    edit_modal = True


admin.add_view(TagAdminView(models.Tag, db.session, category="Models"))
admin.add_view(ArticleAdminView(models.Article, db.session, category="Models"))
admin.add_view(AuthorAdminView(models.Author, db.session, category="Models"))
admin.add_view(UserAdminView(models.User, db.session, category="Models"))
