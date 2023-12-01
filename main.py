from db import MBTLDB

import sys


def connect_to_db() -> MBTLDB:
    if len(sys.argv) < 2:
        print('Path to database not provided')
        sys.exit(2)
    else:
        print('Connecting to database')
        return MBTLDB(sys.argv[1])


if __name__ == '__main__':
    mbtl_db = connect_to_db()
    print('Initializing database')
    mbtl_db.init_db()
    mbtl_db.populate_db()
