from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from config import Config
from database import db

from models.product import Product
from models.user import User
from models.cart import Cart
from models.cart_item import CartItem

from routes.products import product_bp
from routes.auth import auth_bp
from routes.cart import cart_bp

app = Flask(__name__)

app.config.from_object(Config)

CORS(app)

jwt = JWTManager(app)

db.init_app(app)

app.register_blueprint(product_bp, url_prefix="/api")
app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(cart_bp, url_prefix="/api/cart")


@app.route("/")
def home():
    return {
        "message": "Amazon Backend API Running Successfully"
    }


if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
