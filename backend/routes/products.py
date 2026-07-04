from flask import Blueprint, jsonify
import json

product_bp = Blueprint("products", __name__)


@product_bp.route("/api/products", methods=["GET"])
def get_products():

    with open("products.json", "r", encoding="utf-8") as file:
        products = json.load(file)

    return jsonify(products)
