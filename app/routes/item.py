from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.item import Item
from app.models.label import Label

bp = Blueprint("item_bp", __name__, url_prefix="/items")