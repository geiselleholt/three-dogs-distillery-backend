from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.order import Order
from app.models.item import Item
from app.routes.helper_functions import validate_model

bp = Blueprint("order_bp", __name__, url_prefix="/orders")


@bp.route("", methods=["POST"])
def create_order():
    request_body = request.get_json()
    new_order = Order.from_dict(request_body)

    db.session.add(new_order)
    db.session.commit()

    order_dict = new_order.to_dict(request_body)

    return make_response(jsonify({"order": order_dict}), 201)


@bp.route("<order_id>", methods=["DELETE"])
def delete_order(order_id):
    order = validate_model(Order, order_id)

    db.session.delete(order)
    db.session.commit()

    return {"details": f"order {Order.order_id} successfully deleted"}



@bp.route("<customer_id>", methods=["GET"])
def read_all_orders_for_one_customer(customer_id):
    order_query = Order.query.filter(Order.customer_id == customer_id)

    order_response = [order.to_dict() for order in order_query]

    return jsonify(order_response), 200


@bp.route("<order_id>/status", methods=["PUT"])
def increase_likes(order_id):
    order = validate_model(Order, order_id)

    request_body = request.get_json()
    order.status = request_body["status"]
    db.session.commit()

    return make_response(jsonify({"order": order.to_dict()}), 200)