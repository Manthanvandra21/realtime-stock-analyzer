# File: backend/app.py

from flask import Flask, jsonify, request

from backend.data_fetcher import fetch_price, fetch_news
from ml.model import calculate_risk
from backend.db import (
    get_portfolio,
    get_risk_history,
    add_to_portfolio,
    save_risk
)
from backend.logger import logger

app = Flask(__name__)


# -------------------------
# Root route
# -------------------------
@app.route("/", methods=["GET"])
def root():
    logger.info("API HIT | /")
    return jsonify({
        "status": "Backend running",
        "apis": [
            "get_price",
            "get_risk",
            "get_news",
            "portfolio",
            "risk_history",
            "portfolio_add",
            "risk_save"
        ]
    }), 200


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

    try:
        if not symbol or not symbol.strip():
            return jsonify({"error": "Stock symbol is required"}), 400

        symbol = symbol.upper()
        data = fetch_price(symbol)

        return jsonify({"symbol": symbol, "data": data}), 200

    except Exception as e:
        logger.error(f"PRICE FETCH FAILED | {symbol} | {e}")
        return jsonify({"error": "Failed to fetch price data"}), 500


# -------------------------
# Risk API (ML)
# -------------------------
@app.route("/api/get_risk/<symbol>", methods=["GET"])
def get_risk(symbol):
    logger.info(f"API HIT | get_risk | {symbol}")

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
        logger.error(f"RISK CALC FAILED | {symbol} | {e}")
        return jsonify({"error": "Failed to calculate risk score"}), 500


# -------------------------
# News API
# -------------------------
@app.route("/api/get_news/<symbol>", methods=["GET"])
def get_news(symbol):
    logger.info(f"API HIT | get_news | {symbol}")

    try:
        if not symbol or not symbol.strip():
            return jsonify({"error": "Stock symbol is required"}), 400

        symbol = symbol.upper()
        data = fetch_news(symbol)

        return jsonify({"symbol": symbol, "data": data}), 200

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
        return jsonify({"count": len(data), "data": data}), 200

    except Exception as e:
        logger.error(f"PORTFOLIO READ FAILED | {e}")
        return jsonify({"error": "Failed to fetch portfolio"}), 500


# -------------------------
# Risk History API (READ)
# -------------------------
@app.route("/api/risk_history/<symbol>", methods=["GET"])
def risk_history(symbol):
    logger.info(f"API HIT | GET /api/risk_history/{symbol}")

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

    except Exception as e:
        logger.error(f"RISK HISTORY READ FAILED | {symbol} | {e}")
        return jsonify({"error": "Failed to fetch risk history"}), 500


# -------------------------
# Portfolio API (WRITE)
# -------------------------
@app.route("/api/portfolio/add", methods=["POST"])
def portfolio_add():
    logger.info("API HIT | POST /api/portfolio/add")

    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON body"}), 400

    symbol = data.get("symbol")
    quantity = data.get("quantity")
    price = data.get("price")

    if not symbol or quantity is None or price is None:
        logger.warning("VALIDATION FAILED | portfolio add")
        return jsonify({"error": "symbol, quantity and price are required"}), 400

    success = add_to_portfolio(symbol.upper(), quantity, price)

    if success:
        logger.info(f"PORTFOLIO ADD SUCCESS | {symbol}")
        return jsonify({"message": "Stock added to portfolio"}), 201

    logger.error(f"PORTFOLIO ADD FAILED | {symbol}")
    return jsonify({"error": "Failed to write to database"}), 500


# -------------------------
# Risk API (WRITE)
# -------------------------
@app.route("/api/risk/save", methods=["POST"])
def risk_save():
    logger.info("API HIT | POST /api/risk/save")

    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON body"}), 400

    symbol = data.get("symbol")
    risk_score = data.get("risk_score")

    if not symbol or risk_score is None:
        logger.warning("VALIDATION FAILED | risk save")
        return jsonify({"error": "symbol and risk_score are required"}), 400

    success = save_risk(symbol.upper(), risk_score)

    if success:
        logger.info(f"RISK SAVE SUCCESS | {symbol}")
        return jsonify({"message": "Risk saved"}), 201

    logger.error(f"RISK SAVE FAILED | {symbol}")
    return jsonify({"error": "Failed to write to database"}), 500


if __name__ == "__main__":
    logger.info("Backend server started")
    app.run(debug=True)
