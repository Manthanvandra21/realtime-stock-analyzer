# File: backend/app.py

from flask import Flask, jsonify

# Import dummy data functions
from backend.data_fetcher import fetch_price, fetch_news

# Import ML risk function
from ml.model import calculate_risk

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/api/get_price/<symbol>", methods=["GET"])
def get_price(symbol):
    data = fetch_price(symbol.upper())
    return jsonify(data), 200


@app.route("/api/get_risk/<symbol>", methods=["GET"])
def get_risk(symbol):
    # Read stock symbol
    symbol = symbol.upper()

    # Call ML risk logic (dummy-based)
    risk_score, explanation = calculate_risk(symbol)

    # Return structured JSON response
    return jsonify({
        "symbol": symbol,
        "risk_score": risk_score,
        "explanation": explanation
    }), 200


@app.route("/api/get_news/<symbol>", methods=["GET"])
def get_news(symbol):
    data = fetch_news(symbol.upper())
    return jsonify(data), 200


if __name__ == "__main__":
    app.run(debug=True)
