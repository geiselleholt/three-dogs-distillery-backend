# ! /usr/bin/env python3.6

"""
server.py
Stripe Sample.
Python 3.6 or newer required.
"""
import os
from flask import Blueprint, redirect, request
import stripe
from dotenv import load_dotenv
from app.models.item import Item

load_dotenv()

bp = Blueprint("server_bp", __name__, url_prefix="")

stripe.api_key = os.environ.get(
    "STRIPE_API_KEY")

# customer = stripe.Customer.create()
# print(customer.last_response.request_id)

@bp.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():

    item_query = Item.query.filter(Item.item_id == request.form['itemId'])
    item_response = [item.to_dict() for item in item_query]

    stripe_quantity = item_response[0]["quantity"]

    stripe_line_items =[]

    brandy = {
                    'price': 'price_1MZHq5Dxl1uhmuInddRde6LT',
                    'quantity': stripe_quantity,
    }

    whiskey = {
                    'price': 'price_1MZHrFDxl1uhmuInhXAXa7de',
                    'quantity': stripe_quantity,
    }

    vodka = {
                    'price': 'price_1MYjvzDxl1uhmuIn9JEruSqc',
                    'quantity': stripe_quantity,
    }

    moonshine = {
                    'price': 'price_1MYju9Dxl1uhmuInNLCR4lMG',
                    'quantity': stripe_quantity,
    }

    bourbon = {
                    'price': 'price_1MWxxDDxl1uhmuInz4weCs0W',
                    'quantity': stripe_quantity,
    }

    mason_jar = {
                    'price': 'price_1MZHdeDxl1uhmuInlt6UJkfI',
                    'quantity': stripe_quantity,
    }

    mini_mason_jar = {
                    'price': 'price_1MZHdFDxl1uhmuInoFkSE3JO',
                    'quantity': stripe_quantity,
    }

    standard = {
                    'price': 'price_1MZHc7Dxl1uhmuInBbXXm100',
                    'quantity': stripe_quantity,
    }

    minis = {
                    'price': 'price_1MZHcvDxl1uhmuIn8s9cLwEN',
                    'quantity': stripe_quantity,
    }

    fancy = {
                    'price': 'price_1MZHcPDxl1uhmuInFDBuKmT1',
                    'quantity': stripe_quantity,
    }

    apple = {
                    'price': 'price_1MZHF9Dxl1uhmuInQpIo1Fuz',
                    'quantity': stripe_quantity,
    }

    citrus = {
                    'price': 'price_1MZHbiDxl1uhmuInB6Fd68gA',
                    'quantity': stripe_quantity,
    }

    candy = {
                    'price': 'price_1MZHGUDxl1uhmuInd6Xg097E',
                    'quantity': stripe_quantity,
    }

    espresso = {
                    'price': 'price_1MZHGwDxl1uhmuInE3TqU0eP',
                    'quantity': stripe_quantity,
    }

    cherry = {
                    'price': 'price_1MZHFxDxl1uhmuInEDVEiM8Z',
                    'quantity': stripe_quantity,
    }
    
    if item_response[0]["spirit"] == 'Brandy':
        stripe_line_items.append(brandy)

    if item_response[0]["spirit"] == 'Whiskey':
        stripe_line_items.append(whiskey)

    if item_response[0]["spirit"] == 'Vodka':
        stripe_line_items.append(vodka)

    if item_response[0]["spirit"] == 'Moonshine':
        stripe_line_items.append(moonshine)

    if item_response[0]["spirit"] == 'Bourbon':
        stripe_line_items.append(bourbon)

    if item_response[0]["bottle"] == 'Mason Jar':
        stripe_line_items.append(mason_jar)

    if item_response[0]["bottle"] == 'Mini Mason Jars':
        stripe_line_items.append(mini_mason_jar)

    if item_response[0]["bottle"] == 'Standard':
        stripe_line_items.append(standard)
    
    if item_response[0]["bottle"] == 'Mini Bottles':
        stripe_line_items.append(minis)

    if item_response[0]["bottle"] == 'Fancy':
        stripe_line_items.append(fancy)

    if item_response[0]["flavor"] == 'Apple':
        stripe_line_items.append(apple)

    if item_response[0]["flavor"] == 'Cherry':
        stripe_line_items.append(cherry)

    if item_response[0]["flavor"] == 'Espresso':
        stripe_line_items.append(espresso)

    if item_response[0]["flavor"] == 'Citrus':
        stripe_line_items.append(citrus)

    if item_response[0]["flavor"] == 'Watermelon Candy':
        stripe_line_items.append(candy)
    

    try:
        checkout_session = stripe.checkout.Session.create(
            customer_email='customer@example.com',
            billing_address_collection='auto',
            shipping_address_collection={
              'allowed_countries': ['US'],
            },
            line_items= stripe_line_items,
            mode='payment',
            success_url="https://three-dogs-backend.herokuapp.com/thankyou",
            cancel_url="https://three-dogs-backend.herokuapp.com/cancelorder",
            automatic_tax={'enabled': True},
        )
    
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)
