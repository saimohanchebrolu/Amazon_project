import uuid

from database import db

from models.payment import Payment
from models.order import Order


class PaymentService:

    @staticmethod
    def make_payment(order_id, payment_method):

        order = Order.query.get(order_id)

        if not order:

            return {
                "message": "Order Not Found"
            },404

        transaction = str(uuid.uuid4())

        payment = Payment(

            order_id=order.id,

            amount=order.total_amount,

            payment_method=payment_method,

            transaction_id=transaction,

            payment_status="SUCCESS"

        )

        db.session.add(payment)

        order.payment_status="SUCCESS"

        db.session.commit()

        return {

            "message":"Payment Successful",

            "transaction_id":transaction,

            "amount":order.total_amount

        },200
