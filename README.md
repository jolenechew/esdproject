# Mystery Food Box

## Overview

Mystery Food Box hopes to manage food waste and increase the ease of food recycling, where restaurants can sell their leftover food items and customers can enjoy food at a lower price compared to during business hours from restaurants nearest them.


## User Scenarios
Customer logs in via Google Provider and searches for the 20 nearest restaurants selling food boxes
Customer places an order and conducts payment
Customer cancels an order and receives a refund


## Features
### Authentication
Users are able to sign up with a username and password or conveniently log in using their Google account, all with the use of Google Login Service Provider and Firebase Authentication.

### Food Boxes Listings
Users are able to browse through the vast selection of food boxes uploaded by the restaurants.

### Nearest Food Boxes
Users would be able to enter their address and filter the food boxes based on the location of the nearest restaurants using Google Geocoding API.

### Place an Order
Users can place an order and conduct payment, all within one click, using the complex microservice of Place an Order and Stripe API.

### Refund
Users can refund their food boxes if they did not enjoy them as much as we hoped they would.

### Notify
Users are notified through SMS about their order status, payment status and refund status.


## Running the application 
1. Run WAMP server
2. Import all sql files into phpMyAdmin MySql 
    - Box.sql
    - Order.sql
    - Activity_log.sql
    - Error.sql
    - Restaurant.sql
3. cd esdProject and run docker-compose up in the terminal
4. Use localhost to access login.html in the browser.


### Login
- Select an account type that the user is logging in as: Customer or Restaurant.
- If user does not have an account, user can create one by clicking the sign up button and filling in the required information. 
- If user does not have an account and does not want to create an account, user can also click on “Sign in with Google'' to login with any Google account, and user will be redirected to the index page to view all the foodboxes available for the day.


### Stripe Testing
For testing purposes, in the success case, input “4242 4242 4242 4242” for card number, and any number for expiry date and CVC number. 
For failure cases, input “4000 0000 0000 0002” for card number, and any number for expiry date and CVC number. For more test cases, you can refer to Stripe Documentation.


## Clone files to server
Go to an empty directory in the server and clone the application.
bash
git clone https://github.com/kllygh/esdProject.git
