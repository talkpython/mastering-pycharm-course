import datetime
import sqlalchemy
from pypi_org.data.modelbase import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True, index=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, index=True)
    profile_image_url = sqlalchemy.Column(sqlalchemy.String)
    last_login = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, index=True)
