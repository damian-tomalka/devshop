from decimal import Decimal

from flask import Blueprint, current_app, jsonify, request
from sqlalchemy import text

from .models import Product, db
from .validation import validate_product

bp = Blueprint("api", __name__)


@bp.get("/health")
def health():
    try:
        db.session.execute(text("SELECT 1"))
        return jsonify(status="ok", db="ok"), 200
    except Exception:
        current_app.logger.exception("baza nie odpowiada")
        db.session.rollback()
        return jsonify(status="error", db="fail"), 503


@bp.get("/api/products")
def list_products():
    products = db.session.scalars(db.select(Product).order_by(Product.id)).all()
    return jsonify([p.to_dict() for p in products]), 200


@bp.get("/api/products/<int:product_id>")
def get_product(product_id: int):
    product = db.session.get(Product, product_id)
    if product is None:
        return jsonify(error="nie znaleziono"), 404
    return jsonify(product.to_dict()), 200


@bp.post("/api/products")
def create_product():
    data = request.get_json(silent=True)
    errors = validate_product(data)
    if errors:
        return jsonify(errors=errors), 400

    product = Product(name=data["name"].strip(), price=Decimal(str(data["price"])))
    db.session.add(product)
    db.session.commit()
    current_app.logger.info("dodano produkt id=%s", product.id)
    return jsonify(product.to_dict()), 201
