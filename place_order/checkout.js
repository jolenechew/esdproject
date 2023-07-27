console.log("yes");
const stripe = Stripe(
  "pk_test_51Mmaq9Kcs6la72jh1ZMbbP5wP4yd0wbYZ43d1aDu09CDagPhLEet12Mcho1Nm2gApRmaPt8CCHrrFpWNsKb3h6De00PYaYjnbP"
);

const place_order_URL = "http://localhost:5100/place_order";
const payment_URL = "http://localhost:6002/payment";
const box_url = "http://localhost:5000/box";
const restaurant_url = "http://localhost:5300/restaurant";

// HERE CREATE PAYMENT ELEMENT
const options = {
  mode: "payment",
  amount: 1099, // this one needs to be generated dynamically from UI NOTE
  currency: "sgd",
  appearance: {
    theme: "stripe",
  },
};

// Set up Stripe.js and Elements to use in checkout form
const elements = stripe.elements(options);

// HERE Create and mount the Payment Element
const paymentElement = elements.create("payment", {
  layout: {
    type: "accordion",
    defaultCollapsed: false,
    radios: true,
    spacedAccordionItems: false,
  },
  customer: {
    customerNumber: "123456",
    quantity: "1",
  },
});
paymentElement.mount("#payment-element");
