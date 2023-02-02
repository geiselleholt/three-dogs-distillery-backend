# ! /usr/bin/env python3.6

"""
server.py
Stripe Sample.
Python 3.6 or newer required.
"""
import os
from flask import Flask, redirect, request, render_template_string
import stripe

YOUR_DOMAIN = 'http://localhost:4242'

app = Flask(__name__,
            static_url_path='',
            static_folder='public')


@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            customer_email='customer@example.com',
            submit_type='donate',
            billing_address_collection='auto',
            shipping_address_collection={
              'allowed_countries': ['US'],
            },
            line_items=[
                {
                    'price': '{{price_1MWyDHDxl1uhmuInoUrua1jL}}',
                    "adjustable_quantity": {"enabled": True, "minimum": 1, "maximum": 10},
                    'quantity': 1,
                },
                {
                    'price': '{{price_1MWyChDxl1uhmuIniS37uYiQ}}',
                    "adjustable_quantity": {"enabled": True, "minimum": 1, "maximum": 10},
                    'quantity': 1,
                },
                {
                    'price': '{{price_1MWyCHDxl1uhmuInp1qoBbhf}}',
                    "adjustable_quantity": {"enabled": True, "minimum": 1, "maximum": 10},
                    'quantity': 1,
                },
                {
                    'price': '{{price_1MWyBXDxl1uhmuInOl5mMJeY}}',
                    "adjustable_quantity": {"enabled": True, "minimum": 1, "maximum": 10},
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url="http://three-dogs-distillery.herokuapp.com/order/success?session_id={CHECKOUT_SESSION_ID}",
            cancel_url=YOUR_DOMAIN + '?canceled=true',
            automatic_tax={'enabled': True},
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)

@app.route('/order/success', methods=['GET'])
def order_success():
  session = stripe.checkout.Session.retrieve(request.args.get('session_id'))
  customer = stripe.Customer.retrieve(session.customer)

  return render_template_string('<html><body><h1>Thanks for your order, {{customer.name}}!</h1></body></html>', customer=customer)

if __name__ == '__main__':
    app.run(port=4242)