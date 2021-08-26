import sqlalchemy.orm
from sqlalchemy.ext.orderinglist import ordering_list

# noinspection PyPackageRequirements
from models.modelbase import SqlAlchemyBase


class Album(SqlAlchemyBase):
    __tablename__ = 'Album'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=False)
    url = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=False)
    year = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    price = sqlalchemy.Column(sqlalchemy.Float, index=True)
    album_image = sqlalchemy.Column(sqlalchemy.String)
    has_preview = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    is_published = sqlalchemy.Column(sqlalchemy.Boolean, default=False)

    tracks = sqlalchemy.orm.relationship('Track', back_populates='album',
                                         order_by='Track.display_order',
                                         collection_class=ordering_list('display_order'),
                                         cascade='all')
