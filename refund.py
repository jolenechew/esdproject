import stripe
import json
import os
import amqp_setup

# from flask import Flask
import pika
from invokes import invoke_http
from os import environ

# app = Flask(__name__)

orderURL = environ.get('order_URL') or "http://localhost:5001/order"
# get them
stripeSecretKey = os.environ.get(
    "stripeSecretKey") or "sk_test_51Mmaq9Kcs6la72jh0v2KAFQGvOWzqEVksC3hLHdDwf7UfuTRLxS62UVBJFxdZfnvGHcWLVmSuHLypH5kyHWGaQuy00wKtjTYqW"
stripePublicKey = os.environ.get(
    "stripePublicKey") or "pk_test_51Mmaq9Kcs6la72jh1ZMbbP5wP4yd0wbYZ43d1aDu09CDagPhLEet12Mcho1Nm2gApRmaPt8CCHrrFpWNsKb3h6De00PYaYjnbP"
stripe.api_key = stripeSecretKey
# stripe.api_key = stripeSecretKey

monitorBindingKey = '#.refund'


def requestRefund():
    amqp_setup.check_setup()

    queue_name = 'Refund'  # can change later

    # set up a consumer and start to wait for coming messages
    amqp_setup.channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True)
    amqp_setup.channel.start_consuming()


def callback(channel, method, properties, body):
    print("\nReceived a request to notify customer by " + __file__)
    print('\n-----------------------TEST 1 PASSED--------------------')
    arr = json.loads(body) 
    print(arr)
    val = arr['refund_details']
    orderID = arr["order_id"]
    print(orderID)

    print('\n\n---------------------------------1.Initiate Refund-------------------------------------')
    ref_json = initiate_refund(val[0], val[1])
    print('\n\n---------------------------------2.Refund Success-------------------------------------')

    print('\n\n---------------------------------3.Update Order Details-------------------------------------')
    result = update_order_status(orderID, ref_json)
    print(result)

def initiate_refund(chargeID, amt):
    print('\n\n--------Start Stripe Refund--------')

    amqp_setup.check_setup()

    amt = int(amt*100)
    refund = stripe.Refund.create(
        payment_intent=chargeID,
        amount=amt  # amount refunded in cents, MUST BE INT NOT FLOAT
    )
    print('\n\n--------End Stripe Refund--------')
    if refund.status == 'succeeded':
        refund_id = refund.id
        return {
            "refund_id": refund_id,
            "status": refund.status
        }
    return {
        "status": refund.status
    }

def update_order_status(orderID, refund):
    # update order
    if refund['status'] == 'succeeded':
        print('\n\n------------------------4. Start Update Order------------------------')
        refID = refund['refund_id']
        order_update = {"status": "REFUNDED", "refund_id": refID}
        order = invoke_http(orderURL + '/update/' +
                            str(orderID), method='PUT', json=order_update)
        print('\n\n------------------------5. End Update Order------------------------')
        print(order)
        code = order["code"]
        message = json.dumps(order)
        if code not in range(200, 300):
            routing_key = 'updateOrder.error'
            updateActivityandError(code, message, order, routing_key)
            return {
                "code": 500,
                "data": {"status": "Failed"},
                "message": "Order refund unsuccessful."
            }
        routing_key = 'updateOrder.info'
        updateActivityandError(code, message, order, routing_key)
        amqp_setup.channel.close()
        return {
            "code": 200,
            "data": {
                "cancel_order_result": order['data'],
                "status": "Success"
            },
            "message": "Order successfully refunded."
        }
    else:
        return {
            "code": 500,
            "data": {"cancel_order_result": None},
            "message": "Error processing refund."
        }
    
def updateActivityandError(code, message, order_result, rKey):
    print(rKey, code, message, order_result)
    amqp_setup.check_setup()
    if code not in range(200, 300):
        print('\n\n-----Publishing the error message with routing_key=' + rKey + '-----')

        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key=rKey,
                                         body=message, properties=pika.BasicProperties(delivery_mode=2))
        print("\nOrder status ({:d}) published to the RabbitMQ Exchange:".format(
            code), order_result)

    else:
        print('\n\n-----Publishing the info message with routing_key=' + rKey + '-----')
        amqp_setup.check_setup()

        # invoke_http(activity_log_URL, method="POST", json=order_result)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key=rKey,
                                         body=message, properties=pika.BasicProperties(delivery_mode=2))

    print("\nOrder published to RabbitMQ Exchange.\n")

# execute this program only if it is run as a script (not by 'import')
if __name__ == "__main__":
    print("\nThis is " + os.path.basename(__file__), end='')
    print(": monitoring routing key '{}' in exchange '{}' ...".format(
        monitorBindingKey, amqp_setup.exchangename))
    requestRefund()
