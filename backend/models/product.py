from database import db


class Product(db.Model):

    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(255), nullable=False)

    image = db.Column(db.String(500))

    rating = db.Column(db.Float)

    ratings_count = db.Column(db.Integer)

    price = db.Column(db.Float)

    keywords = db.Column(db.Text)

    description = db.Column(db.Text)

    category = db.Column(db.String(100))

    stock = db.Column(db.Integer, default=100)

    def to_dict(self):

        return {
            "id": self.id,
            "name": self.name,
            "image": self.image,
            "rating": self.rating,
            "ratings_count": self.ratings_count,
            "price": self.price,
            "keywords": self.keywords,
            "description": self.description,
            "category": self.category,
            "stock": self.stock
        }
