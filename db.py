import sqlite3
from sqlite3 import Error
import sys

CREATE_CHARACTER_TABLE = """CREATE TABLE character (
                                id int NOT NULL,
                                name varchar(255) NOT NULL,
                                PRIMARY KEY(id));"""

CREATE_MOVE_TABLE = """CREATE TABLE move (
                            id int NOT NULL,
                            charId int NOT NULL,
                            name varchar(255) NOT NULL,
                            input varchar(15) NOT NULL,
                            damage varchar(7) NOT NULL,
                            block varchar(4) NOT NULL,
                            cancel varchar(255) NOT NULL,
                            property varchar(255) NOT NULL,
                            cost varchar(255) NOT NULL,
                            attribute varchar(255) NOT NULL,
                            startup varchar(255) NOT NULL,
                            active varchar(255) NOT NULL,
                            recovery varchar(255) NOT NULL,
                            overall varchar(255) NOT NULL,
                            advantage varchar(255) NOT NULL,
                            invuln varchar(255) NOT NULL,
                            PRIMARY KEY(id),
                            FOREIGN KEY (charId) REFERENCES character(id)
                    );"""

class MBTLDB:
    def __init__(self, path_to_db):
        try:
            self.conn = sqlite3.connect(path_to_db)
        except Error as e:
            print(e)
            sys.exit(1)

    def init_db(self):
        try:
            c = self.conn.cursor()
            c.execute(CREATE_CHARACTER_TABLE)
            c.execute(CREATE_MOVE_TABLE)
        except Error as e:
            print(e)
            sys.exit(1)
