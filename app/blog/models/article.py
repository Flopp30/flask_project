from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship

from blog.models.author import Author
from blog.models.user import CustomBaseModel


class Article(CustomBaseModel):
    __tablename__ = 'articles'

    id = Column(Integer(), primary_key=True)
    author_id = Column(Integer(), ForeignKey('authors.id'))

    title = Column(String(80), nullable=False)
    desc = Column(Text(), nullable=False, default=False)

    author = relationship("Author", back_populates="articles")

    def __repr__(self):
        return f"<Article #{self.id} {self.name!r}>"

    def __init__(self, title, desc):
        self.title = title
        self.desc = desc
