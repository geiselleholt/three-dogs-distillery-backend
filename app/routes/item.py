from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.item import Item
from app.models.label import Label
from app.routes.helper_functions import validate_model

bp = Blueprint("item_bp", __name__, url_prefix="/items")


@bp.route("", methods=["POST"])
def create_item():
    request_body = request.get_json()
    new_item = Item.from_dict(request_body)

    db.session.add(new_item)
    db.session.commit()

    item_dict = new_item.to_dict()

    return make_response(jsonify({"item": item_dict}), 201)

@bp.route("<item_id>", methods=["DELETE"])
def delete_item(item_id):
    item = validate_model(Item, item_id)

    db.session.delete(item)
    db.session.commit()

    return {"details": f"Item {item.item_id} successfully deleted"}

@bp.route("<order_id>", methods=["GET"])
def read_all_items_for_one_order(order_id):
    item_query = Item.query.filter(Item.order_id == order_id)

    item_response = [item.to_dict() for item in item_query]

    return jsonify(item_response), 200
