from sqlalchemy import Column, Integer, String

from blog.extensions import db
from blog.models.user import User


class Article(db.Model):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    desc = Column(String(500), nullable=False, default=False)
    creator = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

    def __repr__(self):
        return f"<Article #{self.id} {self.name!r}>"
