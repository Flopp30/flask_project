from blog.extensions import db
from blog.models import User
from blog.schemas import UserSchema
from flask_combo_jsonapi import ResourceDetail, ResourceList


class UserList(ResourceList):
    schema = UserSchema
    data_layer = {
        "session": db.session,
        "model": User,
    }


class UserDetail(ResourceDetail):
    schema = UserSchema
    data_layer = {
        "session": db.session,
        "model": User,
    }
