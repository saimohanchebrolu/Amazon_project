from database import db


class Payment(db.Model):

    __tablename__ = "payments"

    id = db.Column(db.Integer, primary_key=True)

    order_id = db.Column(
        db.Integer,
        db.ForeignKey("orders.id"),
        nullable=False
    )

    amount = db.Column(
        db.Float,
        nullable=False
    )

    payment_method = db.Column(
        db.String(50),
        nullable=False
    )

    payment_status = db.Column(
        db.String(50),
        default="SUCCESS"
    )

    transaction_id = db.Column(
        db.String(200),
        unique=True
    )

    payment_date = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )
