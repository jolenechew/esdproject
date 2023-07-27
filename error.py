from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from flask_cors import CORS
from datetime import date

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
    __tablename__ = 'error'

    errorID = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, nullable=False)
    error_details = db.Column(db.String(64), nullable=False)

    def __intit__(self, errorID, created, error_details):
        self.errorID = errorID
        self.created = created
        self.error_details = error_details

    def json(self):
        return {"errorID": self.errorID,
                "created": self.created,
                "error_details": self.error_details
                }


############ 2. Receiving the data from the queue #####################################################

monitorBindingKey = '*.error'


def receiveError():
    amqp_setup.check_setup()

    queue_name = "Error"

    amqp_setup.channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True)
    amqp_setup.channel.start_consuming()


def callback(channel, method, properties, body):
    print("\nReceived an error by " + __file__)
    processError(body)
    print()


############ 3. Adding into Database, SQL #####################################################

def processError(errorMsg):
    print("Printing the error message:")
    try:
        error = json.loads(errorMsg)
        print("--JSON:", error)
        # everyone need to change their MS to return message also!
        newError = error['message']

        # db.session.add(newError)
        # db.session.commit()
        with app.app_context():
            eLog = Logs(error_details=newError)
            db.session.add(eLog)
            db.session.commit()

        # should be like this
        # {
        #     "code": 404,
        #     "data": {
        #         "order_id": 12345
        #     },
        #     "message": "Order not found." ---> REQUIRED
        # }

    except Exception as e:
        print("--NOT JSON:", e)
        print("--DATA:", errorMsg)
    print()


if __name__ == "__main__":
    print("\nThis is " + os.path.basename(__file__), end='')
    print(": monitoring routing key '{}' in exchange '{}' ...".format(
        monitorBindingKey, amqp_setup.exchangename))
    receiveError()
