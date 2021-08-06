import datetime
import sqlalchemy
from pypi_org.data.modelbase import SqlAlchemyBase


class Download(SqlAlchemyBase):
    __tablename__ = 'downloads'

    id: int = sqlalchemy.Column(sqlalchemy.BigInteger, primary_key=True, autoincrement=True)
    created_date: datetime.datetime = sqlalchemy.Column(
        sqlalchemy.DateTime, default=datetime.datetime.now, index=True)

    package_id: str = sqlalchemy.Column(sqlalchemy.String, index=True)
    release_id: int = sqlalchemy.Column(sqlalchemy.BigInteger, index=True)

    ip_address: str = sqlalchemy.Column(sqlalchemy.String)
    user_agent: str = sqlalchemy.Column(sqlalchemy.String)
