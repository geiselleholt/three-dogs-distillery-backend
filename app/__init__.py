from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "SQLALCHEMY_DATABASE_URI")

    app.config["STRIPE_API_KEY"] = os.environ.get(
        "STRIPE_API_KEY")

    # from app.models.customer import Customer
    # from app.models.order import Order
    from app.models.item import Item
    from app.models.label import Label

    db.init_app(app)
    migrate.init_app(app, db)

    # from .routes import customer
    # from .routes import order
    from .routes import item
    from .routes import label
    from .routes import server

    # app.register_blueprint(customer.bp)
    # app.register_blueprint(order.bp)
    app.register_blueprint(item.bp)
    app.register_blueprint(label.bp)
    app.register_blueprint(server.bp)

    CORS(app)
    return app
