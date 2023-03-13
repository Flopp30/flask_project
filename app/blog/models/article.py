from sqlalchemy import Column, Integer, String, ForeignKey, Text, Table
from sqlalchemy.orm import relationship
from blog.extensions import db

from blog.models.user import CustomBaseModel

article_tag_associations_table = Table(
    'article_tag_associations',
    db.metadata,
    Column('article_id', Integer(), ForeignKey('articles.id'), nullable=False),
    Column('tag_id', Integer(), ForeignKey('tags.id'), nullable=False),
)


class Article(CustomBaseModel):
    __tablename__ = 'articles'

    id = Column(Integer(), primary_key=True)
    author_id = Column(Integer(), ForeignKey('authors.id'))
    title = Column(String(80), nullable=False)
    desc = Column(Text(), nullable=False, default=False)

    author = relationship("Author", back_populates="articles")
    tags = relationship("Tag", secondary=article_tag_associations_table, back_populates="articles")

    def __repr__(self):
        return f"<Article #{self.id} {self.title!r}>"

    def __init__(self, title, desc):
        self.title = title
        self.desc = desc


class Tag(CustomBaseModel):
    __tablename__ = 'tags'

    id = Column(Integer(), primary_key=True)
    name = Column(String(120), nullable=False)

    articles = relationship("Article", secondary=article_tag_associations_table, back_populates="tags")

    def __str__(self):
        return self.name
