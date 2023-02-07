# ! /usr/bin/env python3.6

"""
server.py
Stripe Sample.
Python 3.6 or newer required.
"""
import os
from flask import Blueprint, redirect, request, render_template_string
import stripe
from dotenv import load_dotenv

load_dotenv()

bp = Blueprint("server_bp", __name__, url_prefix="")

stripe.api_key = os.environ.get(
    "STRIPE_API_KEY")

customer = stripe.Customer.create()
print(customer.last_response.request_id)

@bp.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    
    try:
        checkout_session = stripe.checkout.Session.create(
            customer_email='customer@example.com',
            billing_address_collection='auto',
            shipping_address_collection={
              'allowed_countries': ['US'],
            },
            line_items=[
                {
                    'price': 'price_1MWxxDDxl1uhmuInz4weCs0W',
                    "adjustable_quantity": {"enabled": True, "minimum": 1, "maximum": 10},
                    'quantity': 1,
                },
                {
                    'price': 'price_1MXBRQDxl1uhmuIn2IB2h6TR',
                    "adjustable_quantity": {"enabled": True, "minimum": 1, "maximum": 10},
                    'quantity': 1,
                },
                # {
                #     'price': 'price_1MWyCHDxl1uhmuInp1qoBbhf',
                #     "adjustable_quantity": {"enabled": True, "minimum": 1, "maximum": 10},
                #     'quantity': 1,
                # },
                # {
                #     'price': 'price_1MYhL3Dxl1uhmuInj1gtIaGB',
                #     "adjustable_quantity": {"enabled": True, "minimum": 1, "maximum": 10},
                #     'quantity': 1,
                # },
            ],
            mode='payment',
            success_url="http://three-dogs-distillery.herokuapp.com/order/success?session_id={CHECKOUT_SESSION_ID}",
            cancel_url="http://three-dogs-distillery.herokuapp.com" + '?canceled=true',
            automatic_tax={'enabled': True},
        )
    
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)

@bp.route('/order/success', methods=['GET'])
def order_success():
  session = stripe.checkout.Session.retrieve(request.args.get('session_id'))
  customer = stripe.Customer.retrieve(session.customer)

  return render_template_string('<html><body><h1>Thanks for your order, {{customer.name}}!</h1></body></html>', customer=customer)
