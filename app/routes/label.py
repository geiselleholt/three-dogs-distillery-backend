from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.label import Label
from app.routes.helper_functions import validate_model

bp = Blueprint("label_bp", __name__, url_prefix="/labels")


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