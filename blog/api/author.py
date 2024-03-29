from blog.extensions import db
from blog.models import Author
from blog.schemas import AuthorSchema
from flask_combo_jsonapi import ResourceDetail, ResourceList


class AuthorList(ResourceList):
    schema = AuthorSchema
    data_layer = {
        "session": db.session,
        "model": Author,
    }


class AuthorDetail(ResourceDetail):
    schema = AuthorSchema
    data_layer = {
        "session": db.session,
        "model": Author,
    }
