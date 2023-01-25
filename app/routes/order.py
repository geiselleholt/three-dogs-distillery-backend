from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.order import Order
from app.models.item import Item

bp = Blueprint("order_bp", __name__, url_prefix="/orders")