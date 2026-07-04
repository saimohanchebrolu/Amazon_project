from database import db


class Product(db.Model):

    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(255), nullable=False)

    description = db.Column(db.Text)

    price = db.Column(db.Float)

    image = db.Column(db.String(500))

    category = db.Column(db.String(100))

    rating = db.Column(db.Float)

    stock = db.Column(db.Integer)
