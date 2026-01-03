# File: backend/app.py

from flask import Flask, jsonify

from backend.data_fetcher import fetch_price, fetch_news
from ml.model import calculate_risk

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/api/get_price/<symbol>", methods=["GET"])
def get_price(symbol):
    try:
        if not symbol or not symbol.strip():
            return jsonify({"error": "Stock symbol is required"}), 400

        data = fetch_price(symbol.upper())
        return jsonify(data), 200

    except Exception as e:
        return jsonify({
            "error": "Failed to fetch price data"
        }), 500


@app.route("/api/get_risk/<symbol>", methods=["GET"])
def get_risk(symbol):
    try:
        if not symbol or not symbol.strip():
            return jsonify({"error": "Stock symbol is required"}), 400

        symbol = symbol.upper()
        risk_score, explanation = calculate_risk(symbol)

        return jsonify({
            "symbol": symbol,
            "risk_score": risk_score,
            "explanation": explanation
        }), 200

    except Exception as e:
        return jsonify({
            "error": "Failed to calculate risk score"
        }), 500


@app.route("/api/get_news/<symbol>", methods=["GET"])
def get_news(symbol):
    try:
        if not symbol or not symbol.strip():
            return jsonify({"error": "Stock symbol is required"}), 400

        data = fetch_news(symbol.upper())
        return jsonify(data), 200

    except Exception as e:
        return jsonify({
            "error": "Failed to fetch news data"
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
