import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import exc

from datetime import datetime
import json
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get(
    'dburl') or 'mysql+mysqlconnector://root@localhost:3306/order'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)


class Order(db.Model):
    __tablename__ = 'orders'

    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_number = db.Column(db.Integer, nullable=False)
    customer_id = db.Column(db.String, nullable=False)
    restaurant_id = db.Column(db.Integer, nullable=False)
    boxID = db.Column(db.Integer, nullable=False)  # change to boxID
    charge_id = db.Column(db.String(50), nullable=False, default='NaN')
    refund_id = db.Column(db.String(50), nullable=False, default='NaN')
    quantity = db.Column(db.Integer, nullable=False)
    total_bill = db.Column(db.Numeric(precision=5, scale=2))
    transaction_no = db.Column(db.Integer)
    payment_method = db.Column(db.String(50))
    currency = db.Column(db.String(50))
    status = db.Column(db.String(10), nullable=False, default="NEW")
    created = db.Column(db.DateTime, nullable=False, default=datetime.now)
    modified = db.Column(db.DateTime, nullable=False,
                         default=datetime.now, onupdate=datetime.now)

    # NOTE The __init__ method is not required because SQLAlchemy provides a default constructor for the class that handles the initialization of the attributes based on the database schema

    def json(self):
        order_info = {
            'order_id': self.order_id,
            'customer_number': self.customer_number,
            'customer_id': self.customer_id,
            'restaurant_id': self.restaurant_id,
            'boxID': self.boxID,
            'charge_id': self.charge_id,
            'refund_id': self.refund_id,
            'quantity': self.quantity,
            'total_bill': self.total_bill,
            'transaction_no': self.transaction_no,
            'payment_method': self.payment_method,
            'currency': self.currency,
            'status': self.status,
            'created': self.created,
            'modified': self.modified
        }

        return order_info


@app.route("/order/customer/<customer_id>")
def get_all(customer_id):
    # orderlist = Order.query.all()
    orderlist = Order.query.filter_by(customer_id=customer_id).all()
    # list of Order objects.
    if len(orderlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "orders": [order.json() for order in orderlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no orders."
        }
    ), 404


@app.route("/order/<int:order_id>")
def find_by_order_id(order_id):
    order = Order.query.filter_by(order_id=order_id).first()
    if order:
        return jsonify(
            {
                "code": 200,
                "data": order.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "order_id": order_id
            },
            "message": "Order not found."
        }
    ), 404


@app.route("/order/new", methods=['POST'])
def create_order():
    data = request.get_json()
    order = Order(status="NEW", **data)

    try:
        db.session.add(order)
        db.session.commit()

    except exc.IntegrityError as e:
        # rollback the transaction to avoid partially committing the changes
        db.session.rollback()
        return jsonify(
            {
                "code": 400,
                "message": "An order with this ID already exists.",
                "data": data
            }
        ), 400
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating the order. " + str(e),
                "data": data
            }
        ), 500

    # convert a JSON object to a string and print
    print(json.dumps(order.json(), default=str))
    print()

    return jsonify(
        {
            "code": 201,
            "message": "Order created successfully",
            "data": order.json()
        }
    ), 201


@app.route("/order/update/<int:order_id>", methods=['PUT'])
def update_order(order_id):
    order = Order.query.filter_by(order_id=order_id).first()
    # update payment details also

    # if no order with that id
    if not order:
        return jsonify(
            {
                "code": 404,
                "data": {
                    "order_id": order_id
                },
                "message": "Order not found."
            }
        ), 404

    # update status
    data = request.get_json()
    for field in ['status', 'charge_id', 'refund_id', 'payment_method', 'currency']:
        if field in data:
            # The setattr() function sets the value of the specified attribute of the specified object.
            setattr(order, field, data[field])
    try:
        db.session.commit()

    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "order_id": order_id
                },
                "message": "An error occurred while updating the order. " + str(e)
            }
        ), 500

    return jsonify(
        {
            "code": 200,
            "message": "Order updated successfully.",
            "data": order.json()
        }
    ), 200


if __name__ == '__main__':
    print("This is flask for " + os.path.basename(__file__) + ": manage orders ...")
    app.run(host='0.0.0.0', port=5001, debug=True)
