#################### Import all relevant libraries ##################################################
from flask import Flask, request, jsonify
from flask_cors import CORS

import os, sys

import requests
# from invokes import invoke_http

from math import radians, sin, cos, sqrt, asin

app = Flask(__name__)
CORS(app)

#################### Converting Customer Location to Lat and Long ####################################
def get_cust_location(address):
    #print("Start of get_cust_location")

    API_KEY = 'AIzaSyDla7hHpUucckrVqSjdXTY_kUGHj8x2uUM'

    params  = {
        'key': API_KEY,
        'address': address
    }

    base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
    response = requests.get(base_url,params=params).json()
    response.keys()

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # raise an exception for 4xx and 5xx errors
        data = response.json()
        if data['status'] == 'OK':
            geometry = data['results'][0]['geometry']
            lat = geometry['location']['lat']
            lon = geometry['location']['lng']
            return ({'lat':lat, 'lng': lon})
        else:
            print(f'Geocoding failed. Status: {data["status"]}')
    except requests.exceptions.HTTPError as err:
        print(f'Error: {err}')
    except requests.exceptions.RequestException as err:
        print(f'Request error: {err}')
    
    #print("End of get_cust_location")

################# Finding the nearest location ########################################################

@app.route('/location', methods = ['POST']) 
def find_nearest_location():

    print("Start of find_nearest_location")
    data = request.json # {starting_loc:"1 hack drive, menlo park, CA" , rest_loc:[{lat:...., lng:.....,rest_id:.....},{lat:...., lng:.....},{lat:...., lng:.....}] }
   # print(data)

    # return ({'lat':lat, 'lng': lon})
    data["starting_location"] = get_cust_location(data.get('starting_location'))

    #data = {starting_location: , rest_loc: }
    #starting_location = {lat:...., lng:.....}
    #restaurant_location = [{'lat':37.48007705012013, 'lng':-122.14532593683853},{'lat':37.48053919210831, 'lng':-122.15144075520307},{'lat':37.477040045901575, 'lng':-122.15352062600218},{'lat':37.477139080546856, 'lng':-122.16080017167964},{'lat':37.46779623020498, 'lng':-122.14041744300732},
    #                       {'lat':37.46779623020498, 'lng':-122.1516903396774},{'lat':37.46600271717554, 'lng':-122.1568760578018},{'lat':37.46600271717554, 'lng':-122.1568760578018},{'lat':37.469206976332174, 'lng':-122.16603436035237},{'lat':37.469206976332174, 'lng':-122.16603436035237},
    #                       {'lat':1.3823169660466292, 'lng':103.68905007456796},{'lat':37.465231300843634, 'lng':-122.18633215021532},{'lat':37.46888062276618, 'lng':-122.18027645639775},{'lat':37.48068777703546, 'lng':-122.16188508879591},{'lat':37.47789932093983, 'lng':-122.13844731073895}
    #                       ]

    # customer_location = data['starting_location'] #make sure that this is in the complex MS and under payload 
    # restaurant_location = data['restaurant_location'] #make sure that this is in the complex MS and under payload 

    customer_location = data.get('starting_location') #make sure that this is in the complex MS and under payload 
    restaurant_location = data.get('restaurant_location')['data'] #make sure that this is in the complex MS and under payload
    print("THIS IS THE LOCATIONS")
    print(customer_location) 
    print(restaurant_location)
    print("THIS IS THE LOCATIONS END")

    # process the locations
    top_20_locations = get_nearest_locations(customer_location['lat'],customer_location['lng'],restaurant_location)

    # check if the .json thing works for here
    nearest_locations = top_20_locations

    # return the status here
    if nearest_locations:
        return jsonify(
            {
                "code": 200,
                "data": nearest_locations,
                "message": "Nearest 20 locations successfully retrieved"
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": data["starting_location"],
            "message": "Unable to suggest top 20 nearest locaion."
        }
    ), 404



def haversine(lat1, lon1, lat2, lon2):
    print("Start of haversine")
    """
    Calculate the great circle distance between two points 
    on the Earth (specified in decimal degrees)
    """
    # Convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # Haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers
    print("End of haversine")
    return c * r

def get_nearest_locations(latitude, longitude, locations):
    print("Start of get_nearest_locations")
    # print(type(latitude))
    # print(type(longitude))
    """
    Get the nearest top 20 locations based on the provided latitude, longitude, and list of locations
    """
    # Calculate distances between the given location and all locations in the list
    distances = []
    for location in locations:
        dist = haversine(latitude, longitude, location[3], location[4])
        distances.append((location, dist))
    
    # Sort the list of locations by distance in ascending order and return the top 20 locations
    sorted_distances = sorted(distances, key=lambda x: x[1])
    nearest_locations = [x[0] for x in sorted_distances[:20]]
    print("End of get_nearest_locations")
    return nearest_locations

if __name__ == '__main__':
    app.run(port=5200,host="0.0.0.0", debug=True)