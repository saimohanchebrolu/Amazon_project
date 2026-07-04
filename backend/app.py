from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from config import Config
from database import db

# Import Models
from models.product import Product
from models.user import User

# Import Routes
from routes.products import product_bp
from routes.auth import auth_bp

app = Flask(__name__)

# Load Configuration
app.config.from_object(Config)

# Enable CORS
CORS(app)

# Initialize JWT
jwt = JWTManager(app)

# Initialize Database
db.init_app(app)

# Register Blueprints
app.register_blueprint(product_bp, url_prefix="/api")
app.register_blueprint(auth_bp, url_prefix="/api/auth")


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
