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
    
    def noofmovies(self, genres):
        genres_list = []
        year_movie_count = {}
        if "," in genres:
            genres_list = genres.split(",")
        else:
            genres_list.append(genres)
        year_query = "select StartYear from movies_data where StartYear is not NULL and StartYear <> '' "
        for genre in genres_list:
            year_query += "and Genres like '%" + genre + "%' "
        year_query += "ORDER by StartYear ASC"
        cur = self.conn.cursor()
        cur.execute(year_query)
        movies_years = cur.fetchall()
        for year in movies_years:
            if(year[0] in year_movie_count):
                year_movie_count[year[0]] += 1
            else:
                year_movie_count[year[0]] = 1
        return year_movie_count

    def split_directors(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM movies_data")
        rows = cur.fetchall()
        for row in rows:
            if(str(row[1]).find(',') >=0):
                directors = str(row[1]).split(',')
                record = list(row)
                cur.execute("DELETE FROM movies_data WHERE Directors='{0}'".format(row[1]))
                for director in directors:
                    record[1] = director
                    print("INSERT INTO movies_data VALUES{0}".format(tuple(record)))
                    #TODO Fails when multi type quotes are present in title
                    cur.execute("INSERT INTO movies_data VALUES{0}".format(tuple(record)))
            

