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

    responseJson = {}

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

    responseJson = computeChartData(db_connection, city_name, country_name, str(2009), str(2019),str(2009), str(2019))
    responseJson['numReviews'] = barchart_list[1]
    responseJson['numListings'] = barchart_list[2]

    # print(responseJson)

    return JsonResponse(responseJson, safe=False)

@csrf_exempt
def computeChartData(db_connection, city_name, country_name, from_review_year, to_review_year, from_listing_year, to_listing_year):

    responseData = {};

    barchart = []
    
    review_rows = db_connection.get_neighbourhood_reviews_between_years(city_name, country_name, from_review_year, to_review_year)
    listing_rows = db_connection.get_neighbourhood_listing_between_years(city_name, country_name, from_listing_year, to_listing_year)

    id = 0
    neighbourhoodIdMap = {}
    neighbourhoodIdMap[city_name] = id

    review_list = {}
    for each_row in review_rows:
        review_list[each_row[0]] = each_row[1]
        # Also compute the IDs for neighbourhood 
        id +=1
        neighbourhoodIdMap[each_row[0]] = id

    # Compute review weights
    review_weights = computeWeight(review_rows, "reviews", city_name, country_name)

    

    listings_list = {}
    for each_row in listing_rows:
        listings_list[each_row[0]] = each_row[1]
        

    # Compute listings weights
    listings_weights = computeWeight(listing_rows, "listings", city_name, country_name)


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

    flowerData = prepFlowerData(review_weights, listings_weights, city_name, neighbourhoodIdMap)

    responseData['bars'] = barchart
    responseData['links'] = flowerData[0]
    responseData['nodes'] = flowerData[1]
        

    return responseData

def computeWeight(lists, listType, city_name, country_name):
    db_connection = DBConnection()

    weights = {}
    if listType == "reviews":
        reviewMaxMin = db_connection.getMaxMin(city_name, country_name, "reviews")
        reviewMax = float(reviewMaxMin[0])
        reviewMin = float(reviewMaxMin[1])
        maxminDiff = reviewMax - reviewMin

        for eachrow in lists:
            weights[eachrow[0]] = (float(eachrow[1]) - reviewMin) / maxminDiff

    else:
        listingsMaxMin = db_connection.getMaxMin(city_name, country_name, "listings")
        listingsMax = listingsMaxMin[0]
        listingsMin = listingsMaxMin[1]
        maxminDiff = listingsMax - listingsMin

        for eachrow in lists:
            weights[eachrow[0]] = (float(eachrow[1]) - listingsMin) / maxminDiff

    return weights

def prepFlowerData(review_weights, listings_weights, city_name, neighbourhoodIdMap):
    db_connection = DBConnection()

    flowerData = [[],[]]

    flowerReviewNodeObj = {}
    flowerReviewNodeObj['bloom_order'] = 0
    flowerReviewNodeObj['hostels'] = "False"
    flowerReviewNodeObj['filter_num'] = 0
    flowerReviewNodeObj['gtype'] = "neighbourhood"
    flowerReviewNodeObj['id'] = 0
    flowerReviewNodeObj['name'] = json.loads(city_name)
    flowerReviewNodeObj['diff'] = 0 #Need to check
    flowerReviewNodeObj['inf_in'] = 0 #Need to check
    flowerReviewNodeObj['inf_out'] = 0 #Need to check
    flowerReviewNodeObj['ratio'] = -1 
    flowerReviewNodeObj['size'] = 0 #Need to check
    flowerReviewNodeObj['sum'] = 6.5 #Need to check
    flowerReviewNodeObj['weight'] = 0 #Need to check
    flowerReviewNodeObj['xpos'] = 0 #Need to check
    flowerReviewNodeObj['ypos'] = 0 #Need to check
    flowerData[1].append(flowerReviewNodeObj)



    for each_row in review_weights:
        # Link review obj 
        flowerReviewDataObj = {}
        flowerReviewDataObj['gtype'] = "neighbourhood"
        flowerReviewDataObj['id'] = neighbourhoodIdMap[each_row]
        flowerReviewDataObj['bloom_order'] = neighbourhoodIdMap[each_row]
        flowerReviewDataObj['filter_num'] = 0
        flowerReviewDataObj['padding'] = 1
        flowerReviewDataObj['type'] = "in"
        flowerReviewDataObj['source'] = each_row #neighbourhood
        flowerReviewDataObj['target'] = json.loads(city_name)
        flowerReviewDataObj['weight'] = review_weights[each_row]
        flowerReviewDataObj['o_weight'] = 0 #Not sure what it needs to have
        flowerData[0].append(flowerReviewDataObj)

        # Link listing obj 
        flowerListingDataObj = {}
        flowerListingDataObj['gtype'] = "neighbourhood"
        flowerListingDataObj['id'] = neighbourhoodIdMap[each_row]
        flowerListingDataObj['bloom_order'] = neighbourhoodIdMap[each_row]
        flowerListingDataObj['filter_num'] = 0
        flowerListingDataObj['padding'] = 1
        flowerListingDataObj['type'] = "out"
        flowerListingDataObj['source'] = json.loads(city_name)
        flowerListingDataObj['target'] = each_row
        flowerListingDataObj['weight'] = listings_weights[each_row]
        flowerListingDataObj['o_weight'] = 0 #Not sure what it needs to have
        flowerData[0].append(flowerListingDataObj)

        # Node Obj 
        flowerReviewNodeObj = {}
        flowerReviewNodeObj['bloom_order'] = neighbourhoodIdMap[each_row]
        flowerReviewNodeObj['hostels'] = "False"
        flowerReviewNodeObj['filter_num'] = 0
        flowerReviewNodeObj['gtype'] = "neighbourhood"
        flowerReviewNodeObj['id'] = neighbourhoodIdMap[each_row]
        flowerReviewNodeObj['name'] = each_row
        flowerReviewNodeObj['dif'] = 0 #Need to check
        flowerReviewNodeObj['inf_in'] = 0 #Need to check
        flowerReviewNodeObj['inf_out'] = 0 #Need to check
        flowerReviewNodeObj['ratio'] = -1 
        flowerReviewNodeObj['size'] = 0 #Need to check
        flowerReviewNodeObj['sum'] = 6.5 #Need to check
        flowerReviewNodeObj['weight'] = 0 #Need to check
        flowerReviewNodeObj['xpos'] = 0 #Need to check
        flowerReviewNodeObj['ypos'] = 0 #Need to check
        flowerData[1].append(flowerReviewNodeObj)

    return flowerData


@csrf_exempt
def regenerate(request):
    db_connection = DBConnection()
    return_response = {}
    city_name = request.POST.get('city_name')
    country_name = request.POST.get('country_name')
    from_review_year = int(request.POST.get('from_review_year'))
    to_review_year = int(request.POST.get('to_review_year'))
    from_listing_year = int(request.POST.get('from_listing_year'))
    to_listing_year = int(request.POST.get('to_listing_year'))
    
    return_response = computeChartData(db_connection, city_name, country_name, from_review_year, to_review_year, from_listing_year, to_listing_year)

    return JsonResponse(return_response, safe=False)