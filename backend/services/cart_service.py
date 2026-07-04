from database import db

from models.cart import Cart
from models.cart_item import CartItem


class CartService:

    @staticmethod
    def get_cart(user_id):

        cart = Cart.query.filter_by(user_id=user_id).first()

        if not cart:
            return []

        items = CartItem.query.filter_by(cart_id=cart.id).all()

        return items

    @staticmethod
    def add_to_cart(user_id, product_id, quantity):

        cart = Cart.query.filter_by(user_id=user_id).first()

        if not cart:

            cart = Cart(user_id=user_id)

            db.session.add(cart)

            db.session.commit()

        item = CartItem.query.filter_by(
            cart_id=cart.id,
            product_id=product_id
        ).first()

        if item:

            item.quantity += quantity

        else:

            item = CartItem(
                cart_id=cart.id,
                product_id=product_id,
                quantity=quantity
            )

            db.session.add(item)

        db.session.commit()

        return {"message": "Product Added Successfully"}

    @staticmethod
    def remove_from_cart(user_id, product_id):

        cart = Cart.query.filter_by(user_id=user_id).first()

        if not cart:
            return {"message": "Cart not found"}

        item = CartItem.query.filter_by(
            cart_id=cart.id,
            product_id=product_id
        ).first()

        if item:

            db.session.delete(item)

            db.session.commit()

        return {"message": "Item Removed Successfully"}

    @staticmethod
    def update_quantity(user_id, product_id, quantity):

        cart = Cart.query.filter_by(user_id=user_id).first()

        if not cart:
            return {"message": "Cart not found"}

        item = CartItem.query.filter_by(
            cart_id=cart.id,
            product_id=product_id
        ).first()

        if item:

            item.quantity = quantity

            db.session.commit()

        return {"message": "Cart Updated"}
