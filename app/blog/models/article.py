from sqlalchemy import Column, Integer, String

from blog.extensions import db
from blog.models.user import User, CustomBaseModel


class Article(CustomBaseModel):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String(80), nullable=False)
    desc = Column(String(500), nullable=False, default=False)
    creator = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

    def __repr__(self):
        return f"<Article #{self.id} {self.name!r}>"

    def __init__(self, title, desc, creator):
        self.title = title
        self.desc = desc
        self.creator = creator
