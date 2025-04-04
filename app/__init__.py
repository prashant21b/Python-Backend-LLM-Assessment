from flask import Flask, jsonify
from .routes import api

def create_app():
    app = Flask(__name__)
    
  
    app.register_blueprint(api, url_prefix='/api')

  
    @app.route("/", methods=["GET"])
    def home():
        return jsonify({
            "message": " Welcome to the AI Stock Market Agent!",
            "usage": "POST /api/stock with JSON {'stock': '<stock name>'} to get real-time price and recommendation.",
            "example": {
                "method": "POST",
                "endpoint": "/api/stock",
                "body": {
                    "stock": "Apple"
                }
            }
        })

    return app
