import sqlalchemy
from pypi_org.data.modelbase import SqlAlchemyBase


class Maintainer(SqlAlchemyBase):
    __tablename__ = 'maintainers'

    user_id: int = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    package_id: str = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
