from flask import Flask
from flask_cors import CORS

from config import Config
from database import db

from routes.products import product_bp


app = Flask(__name__)

app.config.from_object(Config)

CORS(app)

db.init_app(app)

app.register_blueprint(product_bp, url_prefix="/api")


@app.route("/")
def home():

    return {
        "message": "Amazon Backend API Running Successfully"
    }


if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(host="0.0.0.0", port=5000, debug=True)
