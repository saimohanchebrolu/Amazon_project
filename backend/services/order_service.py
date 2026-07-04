from database import db

from models.cart import Cart
from models.cart_item import CartItem
from models.order import Order
from models.order_item import OrderItem


class OrderService:

    @staticmethod
    def place_order(user_id):

        cart = Cart.query.filter_by(user_id=user_id).first()

        if not cart:
            return {"message": "Cart Empty"}, 400

        cart_items = CartItem.query.filter_by(cart_id=cart.id).all()

        if len(cart_items) == 0:
            return {"message": "Cart Empty"}, 400

        total = 0

        for item in cart_items:
            total += item.product.price * item.quantity

        order = Order(
            user_id=user_id,
            total_amount=total
        )

        db.session.add(order)

        db.session.commit()

        for item in cart_items:

            order_item = OrderItem(
                order_id=order.id,
                product_id=item.product_id,
                quantity=item.quantity,
                price=item.product.price
            )

            db.session.add(order_item)

        CartItem.query.filter_by(cart_id=cart.id).delete()

        db.session.commit()

        return {
            "message": "Order Placed Successfully",
            "order_id": order.id
        }, 201

    @staticmethod
    def get_orders(user_id):

        return Order.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_order(order_id):

        return OrderItem.query.filter_by(order_id=order_id).all()
