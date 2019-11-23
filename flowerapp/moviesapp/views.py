from django.shortcuts import render
from .dbconnect import DBConnection
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import math


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

def query_browse_group(genre_list):
    document = {}
    document["DisplayName"] = genre_list
    return document

def get_url_query(query):
    config = None
    genre_list = query.get("genre_list")
    document = query_browse_group(genre_list)
    return document, "author", config

def flower(request):
    print("Movies Flower Request: ", datetime.now())
    total_request_cur = datetime.now()
    time_cur = datetime.now()
    configuration = dict()
    session = dict()
    curated_flag = False
    num_leaves = 10
    print("FLOWER REQUEST")
    print(request.GET)
    if request.method == "GET":
        # URL sample
        # /moviesflower/?genre_list=Adventure,Romance,Horror
        curated_flag = True
        data, option,config = get_url_query(request.GET)
        print('--------------------------')
        print("DATA FROM DB ON QUERY")
        print(data)
        print('--------------------------')
        flower_name = str(data.get("DisplayName"))
        configuration["flower_name"] = flower_name
        print("flower_name", flower_name)
    else:
        # TODO
        pass
    min_year = None
    max_year = None

    # some debug prints
    time_cur = datetime.now()

    # check if data is returned else redirect to missing_info page
    if False:
        return render(request, "missing_info.html")
    
    print('--------------------------')
    print("Number of Movies found: ")
    print('Time taken: ', datetime.now() - time_cur)
    print('--------------------------')

    # flower_config = default_config()
    # if config:
    #     flower_config = config
    
    db_connection = DBConnection()
    statpanel_default_data = db_connection.noofmovies(flower_name)
    statpanel_json_list = []
    for row in statpanel_default_data:
        statpanel_json_list.append({"year":row, "count":statpanel_default_data[row]})
    print(statpanel_json_list)
    configuration['statpanel_default_data'] = statpanel_json_list

    data["session"] = session
    data["configuration"] = configuration
    # data["config"] = config

    return render(request, "flower_movies.html", data)

