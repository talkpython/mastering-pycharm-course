# noinspection PyPackageRequirements
from models.album import Album
# noinspection PyPackageRequirements
from models.dbsession import DbSessionFactory


def main():
    DbSessionFactory.global_init()
    list_albums()


def list_albums():
    session = DbSessionFactory.create_session()

    query = session.query(Album).order_by(Album.name.desc())
    albums = list(query)

    print("There are {} albums".format(len(albums)))
    for a in albums:
        print("* {} - {} tracks".format(a.name, len(a.tracks)))


if __name__ == '__main__':
    main()
