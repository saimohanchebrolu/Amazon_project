from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)

CORS(app)


@app.route("/")
def home():
    return {
        "message": "Amazon Backend API is running successfully"
    }


@app.route("/api/products")
def get_products():
    with open("products.json", "r", encoding="utf-8") as file:
        products = json.load(file)

    return jsonify(products)


if __name__ == "__main__":
    app.run(debug=True)
