from django.shortcuts import render
from .dbconnect import DBConnection
# Create your views here.
class Entity:
    display_name = ''
    s_no=''
    document_id = -1
    def __init__(self, display_name='', s_no='', document_id=-1):
        self.display_name = display_name
        self.s_no = s_no
        self.document_id = document_id
def browse(request):
    db_connection = DBConnection()
    rows = db_connection.get_cities()
    entity_list = []
    for i in range(len(rows)):
        entity = Entity(rows[i][2], rows[i][0], i)
        entity_list.append(entity)
    return render(request, "browse_airbnb.html", {"entity_list": entity_list})