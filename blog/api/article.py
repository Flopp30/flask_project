from blog.extensions import db
from blog.models import Article
from blog.schemas import ArticleSchema
from flask_combo_jsonapi import ResourceDetail, ResourceList


class ArticleList(ResourceList):
    schema = ArticleSchema
    data_layer = {
        "session": db.session,
        "model": Article,
    }


class ArticleDetail(ResourceDetail):
    schema = ArticleSchema
    data_layer = {
        "session": db.session,
        "model": Article,
    }
