from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.customer import Customer
from app.models.order import Order

bp = Blueprint("customer_bp", __name__, url_prefix="/customers")