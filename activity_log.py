from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from flask_cors import CORS
from datetime import datetime


import json
import os
from os import environ

import amqp_setup

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get(
    'dburl') or 'mysql+mysqlconnector://root:root@localhost:3306/activity_log'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}


############ 1. Creation of the database #####################################################
db = SQLAlchemy(app)
CORS(app)


class Logs(db.Model):
    __tablename__ = 'activity_log'

    activityID = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    activity_details = db.Column(db.String(64), nullable=False)

    def __intit__(self, activityID, created, activity_details):
        self.activityID = activityID
        self.created = created
        self.activity_details = activity_details

    def json(self):
        return {"activityID": self.activityID,
                "created": self.created,
                "activity_details": self.activity_details
                }


############ 2. Receiving the data from the queue #####################################################
monitorBindingKey = '#.info'


def receiveLog():
    amqp_setup.check_setup()

    queue_name = 'Activity_log'

    amqp_setup.channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True)
    amqp_setup.channel.start_consuming()


def callback(channel, method, properties, body):
    print("\nReceived an order log by " + __file__)
    processLog(json.loads(body))
#     print()

############ 3. Adding into Database, SQL #####################################################


def processLog(logs):
    print("Recording an log:")
    print(logs)
    # everyone need to change their MS to return message also!
    newLogs = logs['message']
    print(newLogs)

    # aLog = Logs(activity_details = newLogs)
    # db.session.add(aLog)
    # db.session.commit()

    with app.app_context():
        aLog = Logs(activity_details=newLogs)
        db.session.add(aLog)
        db.session.commit()

    # should be like this
    # {
    #     "code": 404,
    #     "data": {
    #         "order_id": 12345
    #     },
    #     "message": "Order not found." ---> REQUIRED
    # }


if __name__ == "__main__":
    print("\nThis is " + os.path.basename(__file__), end='')
    print(": monitoring routing key '{}' in exchange '{}' ...".format(
        monitorBindingKey, amqp_setup.exchangename))
    receiveLog()

# test =    {
#         "code": 404,
#         "data": {
#             "order_id": 12345
#         },
#         "message": "Order not found."
#     }
# processLog(test)
