# File: backend/app.py

from flask import Flask, jsonify

from backend.data_fetcher import fetch_price, fetch_news
from ml.model import calculate_risk

app = Flask(__name__)


# -------------------------
# Root route (demo ready)
# -------------------------
@app.route("/", methods=["GET"])
def root():
    print("[INFO] Root endpoint called")
    return jsonify({
        "status": "Backend running",
        "apis": ["get_price", "get_risk", "get_news"]
    }), 200


@app.route("/health", methods=["GET"])
def health():
    print("[INFO] Health check called")
    return jsonify({"status": "ok"}), 200


# -------------------------
# Price API
# -------------------------
@app.route("/api/get_price/<symbol>", methods=["GET"])
def get_price(symbol):
    print(f"[INFO] get_price API called with symbol: {symbol}")

    try:
        if not symbol or not symbol.strip():
            return jsonify({
                "symbol": "",
                "error": "Stock symbol is required"
            }), 400

        symbol = symbol.upper()
        data = fetch_price(symbol)

        return jsonify({
            "symbol": symbol,
            "data": data
        }), 200

    except Exception:
        return jsonify({
            "symbol": symbol.upper() if symbol else "",
            "error": "Failed to fetch price data"
        }), 500


# -------------------------
# Risk API (ML connected)
# -------------------------
@app.route("/api/get_risk/<symbol>", methods=["GET"])
def get_risk(symbol):
    print(f"[INFO] get_risk API called with symbol: {symbol}")

    try:
        if not symbol or not symbol.strip():
            return jsonify({
                "symbol": "",
                "error": "Stock symbol is required"
            }), 400

        symbol = symbol.upper()
        print("[INFO] Triggering ML risk calculation")

        risk_score, explanation = calculate_risk(symbol)

        return jsonify({
            "symbol": symbol,
            "risk_score": risk_score,
            "explanation": explanation
        }), 200

    except Exception:
        return jsonify({
            "symbol": symbol.upper() if symbol else "",
            "error": "Failed to calculate risk score"
        }), 500


# -------------------------
# News API
# -------------------------
@app.route("/api/get_news/<symbol>", methods=["GET"])
def get_news(symbol):
    print(f"[INFO] get_news API called with symbol: {symbol}")

    try:
        if not symbol or not symbol.strip():
            return jsonify({
                "symbol": "",
                "error": "Stock symbol is required"
            }), 400

        symbol = symbol.upper()
        data = fetch_news(symbol)

        return jsonify({
            "symbol": symbol,
            "data": data
        }), 200

    except Exception:
        return jsonify({
            "symbol": symbol.upper() if symbol else "",
            "error": "Failed to fetch news data"
        }), 500


if __name__ == "__main__":
    print("[INFO] Starting backend server")
    app.run(debug=True)
