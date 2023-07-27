'''
Things to remember to do:
-- Link this MS to login (change the user ID in the database based on the firebase)
-- Change the user Id to link with firebase
-- Create a docker file for your current microservice
'''
#################### Import libraries ###############################################################################
from flask import Flask, request, jsonify
from flask_cors import CORS

import os
import sys

import requests
from invokes import invoke_http
from os import environ
import json

import pika
import json
import amqp_setup

app = Flask(__name__)
CORS(app)

#################### Microservices URL #############################################################################

location_URL = environ.get("location_URL")
box_URL = environ.get("box_URL")
rest_URL = environ.get("rest_URL")
get_rest_from_box_ms = "http://restaurant:5300/restaurant"

#################### Call on Near By Complex MS ####################################################################


@app.route("/near_by", methods=['POST'])
def near_by():
    # Simple check of input format and data of the request are JSON
    if request.is_json:
        try:
            # customer_location: refers to the location that the customer gave {'cust_location': '30 Sembawang Dr, Singapore 757713'}
            customer_location = request.get_json()
            print("\nReceived an request in JSON:", customer_location)

            # do the actual work
            customer_location = customer_location["customer_location"]
            # result = processNearByLocation(customer_location)
            result = processNearByLocation(customer_location)

            print("--------------result: ", result)

            code = result["code"]
            print("--------------status code: ", code)
            message = result['message']

            ######################## Send to AMQP ##########################################
            if code not in range(200, 300):
                routing_key = 'retrieveDetails.error'
                updateActivityandError(code, message, result, routing_key)
                return {
                    "code": 500,
                    "data": result,
                    "message": message
                }
            routing_key = 'retrieveDetails.info'
            activity = json.dumps({
                "code": 200,
                "data": {"nearby_result": message},
                "message": 'Retrieve Box successful.'
            })
            updateActivityandError(code, activity, result, routing_key)
            ####################### End of AMQP ##########################################

            return jsonify(result), result["code"]

            # return {
            #     "code": 200,
            #     "data": box_info, #would be a array of all the box information (dict) taken from box ms
            #     "message": "Sent box information for top 20 recommended nearby places."
            # }

        except Exception as e:
            # Unexpected error in code
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + \
                fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)

            return jsonify({
                "code": 500,
                "message": "nearby.py internal error: " + ex_str
            }), 500

    # if reached here, not a JSON request.
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " + str(request.get_data())
    }), 400

#################### Main bulk of Near By Complex MS #################################################################


def processNearByLocation(customer_location):
    ###### 2. Ask Mystery Box MS for array of rest_id that posted today ##############################################

    print('\n-----Invoking Mystery Box microservice-----')
    box_result = invoke_http(box_URL)
    print(box_result)
    print("this is the box result", box_result)
    # response_dict = json.loads(box_result)
    boxes_list = box_result['data']['boxes']
    print("this is the box list", boxes_list)

    print('\n-----test-----')
    # create an empty list to store the restaurant IDs
    restaurant_ids = []
    for box in boxes_list:
        restaurant_ids.append(box['restaurant_id'])
    print('restaurant_ids:', restaurant_ids)
    print('\n-----End of Mystery Box microservice-----')

    ###### 3. Ask Restaurant MS for lat, lng based on restaurant_id array ###########################################

    print('\n-----Invoking Restaurant microservice-----')
    # restaurant_locations: Returns the list of dictionary of the restaurant information ~ restaurant that posted
    msg = {
        "restaurant_ids": restaurant_ids
    }
    restaurant_locations = invoke_http(rest_URL, method="POST", json=msg)
    print('restaurant_locations:', restaurant_locations)
    print('\n-----End of Restaurant microservice-----')

    ###### 4. Ask Location MS for top 20 nearest recommendation based on restaurant_location array #################
    print('\n-----Invoking Location microservice-----')
    nearby_locations = invoke_http(location_URL, method="POST", json={
                                   "starting_location": customer_location, "restaurant_location": restaurant_locations})
    print('order_result:', nearby_locations)
    print('\n-----End of Location microservice-----')

    ###### 5. Return the box information for the top 20 restaurant base on their restaurant_ids #################

    # nearby would return the below
    print("\n-----Start of trying to return the box information-----")
    # {"restaurant_id": , "restaurant_name": , "restaurant_location": , "latitude": , "longitude": }
    restaurant_info = nearby_locations['data']
    print("restaurant_info", restaurant_info)
    # loop through the rest_info and then query the box ms to give you the information and then send it back
    box_info = []
    for restaurant in restaurant_info:
        restaurant_id = restaurant[0]
        # call on the box URL
        print("restaurant_id", restaurant_id)
        box_indi_info = invoke_http(box_URL + "/rest/" + str(restaurant_id))
        print("box_indi_info", box_indi_info)
        box_array = box_indi_info['data']['box']
        for box in box_array:
            box_info.append(box)
    print("box_info", box_info)

    box_info = box_info[:20]
    if box_info:
        return {
            "code": 200,
            # would be a array of all the box information (dict) taken from box ms
            "data": box_info,
            "message": "Sent box information for top 20 recommended nearby places."
        }

    return {
        "code": 400,
        "message": "Unable to find top 20 recommended nearby places."
    }

#################### AMQP activity log and error handling ############################################################


def updateActivityandError(code, message, result, rKey):
    amqp_setup.check_setup()

    if code not in range(200, 300):
        print('\n\n-----Publishing the error message with routing_key=' + rKey + '-----')

        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key=rKey,
                                         body=message, properties=pika.BasicProperties(delivery_mode=2))
        print("\nStatus ({:d}) published to the RabbitMQ Exchange:".format(
            code), result)

    else:
        print('\n\n-----Publishing the info message with routing_key=' + rKey + '-----')

        # invoke_http(activity_log_URL, method="POST", json=order_result)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key=rKey,
                                         body=message, properties=pika.BasicProperties(delivery_mode=2))

    print("\nPublished to RabbitMQ Exchange.\n")


#################### Execute this program if it is run as a main script (not by 'import') ############################
if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) +
          " for placing an order...")
    app.run(host="0.0.0.0", port=5400, debug=True)
