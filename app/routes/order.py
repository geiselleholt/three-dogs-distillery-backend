from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.order import Order
from app.models.item import Item

bp = Blueprint("order_bp", __name__, url_prefix="/orders")

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message": f"{cls.__name__} {model_id} invalid"}, 400))

    model = cls.query.get(model_id)

    if not model:
        abort(make_response({"message": f"{cls.__name__} {model_id} not found"}, 404))

    return model


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


@bp.route("<order_id>/like", methods=["PUT"])
def increase_likes(order_id):
    order = validate_model(Order, order_id)

    request_body = request.get_json()
    order.likes_count = request_body["likes_count"]
    db.session.commit()

    return make_response(jsonify({"order": order.to_dict()}), 200)