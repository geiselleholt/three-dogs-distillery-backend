from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.customer import Customer
from app.models.order import Order

bp = Blueprint("customer_bp", __name__, url_prefix="/customers")

@bp.route("", methods=["POST"])
def create_customer():
    request_body = request.get_json()
    check_duplicates(request_body["user_name"])

    new_customer = Customer.from_dict(request_body)

    db.session.add(new_customer)
    db.session.commit()

    customer_dict = new_customer.to_dict()

    return make_response(jsonify({"customer": customer_dict}), 201)


def check_duplicates(customer_user_name):
    """
    check whether or not a customer with a particular user_name already exists
    """
    test_customer = Customer.query.filter(customer.user_name == customer_user_name).first()
    if test_customer is not None:
        abort(
            make_response(
                {
                    "details": f"Customer {customer_user_name} already exists, please enter a unique user_name"
                },
                400,
            )
        )


@bp.route("", methods=["GET"])
def read_all_customers():
    customers = Customer.query.all()

    customers_response = [customer.to_dict() for customer in customers]

    return jsonify(customers_response), 200

@bp.route("<user_name>/orders", methods=["GET"])
def read_all_orders(user_name):
    sort_query = request.args.get("sort")
    order_query = Order.query.filter(Order.user_name == user_name)
    if sort_query == "asc":
        order_query = order_query.order_by(Order.message.asc())
    elif sort_query == "likes":
        order_query = order_query.order_by(order.likes_count.desc())
    else:
        order_query = order_query.order_by(Order.order_id.desc())
    order_response = [order.to_dict() for order in order_query]

    return jsonify(order_response), 200


# @bp.route("<customer_id>/orders", methods=["GET"])
# def read_all_orders(customer_id):
#     sort_query = request.args.get("sort")
#     order_query = Order.query.filter(Order.customer_id == customer_id)
#     if sort_query == "asc":
#         order_query = order_query.order_by(Order.message.asc())
#     elif sort_query == "likes":
#         order_query = order_query.order_by(order.likes_count.desc())
#     else:
#         order_query = order_query.order_by(Order.order_id.desc())
#     order_response = [order.to_dict() for order in order_query]

#     return jsonify(order_response), 200