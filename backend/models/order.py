from database import db


class Order(db.Model):

    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    total_amount = db.Column(
        db.Float,
        nullable=False
    )

    status = db.Column(
        db.String(50),
        default="PLACED"
    )

    payment_status = db.Column(
        db.String(50),
        default="PENDING"
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )
