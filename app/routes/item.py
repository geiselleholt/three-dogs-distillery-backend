from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.item import Item
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

@bp.route("", methods=["GET"])
def read_all_items():
    items = Item.query.all()

    item_response = [item.to_dict() for item in items]

    return jsonify(item_response), 200

@bp.route("<email>", methods=["GET"])
def read_one_item(email):
    item_query = Item.query.filter(Item.email == email)

    item_response = [item.to_dict() for item in item_query]

    return jsonify(item_response), 200

@bp.route("/<item_id>/status", methods=["PUT"])
def update_status(item_id):
    item = validate_model(Item, item_id)
    request_body = request.get_json()
    item.status = request_body["status"]
    db.session.commit()

    return make_response(jsonify({"item": item.to_dict()}), 200)