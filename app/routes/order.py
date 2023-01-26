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

    order_dict = new_order.to_dict()

    return make_response(jsonify({"order": order_dict}), 201)


@bp.route("<order_id>", methods=["DELETE"])
def delete_order(order_id):
    order = validate_model(Order, order_id)

    db.session.delete(order)
    db.session.commit()

    return {"details": f"order {Order.order_id} successfully deleted"}


@bp.route("<order_id/items", methods=["GET"])
def read_all_items_for_one_order(order_id):
    item_query = Item.query.filter(Item.order_id == order_id)

    item_response = [item.to_dict() for item in item_query]

    return jsonify(item_response), 200