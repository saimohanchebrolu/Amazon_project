from flask import Blueprint, jsonify

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)

from services.order_service import OrderService

orders_bp = Blueprint("orders", __name__)


@orders_bp.route("/", methods=["GET"])
@jwt_required()
def get_orders():

    user_id = get_jwt_identity()

    orders = OrderService.get_orders(user_id)

    response = []

    for order in orders:

        response.append({

            "order_id": order.id,

            "total": order.total_amount,

            "status": order.status,

            "payment_status": order.payment_status,

            "created_at": order.created_at

        })

    return jsonify(response)


@orders_bp.route("/place", methods=["POST"])
@jwt_required()
def place_order():

    user_id = get_jwt_identity()

    response, status = OrderService.place_order(user_id)

    return jsonify(response), status


@orders_bp.route("/<int:order_id>", methods=["GET"])
@jwt_required()
def get_order(order_id):

    items = OrderService.get_order(order_id)

    response = []

    for item in items:

        response.append({

            "product": item.product.name,

            "image": item.product.image,

            "price": item.price,

            "quantity": item.quantity

        })

    return jsonify(response)
