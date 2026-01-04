# File: backend/app.py

from flask import Flask, jsonify

from backend.data_fetcher import fetch_price, fetch_news
from ml.model import calculate_risk
from backend.db import get_portfolio, get_risk_history

app = Flask(__name__)


# -------------------------
# Root route
# -------------------------
@app.route("/", methods=["GET"])
def root():
    return jsonify({
        "status": "Backend running",
        "apis": [
            "get_price",
            "get_risk",
            "get_news",
            "portfolio",
            "risk_history"
        ]
    }), 200


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


# -------------------------
# Price API
# -------------------------
@app.route("/api/get_price/<symbol>", methods=["GET"])
def get_price(symbol):
    try:
        if not symbol or not symbol.strip():
            return jsonify({"error": "Stock symbol is required"}), 400

        symbol = symbol.upper()
        data = fetch_price(symbol)

        return jsonify({
            "symbol": symbol,
            "data": data
        }), 200

    except Exception:
        return jsonify({"error": "Failed to fetch price data"}), 500


# -------------------------
# Risk API (ML)
# -------------------------
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

    except Exception:
        return jsonify({"error": "Failed to calculate risk score"}), 500


# -------------------------
# News API
# -------------------------
@app.route("/api/get_news/<symbol>", methods=["GET"])
def get_news(symbol):
    try:
        if not symbol or not symbol.strip():
            return jsonify({"error": "Stock symbol is required"}), 400

        symbol = symbol.upper()
        data = fetch_news(symbol)

        return jsonify({
            "symbol": symbol,
            "data": data
        }), 200

    except Exception:
        return jsonify({"error": "Failed to fetch news data"}), 500


# -------------------------
# Portfolio API (DB READ)
# -------------------------
@app.route("/api/portfolio", methods=["GET"])
def portfolio():
    try:
        data = get_portfolio()
        return jsonify({
            "count": len(data),
            "data": data
        }), 200

    except Exception:
        return jsonify({"error": "Failed to fetch portfolio"}), 500


# -------------------------
# Risk History API (DB READ)
# -------------------------
@app.route("/api/risk_history/<symbol>", methods=["GET"])
def risk_history(symbol):
    try:
        if not symbol or not symbol.strip():
            return jsonify({"error": "Stock symbol is required"}), 400

        symbol = symbol.upper()
        data = get_risk_history(symbol)

        return jsonify({
            "symbol": symbol,
            "count": len(data),
            "data": data
        }), 200

    except Exception:
        return jsonify({"error": "Failed to fetch risk history"}), 500


if __name__ == "__main__":
    app.run(debug=True)
