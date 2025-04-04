from flask import Blueprint, request, jsonify
from .stock_fetcher import fetch_stock_price
from .agent import get_stock_analysis

api = Blueprint('api', __name__)

@api.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Welcome to the AI Stock Market Agent.",
        "description": "This API provides the latest stock price and a buy/sell/hold recommendation based on analysis.",
        "usage": "Send a POST request to /api/stock with a JSON body containing a 'stock' field.",
        "example_request": {
            "method": "POST",
            "endpoint": "/api/stock",
            "headers": {
                "Content-Type": "application/json"
            },
            "body": {
                "stock": "Apple"
            }
        }
    }), 200

@api.route('/stock', methods=['POST'])
def analyze_stock():
    data = request.json
    stock = data.get("stock")

    if not stock:
        return jsonify({"error": "Missing 'stock' field"}), 400

    price = fetch_stock_price(stock)
    if price is None:
        return jsonify({"error": "Could not fetch price"}), 404

    recommendation = get_stock_analysis(stock, price)
    return jsonify({
        "stock": stock,
        "price": price,
        "recommendation": recommendation,
        "note": "This includes a real-time stock price and an AI-generated buy/sell/hold suggestion."
    })
