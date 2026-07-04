import json

from app import app
from database import db
from models.product import Product


def seed_products():

    with app.app_context():

        Product.query.delete()

        db.session.commit()

        with open("products.json", "r", encoding="utf-8") as file:

            products = json.load(file)

        for item in products:

            rating = item.get("rating", {})

            product = Product(

                id=int(item["id"]),

                name=item["name"],

                image=item["image"],

                rating=rating.get("stars", 0),

                ratings_count=rating.get("count", 0),

                price=float(item["priceCents"]) / 100,

                keywords=", ".join(item.get("keywords", [])),

                description=item.get("description", ""),

                category=item.get("category", "General"),

                stock=100

            )

            db.session.add(product)

        db.session.commit()

        print("Products Imported Successfully")


if __name__ == "__main__":

    seed_products()
