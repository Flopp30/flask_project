from blog.extensions import db
from blog.models import Tag
from blog.schemas import TagSchema
from flask_combo_jsonapi import ResourceDetail, ResourceList


class TagList(ResourceList):
    schema = TagSchema
    data_layer = {
        "session": db.session,
        "model": Tag,
    }


class TagDetail(ResourceDetail):
    schema = TagSchema
    data_layer = {
        "session": db.session,
        "model": Tag,
    }
