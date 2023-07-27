from twilio.rest import Client
import json
import os
from os import environ
import amqp_setup


account_sid = environ.get('account_sid') 
auth_token = environ.get('auth_token')
msg_service_sid = environ.get('msg_service_sid')

client = Client(account_sid, auth_token)

monitorBindingKey='#.notify'

def sendNotif():
    amqp_setup.check_setup()

    queue_name = 'Notification'  # can change later

    # set up a consumer and start to wait for coming messages
    amqp_setup.channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True)
    amqp_setup.channel.start_consuming()


def callback(channel, method, properties, body):
    print("\nReceived a request to notify customer by " + __file__)
    arr = json.loads(body)
    key = list(arr.keys())
    if key[0] == 'OrderSuccess':
        val = arr[key[0]]
        phoneNo = val[0]
        custID = val[1]
        orderID = val[2]
        cTime = val[3]
        loc = val[4]
        OrderConfirmation(phoneNo, custID, orderID, cTime, loc)
    elif key[0] == 'transactionSuccess':
        val = arr[key[0]]
        phoneNo = val[0]
        transAmt = val[1]
        transID = val[2]
        transactionCompleted(phoneNo, transAmt, transID)
    else:
        val = arr[key[0]]
        phoneNo = val[0]
        refAmt = val[1]
        refundCompleted(phoneNo, refAmt)
    print() # print a new line feed

def OrderConfirmation(phoneNo, custID, orderID, collectionTime, location):
    # phoneNum = '+6590907461'
    # custID = 'test_custID'
    # orderID = 'test_OrderID'
    # collectionTime = '8pm-9pm'

    phoneNum = phoneNo
    custID = custID
    orderID = orderID
    collectionTime = collectionTime
    location = location
    msgbody = 'Thank you for your order. Please show this message to the restaurant when collecting your Mystery Box. \n\n Order ID: ' + \
        orderID + '\n Customer ID: ' + custID + '\n Collection Time: Today at ' + \
        collectionTime + '\n Location: ' + location

    message = client.messages.create(
        messaging_service_sid=msg_service_sid,
        body=msgbody,
        to=phoneNum
    )

    print(message.sid)

# transaction completed function


def transactionCompleted(phoneNo, transAmt, transID):
    # phoneNum = '+6590907461'
    # transactionAmount = str(10.00)
    # transactionID = 'test_transactionID'

    phoneNum = phoneNo
    transactionAmount = transAmt
    transactionID = transID
    msgbody = 'Successful payment of $' + transactionAmount + \
        ' made to Mystery Box. Transaction ID is ' + transactionID + '.'

    message = client.messages.create(
        messaging_service_sid=msg_service_sid,
        body=msgbody,
        to=phoneNum
    )

    print(message.sid)

#transaction refunded function
def refundCompleted(phoneNo, refAmt):
    # phoneNum = '+6590907461' 
    # refundAmount = str(10.00)
    # refundID = 'test_transactionID'
    phoneNum = phoneNo
    refundAmount = refAmt
    msgbody = 'Successful refund of $' + refundAmount + ' made.'
    
    message = client.messages.create(  
                                    messaging_service_sid = msg_service_sid, 
                                    body = msgbody,      
                                    to = phoneNum 
                            ) 
    
    print(message.sid)


# execute this program only if it is run as a script (not by 'import')
if __name__ == "__main__":
    print("\nThis is " + os.path.basename(__file__), end='')
    print(": monitoring routing key '{}' in exchange '{}' ...".format(
        monitorBindingKey, amqp_setup.exchangename))
    sendNotif()
