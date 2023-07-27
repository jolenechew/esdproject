from flask import Flask, request, jsonify
from flask_cors import CORS


import os
import sys
# from os import environ


import requests
from invokes import invoke_http


import pika
import json
import amqp_setup
from os import environ


app = Flask(__name__)
CORS(app)


orderURL = environ.get('order_URL') or "http://localhost:5001/order"
boxURL = environ.get('box_URL') or "http://localhost:5000/box"


############# code added here #########################################################


@app.route('/cancel_order', methods=['POST'])
def CancelOrder():

    orderID = request.get_json()["orderID"]
    # global orderID
    # orderID = int(OrderID)

    try:
        # get order details
        print(orderID)
        print('\n-----1. Getting order details from Order MS-----')
        order = invoke_http(orderURL + '/' + str(orderID))  # type = dict
        print(order)
        code = order["code"]
        message = json.dumps(order)
        if code not in range(200, 300):
            routing_key = 'retrieveDetails.error'
            updateActivityandError(code, message, order, routing_key)
            return {
                "code": 500,
                "data": {"cancel_order_result": order['data'], "status": "Failed"},
                "message": "Unable to find Order."
            }, 500
        routing_key = 'retrieveDetails.info'
        activity = json.dumps({
            "code": 200,
            "data": {"cancel_order_result": order['data'], "status": "Success"},
            "message": "Retrieved Box successfully."
        })
        updateActivityandError(code, activity, order, routing_key)

        print('\n\n--------2. Sending to ProcessCancelOrder--------')
        ProcessCancelOrder(order['data'])
        print('\n\n--------8. End ProcessCancelOrder--------')

        return {
        "code": 200,
        "data": {"cancel_order_result": order, "status": "Success"},
        "message": "Cancel Order success."
        }

        # try:
        #     print('\n\n--------8. Send to update_order_status--------')
        #     status = refundDetails['status']
        #     result = update_order_status(status)
        #     print('\n\n----------9. End update_order_status----------')
        #     return jsonify(result), result["code"]
        # except:
        #     result = {
        #         "code": 500,
        #         "data": {
        #             "status": "Failed"
        #         },
        #         "message": "Order refundID unable to be updated."
        #     }
        #     return jsonify(result), result["code"]

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        ex_str = str(e) + " at " + str(exc_type) + ": " + \
            fname + ": line " + str(exc_tb.tb_lineno)
        print(ex_str)

        return jsonify({
            "code": 500,
            "message": "cancel_order.py internal error: " + ex_str
        }), 500

    # # if reached here, not an int.
    # except:
    #     print('\n\n--------Error not Int--------')
    #     return jsonify({
    #         "code": 400,
    #         "message": "Not an integer"
    #     }), 400


def ProcessCancelOrder(orderDetails):
    # update inventory
    amqp_setup.check_setup()

    print('\n\n--------3. Start Update Box Inventory--------')
    quantity = orderDetails["quantity"]
    boxID = str(orderDetails["boxID"])
    box = invoke_http(boxURL + '/' + boxID)

    quantity += box["data"]["quantity"]  # new quantity to update
    quantity_json = {"quantity": quantity}
    box = invoke_http(boxURL + '/' + boxID, method='PUT', json=quantity_json)
    code = box["code"]
    message = json.dumps(box)
    if code not in range(200, 300):
        routing_key = 'updateInventory.error'
        updateActivityandError(code, message, box, routing_key)
        return {
            "code": 500,
            "data": {"cancel_order_result": box, "status": "Failed"},
            "message": "Unable to update inventory."
        }, 500
    routing_key = 'updateInventory.info'
    updateActivityandError(code, message, box, routing_key)
    print('\n\n--------4. End update Box Inventory--------')

    # start refunding
    global phoneNo
    global amount
    orderID = orderDetails["order_id"]
    chargeID = orderDetails["charge_id"]
    amount = str(orderDetails["total_bill"])  # is string
    phoneNo = '+65' + str(orderDetails["customer_number"])
    print('\n\n----------------------5. Send to refund.py----------------------')
    startRefund(chargeID, amount, orderID)

    print('\n\n----------------------6. Send notification----------------------')
    msg = json.dumps({
        "refundDetails": [phoneNo, amount]
    })
    amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='refund.notify',
                                        body=msg, properties=pika.BasicProperties(delivery_mode=2))
    print('\n\n----------------------7. Notification sent----------------------')

def startRefund(chargeID, Amt, orderID):
    print('\n\n--------StartRefund Function called--------')
    amqp_setup.check_setup()
    amount = float(Amt)
    msg = f"""
    {{
        "refund_details": ["{chargeID}", {amount:.2f}],
        "order_id": {orderID}
    }}
    """  # stringify JSON

    # Send a message with reply-to header under properties
    amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename,
                                     routing_key='refund.refund',
                                     properties=pika.BasicProperties(delivery_mode=2),
                                     body=msg)  # body need to include chargeID and amount, send as "{'refund_details': [chargeID, Amt]}"
    # Listen for the response message on the reply-to queue
    print('\n\n--------End of startRefund--------')

def updateActivityandError(code, message, order_result, rKey):
    print('ddd', rKey, code, message, order_result)
    amqp_setup.check_setup()
    print('====')
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


if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) +
          " for cancelling an order...")
    app.run(host="0.0.0.0", port=5500, debug=True)
