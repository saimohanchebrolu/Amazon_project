from flask import Blueprint, jsonify, request

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)

from services.cart_service import CartService

cart_bp = Blueprint("cart", __name__)


@cart_bp.route("/", methods=["GET"])
@jwt_required()
def get_cart():

    user_id = get_jwt_identity()

    items = CartService.get_cart(user_id)

    response = []

    for item in items:

        response.append({

            "product_id": item.product.id,

            "name": item.product.name,

            "image": item.product.image,

            "price": item.product.price,

            "quantity": item.quantity

        })

    return jsonify(response)


@cart_bp.route("/add", methods=["POST"])
@jwt_required()
def add_to_cart():

    user_id = get_jwt_identity()

    data = request.json

    return jsonify(

        CartService.add_to_cart(

            user_id,

            data["product_id"],

            data["quantity"]

        )

    )


@cart_bp.route("/update", methods=["PUT"])
@jwt_required()
def update_cart():

    user_id = get_jwt_identity()

    data = request.json

    return jsonify(

        CartService.update_quantity(

            user_id,

            data["product_id"],

            data["quantity"]

        )

    )


@cart_bp.route("/remove", methods=["DELETE"])
@jwt_required()
def remove_from_cart():

    user_id = get_jwt_identity()

    data = request.json

    return jsonify(

        CartService.remove_from_cart(

            user_id,

            data["product_id"]

        )

    )
