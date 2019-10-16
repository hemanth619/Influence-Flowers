import sqlite3
from sqlite3 import Error
from django.conf import settings
import os


class DBConnection:

    def __init__(self):
        database = os.path.join(settings.BASE_DIR, 'db.sqlite3')
        DBConnection.create_connection(self, database)

    def create_connection(self, db_file):
        self.conn = None
        try:
            self.conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

    def get_genres(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM genres_list")
        rows = cur.fetchall()
        return rows
