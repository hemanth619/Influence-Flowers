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
    city_name = request.POST.get('city_name')
    country_name = request.POST.get('country_name')
    review_rows = db_connection.get_neighbourhood_reviews(city_name, country_name)
    listing_rows = db_connection.get_neighbourhood_listing(city_name, country_name)
    reviews_per_year = db_connection.get_reviews_per_year(city_name)
    listings_per_year = db_connection.get_listings_per_year(city_name, country_name)

    barchart_list = [[],[],[]]

    review_list = {}

    for each_row in review_rows:
        review_list[each_row[0]] = each_row[1]

    # yearly_reviews = []
    for each_row in reviews_per_year:
        yearlyReviewObj = {}
        yearlyReviewObj['year'] = each_row[1]
        yearlyReviewObj['num_of_reviews'] = each_row[0]
        barchart_list[1].append(yearlyReviewObj)

    # yearly_listings = []
    for each_row in listings_per_year:
        yearlyListingsObj = {}
        yearlyListingsObj['year'] = each_row[0]
        yearlyListingsObj['num_of_listings'] = each_row[1]
        barchart_list[2].append(yearlyListingsObj)
   
    for each_row in listing_rows:
        reviewObj = {}
        reviewObj['neighbourhood'] = each_row[0]
        reviewObj['count'] = review_list[each_row[0]]
        reviewObj['type'] = "review"
        barchart_list[0].append(reviewObj)

        listingObj = {}
        listingObj['neighbourhood'] = each_row[0] + "1"
        listingObj['count'] = each_row[1] * 25
        listingObj['type'] = "listing"
        barchart_list[0].append(listingObj)

    
    
    return JsonResponse(barchart_list, safe=False)
