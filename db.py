from characters import URL_NAMES
from mbtl import MBTLScraper
import sqlite3
from sqlite3 import Error
import sys

CREATE_CHARACTER_TABLE = """CREATE TABLE character (
                                id INTEGER PRIMARY KEY,
                                name varchar(255) NOT NULL,
                                nickname varchar(255) NOT NULL
                                );"""

CREATE_MOVE_TABLE = """CREATE TABLE move (
                            id INTEGER PRIMARY KEY,
                            charId INTEGER NOT NULL,
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
                            FOREIGN KEY (charId) REFERENCES character(id)
                    );"""

INSERT_CHARACTER = """INSERT INTO character (name, nickname) VALUES ( "{}",
                        "{}");"""

INSERT_MOVE = """INSERT INTO move (charId, name, input, damage, block, cancel,
                    property, cost, attribute, startup, active, recovery,
                    overall, advantage, invuln) VALUES ({}, "{}", "{}", "{}",
                    "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}",
                    "{}");"""


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
            c.execute("DROP TABLE IF EXISTS character;")
            c.execute("DROP TABLE IF EXISTS move;")
            c.execute(CREATE_CHARACTER_TABLE)
            c.execute(CREATE_MOVE_TABLE)
        except Error as e:
            print(e)
            sys.exit(1)

    def populate_db(self):
        for c in URL_NAMES:
            scraper = MBTLScraper(c, URL_NAMES[c])
            moves = scraper.scrape_movelist()
            
            cursor = self.conn.cursor()
            cursor.execute(INSERT_CHARACTER.format(c, URL_NAMES[c]))
            self.conn.commit()
            char_id = cursor.lastrowid

            for m in moves:
                cursor.execute(INSERT_MOVE.format(char_id, m.name, m.input,
                                                       m.damage, m.block,
                                                       m.cancel, m.property,
                                                       m.cost, m.attribute,
                                                       m.startup,  m.active,
                                                       m.recovery, m.overall,
                                                       m.advantage,
                                                       m.invuln))
            self.conn.commit()
