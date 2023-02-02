from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.label import Label
from app.routes.helper_functions import validate_model

bp = Blueprint("label_bp", __name__, url_prefix="/labels")


@bp.route("", methods=["POST"])
def create_label():
    request_body = request.get_json()
    new_label = Label.from_dict(request_body)

    db.session.add(new_label)
    db.session.commit()

    label_dict = new_label.to_dict()

    return make_response(jsonify({"label": label_dict}), 201)


@bp.route("<label_id>", methods=["DELETE"])
def delete_label(label_id):
    label = validate_model(Label, label_id)

    db.session.delete(label)
    db.session.commit()

    return {"details": f"label {label_id} successfully deleted"}


@bp.route("<item_id>", methods=["GET"])
def read_all_labels_for_one_item(item_id):
    label_query = Label.query.filter(Label.item_id == item_id)

    label_response = [label.to_dict() for label in label_query]

    return jsonify(label_response), 200