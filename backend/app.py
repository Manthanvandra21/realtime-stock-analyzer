# File: backend/app.py

from flask import Flask, jsonify, request

from data_fetcher import fetch_price, fetch_news
from db import (
    get_portfolio,
    get_risk_history,
    add_to_portfolio,
    save_risk
)
from logger import logger
from ml.model import calculate_risk

app = Flask(__name__)


# -------------------------
# Global Error Handler
# -------------------------
@app.errorhandler(Exception)
def handle_global_error(error):
    logger.error(f"UNHANDLED ERROR | {error}")
    return jsonify({"error": "Internal server error"}), 500


# -------------------------
# Validation Helper
# -------------------------
def is_valid_symbol(symbol):
    return isinstance(symbol, str) and symbol.strip() != ""


# -------------------------
# Root route
# -------------------------
@app.route("/", methods=["GET"])
def root():
    logger.info("API HIT | /")
    return jsonify({"status": "Backend running"}), 200


@app.route("/health", methods=["GET"])
def health():
    logger.info("API HIT | /health")
    return jsonify({"status": "ok"}), 200


# -------------------------
# Price API
# -------------------------
@app.route("/api/get_price/<symbol>", methods=["GET"])
def get_price(symbol):
    logger.info(f"API HIT | get_price | {symbol}")

    if not is_valid_symbol(symbol):
        return jsonify({"error": "Invalid stock symbol"}), 400

    try:
        symbol = symbol.upper()
        return jsonify(fetch_price(symbol)), 200

    except Exception as e:
        logger.error(f"PRICE FETCH FAILED | {symbol} | {e}")
        return jsonify({"error": "Failed to fetch price data"}), 500


# -------------------------
# Risk API (ML)
# -------------------------
@app.route("/api/get_risk/<symbol>", methods=["GET"])
def get_risk(symbol):
    logger.info(f"API HIT | get_risk | {symbol}")

    if not is_valid_symbol(symbol):
        return jsonify({"error": "Invalid stock symbol"}), 400

    try:
        symbol = symbol.upper()
        risk_score = calculate_risk(symbol)

        return jsonify({
            "symbol": symbol,
            "risk_score": risk_score,
            "explanation": "Deterministic dummy risk based on symbol length"
        }), 200

    except Exception as e:
        logger.error(f"RISK CALC FAILED | {symbol} | {e}")
        return jsonify({"error": "Failed to calculate risk score"}), 500


# -------------------------
# News API
# -------------------------
@app.route("/api/get_news/<symbol>", methods=["GET"])
def get_news(symbol):
    logger.info(f"API HIT | get_news | {symbol}")

    if not is_valid_symbol(symbol):
        return jsonify({"error": "Invalid stock symbol"}), 400

    try:
        symbol = symbol.upper()
        return jsonify(fetch_news(symbol)), 200

    except Exception as e:
        logger.error(f"NEWS FETCH FAILED | {symbol} | {e}")
        return jsonify({"error": "Failed to fetch news data"}), 500


# -------------------------
# Portfolio API (READ)
# -------------------------
@app.route("/api/portfolio", methods=["GET"])
def portfolio():
    logger.info("API HIT | GET /api/portfolio")

    try:
        data = get_portfolio()
        return jsonify(data), 200

    except Exception as e:
        logger.error(f"PORTFOLIO READ FAILED | {e}")
        return jsonify({"error": "Failed to fetch portfolio"}), 500


# -------------------------
# Risk History API
# -------------------------
@app.route("/api/risk_history/<symbol>", methods=["GET"])
def risk_history(symbol):
    logger.info(f"API HIT | GET /api/risk_history/{symbol}")

    if not is_valid_symbol(symbol):
        return jsonify({"error": "Invalid stock symbol"}), 400

    try:
        data = get_risk_history(symbol.upper())
        return jsonify(data), 200

    except Exception as e:
        logger.error(f"RISK HISTORY READ FAILED | {symbol} | {e}")
        return jsonify({"error": "Failed to fetch risk history"}), 500


# -------------------------
# Portfolio API (WRITE)
# -------------------------
@app.route("/api/portfolio/add", methods=["POST"])
def portfolio_add():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "Invalid JSON body"}), 400

    symbol = data.get("symbol")
    quantity = data.get("quantity")
    price = data.get("buy_price")

    if not is_valid_symbol(symbol):
        return jsonify({"error": "Invalid stock symbol"}), 400

    try:
        add_to_portfolio(symbol.upper(), quantity, price)
        return jsonify({"message": "Stock added"}), 201

    except Exception as e:
        logger.error(f"PORTFOLIO ADD FAILED | {e}")
        return jsonify({"error": "Database error"}), 500


# -------------------------
# Risk Save API
# -------------------------
@app.route("/api/risk/save", methods=["POST"])
def risk_save():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "Invalid JSON body"}), 400

    symbol = data.get("symbol")
    risk_score = data.get("risk_score")

    try:
        save_risk(symbol.upper(), risk_score)
        return jsonify({"message": "Risk saved"}), 201

    except Exception as e:
        logger.error(f"RISK SAVE FAILED | {e}")
        return jsonify({"error": "Database error"}), 500


if __name__ == "__main__":
    logger.info("Backend server started")
    app.run(debug=True)
