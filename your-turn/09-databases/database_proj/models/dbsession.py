import os
import sqlalchemy
import sqlalchemy.orm
# noinspection PyPackageRequirements
from models.modelbase import SqlAlchemyBase
# noinspection PyUnresolvedReferences,PyPackageRequirements
import models.album
# noinspection PyUnresolvedReferences,PyPackageRequirements
import models.track


class DbSessionFactory:
    factory = None

    @staticmethod
    def global_init():
        if DbSessionFactory.factory:
            return

        db_file = os.path.join(os.path.dirname(__file__), '..', 'db', 'blue_yellow.sqlite')
        db_file = os.path.abspath(db_file)

        conn_str = 'sqlite:///' + db_file
        print("Connecting to db with conn string: {}".format(conn_str))

        engine = sqlalchemy.create_engine(conn_str, echo=False)
        SqlAlchemyBase.metadata.create_all(engine)
        DbSessionFactory.factory = sqlalchemy.orm.sessionmaker(bind=engine)

    @staticmethod
    def create_session():
        return DbSessionFactory.factory()
