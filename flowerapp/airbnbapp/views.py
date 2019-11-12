import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
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
class BarChart:
    review_count=0
    neighbourhood=''
    def __init__(self, neighbourhood='', review_count=0):
        self.review_count = review_count
        self.neighbourhood = neighbourhood

def browse(request):
    db_connection = DBConnection()
    rows = db_connection.get_cities()
    entity_list = []
    for i in range(len(rows)):
        entity = Entity(rows[i][2], rows[i][0], i)
        entity_list.append(entity)
    return render(request, "browse_airbnb.html", {"entity_list": entity_list})

def flower(request):
    # db_connection = DBConnection()
    # rows = db_connection.get_neighbourhood_reviews("austin")
    # barchart_list = []
    # for each_row in rows:
    #     bar = BarChart(each_row[0], each_row[1])
    #     barchart_list.append(bar)
    return render(request, "airbnb_flower.html")

@csrf_exempt
def barchart(request):
    db_connection = DBConnection()
    city_name = request.GET.get('city_name')
    rows = db_connection.get_neighbourhood_reviews("austin")
    barchart_list = []
    for each_row in rows:
        bar = BarChart(each_row[0], each_row[1])
        barchart_list.append(bar)
    return JsonResponse(barchart_list, safe=False)
