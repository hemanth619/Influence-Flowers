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

    def get_cities(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM airbnb_ego_selection")
        rows = cur.fetchall()
        return rows

    def get_neighbourhood_reviews(self, cityname):
        cur = self.conn.cursor()
        query_string = "select neighbourhood,  sum(number_of_reviews) as reviews_count from us_data where City = "+cityname+" group by neighbourhood order by reviews_count desc;"
        cur.execute(query_string)
        rows = cur.fetchall()
        return rows
