from datetime import datetime

from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Boolean, LargeBinary, DateTime

from blog.extensions import db, flask_bcrypt


class CustomBaseModel(db.Model):
    __abstract__ = True

    created_at = Column('created_at', DateTime(), default=datetime.now)
    updated_at = Column('updated_at', DateTime(), default=datetime.now, onupdate=datetime.now)
    deleted = Column('Is deleted?', Boolean(), default=False)

    def __del__(self):
        self.deleted = True


class User(CustomBaseModel, UserMixin):
    __tablename__ = 'users'

    id = Column('id', Integer(), primary_key=True)
    first_name = Column('first_name', String(80), unique=True, nullable=False, default='')
    last_name = Column('last_name', String(80), unique=True, nullable=False, default='')
    _password = Column('password', String(500), nullable=False)
    email = Column('email', String(80), unique=True, nullable=False, default="", server_default="")
    is_staff = Column('is staff', Boolean(), default=False)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = flask_bcrypt.generate_password_hash(value)

    def validate_password(self, password) -> bool:
        return flask_bcrypt.check_password_hash(self._password, password)

    def __repr__(self):
        return f"<User #{self.id} {self.username!r}>"

    def __init__(self, first_name: str, last_name: str, password: str, email: str, is_staff: bool = False):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email
        self.is_staff = is_staff
