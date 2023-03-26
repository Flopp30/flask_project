from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from blog.models.user import CustomBaseModel


class Author(CustomBaseModel):
    __tablename__ = 'authors'

    id = Column('id', Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey('users.id'), nullable=False)

    user = relationship("User", back_populates="author")
    articles = relationship("Article", back_populates="author")

    def __str__(self):
        return self.user.email
