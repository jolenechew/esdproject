import os
import stripe
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

stripe_secret_key = os.environ.get(
    "STRIPE_SECRET_KEY") or "sk_test_51Mmaq9Kcs6la72jh0v2KAFQGvOWzqEVksC3hLHdDwf7UfuTRLxS62UVBJFxdZfnvGHcWLVmSuHLypH5kyHWGaQuy00wKtjTYqW"

stripe_publish_key = os.environ.get(
    "STRIPE_PUBLISHABLE_KEY") or "pk_test_51Mmaq9Kcs6la72jh1ZMbbP5wP4yd0wbYZ43d1aDu09CDagPhLEet12Mcho1Nm2gApRmaPt8CCHrrFpWNsKb3h6De00PYaYjnbP"
stripe_keys = {
    "secret_key": stripe_secret_key,
    "publishable_key": stripe_publish_key,
}
stripe.api_key = stripe_keys["secret_key"]


@app.route('/payment/create-payment-intent', methods=["POST"])
def create_payment_intent():
    # get payment details
    data = request.get_json()
    amount = data["amount"]
    currency = data["currency"]

    try:

        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            automatic_payment_methods={"enabled": True}
        )

        # retrieve the Payment Intent ID from the response
        payment_intent_id = intent['id']

        # stripe.PaymentIntent.confirm(
        #     payment_intent_id
        # )

        # return client secret to Place an Order (to confirm payment)
        return jsonify({
            "clientSecret": intent['client_secret'],
            "paymentIntentId": payment_intent_id,
            "code": 201,
            "message": "Payment intent sucessfully created",

        })

    except Exception as e:
        return jsonify(error=str(e)), 403


# @app.route("/confirm-payment", methods=["POST"])
# def confirm_payment():
#     data = request.get_json()

#     try:
#         # Retrieve payment intent
#         intent = stripe.PaymentIntent.retrieve(data["payment_intent_id"])

#         # confirm payment intent with the provided payment method and payment details
#         # NOTE If payment fails, the PaymentIntent will transition to the requires_payment_method status. If payment succeeds, the PaymentIntent will transition to the succeeded status

#         # NOTE TO UI PEOPLE:  payment_method_id is expected to be included in the POST request data that is sent to the Flask route, either in an HTML form input field or in a JSON payload.
#         intent.confirm(
#             payment_method=data["payment_method_id"], metadata=data["metadata"])

#         # return success response to Place an Order
#         return jsonify({"message": "Payment Intent success", "code": 201, }, 201)

#     except Exception as e:
#         return jsonify({"message": "Payment failed to create Payment Intent", "error": str(e)}), 400


if __name__ == '__main__':
    print("This is flask for " + os.path.basename(__file__) + ": payment ...")
    app.run(host='0.0.0.0', port=6002, debug=True)
