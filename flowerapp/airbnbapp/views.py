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

    barchart_list = [[],[],[]]


    db_connection = DBConnection()
    city_name = request.POST.get('city_name')
    country_name = request.POST.get('country_name')


    reviews_per_year = db_connection.get_reviews_per_year(city_name)
    listings_per_year = db_connection.get_listings_per_year(city_name, country_name)

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

    barchart_list[0] = computeBottomChartData(db_connection, city_name, country_name, str(2009), str(2019),str(2009), str(2019))

    return JsonResponse(barchart_list, safe=False)

@csrf_exempt
def computeBottomChartData(db_connection, city_name, country_name, from_review_year, to_review_year, from_listing_year, to_listing_year):

    barchart = []
    
    review_rows = db_connection.get_neighbourhood_reviews_between_years(city_name, country_name, from_review_year, to_review_year)
    listing_rows = db_connection.get_neighbourhood_listing_between_years(city_name, country_name, from_listing_year, to_listing_year)

    review_list = {}

    for each_row in review_rows:
        review_list[each_row[0]] = each_row[1]


    for each_row in listing_rows:
        reviewObj = {}
        reviewObj['neighbourhood'] = each_row[0]

        # Check if that neighbourhood exists for the given range of years
        if each_row[0] in review_list:
            reviewObj['count'] = review_list[each_row[0]]
        else:
            reviewObj['count'] = 0

        reviewObj['type'] = "review"
        barchart.append(reviewObj)

        listingObj = {}
        listingObj['neighbourhood'] = each_row[0] + "1"
        listingObj['count'] = each_row[1] * 25
        listingObj['type'] = "listing"
        barchart.append(listingObj)

    return barchart

@csrf_exempt
def regenerate(request):
    db_connection = DBConnection()
    return_response = [[]]
    city_name = request.POST.get('city_name')
    country_name = request.POST.get('country_name')
    from_review_year = int(request.POST.get('from_review_year'))
    to_review_year = int(request.POST.get('to_review_year'))
    from_listing_year = int(request.POST.get('from_listing_year'))
    to_listing_year = int(request.POST.get('to_listing_year'))
    
    return_response[0] = computeBottomChartData(db_connection, city_name, country_name, from_review_year, to_review_year, from_listing_year, to_listing_year)

    return JsonResponse(return_response, safe=False)