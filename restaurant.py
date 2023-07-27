from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get(
    'dburl') or 'mysql+mysqlconnector://root@localhost:3306/restaurant'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app)


class Restaurant(db.Model):
    __tablename__ = 'restaurant'

    restaurant_id = db.Column(db.Integer, primary_key=True)
    restaurant_name = db.Column(db.String(64), nullable=False)
    restaurant_location = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    def __init__(self, restaurant_id, restaurant_name, restaurant_location, latitude, longitude):
        self.restaurant_id = restaurant_id
        self.restaurant_name = restaurant_name
        self.restaurant_location = restaurant_location
        self.latitude = latitude
        self.longitude = longitude

    def json(self):
        return {"restaurant_id": self.restaurant_id, "restaurant_name": self.restaurant_name, "restaurant_location": self.restaurant_location, "latitude": self.latitude, "longitude": self.longitude}


#################### GET ALL RESTAURANTS #################################
@app.route("/restaurant")
def get_all():
    restaurantlist = Restaurant.query.all()
    if len(restaurantlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "restaurants": [restaurant.json() for restaurant in restaurantlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no restaurants."
        }
    ), 404


#################### GET A RESTAURANT BY ID #################################
@app.route("/restaurant/<int:restaurant_id>")
def find_by_restaurant_id(restaurant_id):
    restaurant = Restaurant.query.filter_by(
        restaurant_id=restaurant_id).first()
    if restaurant:
        return jsonify(
            {
                "code": 200,
                "data": restaurant.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Restaurant not found."
        }
    ), 404


#################### FILTER BY RESTAURANT_ID #################################
@app.route("/restaurant", methods=["POST"])
def get_by_restaurant_id():
    try:
        # Retrieve restaurant_ids from the request body
        data = request.get_json()
        restaurant_ids = data["restaurant_ids"]

        # Retrieve entries from the database that match the restaurant_ids
        restaurant_entries = Restaurant.query.filter(
            Restaurant.restaurant_id.in_(restaurant_ids)).all()

        # Create a nested list containing the data for each entry
        restaurant_entry_data = [[entry.restaurant_id, entry.restaurant_location,
                                  entry.restaurant_name, entry.latitude, entry.longitude] for entry in restaurant_entries]

        # Return a JSON response containing the list of arrays
        return jsonify({
            "code": 200,
            "data": restaurant_entry_data
        })
    except Exception as e:
        # Return a JSON response with a 500 status code and error message
        return jsonify({
            "code": 500,
            "message": "An error occurred while processing your request: {}".format(str(e))
        })


if __name__ == '__main__':
    app.run(port=5300, host='0.0.0.0', debug=True)
