import os
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

# Load .env for local development
load_dotenv()

app = Flask(__name__)
# Allow requests from any origin
CORS(app, resources={r"/*": {"origins": "*"}}, methods=["GET"])

# Static product list
PRODUCTS = [
    {"id": 1, "name": "Dog Food", "price": 19.99},
    {"id": 2, "name": "Cat Food", "price": 34.99},
    {"id": 3, "name": "Bird Seeds", "price": 10.99},
]


@app.get("/products")
def get_products():
    return jsonify(PRODUCTS), 200


@app.get("/health")
def health():
    # Simple health endpoint for Azure troubleshooting
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    # Azure App Service sets PORT; default to 3030 for local runs
    port = int(os.getenv("PORT", "3030"))
    app.run(host="0.0.0.0", port=port)
