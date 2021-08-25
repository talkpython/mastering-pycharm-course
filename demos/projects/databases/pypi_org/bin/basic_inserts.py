import os
import sys

# Make it run more easily outside of PyCharm
sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..")))

import pypi_org.data.db_session as db_session
from pypi_org.data.package import Package
from pypi_org.data.releases import Release


def main():
    init_db()
    while True:
        insert_a_package()


def insert_a_package():
    p = Package()
    p.id = input('Package id / name: ').strip().lower()

    p.summary = input("Package summary: ").strip()
    p.author_name = input("Author: ").strip()
    p.license = input("License: ").strip()

    print("Release 1:")
    r = Release()
    r.major_ver = int(input("Major version: "))
    r.minor_ver = int(input("Minor version: "))
    r.build_ver = int(input("Build version: "))
    r.size = int(input("Size in bytes: "))
    p.releases.append(r)

    print("Release 2:")
    r = Release()
    r.major_ver = int(input("Major version: "))
    r.minor_ver = int(input("Minor version: "))
    r.build_ver = int(input("Build version: "))
    r.size = int(input("Size in bytes: "))
    p.releases.append(r)

    session = db_session.create_session()
    session.add(p)
    session.commit()


def init_db():
    top_folder = os.path.dirname(__file__)
    rel_file = os.path.join('..', 'db', 'pypi.sqlite')
    db_file = os.path.abspath(os.path.join(top_folder, rel_file))
    db_session.global_init(db_file)


if __name__ == '__main__':
    main()
