from django.shortcuts import render
from .dbconnect import DBConnection


class Entity:
    display_name = ''
    document_id = -1

    def __init__(self, display_name='', document_id=-1):
        self.display_name = display_name
        self.document_id = document_id


def browse(request):
    db_connection = DBConnection()
    rows = db_connection.get_genres()
    entity_list = []
    for i in range(len(rows)):
        entity = Entity(rows[i][0], i)
        entity_list.append(entity)
    return render(request, "browse_movies.html", {"entity_list": entity_list})
