# File: backend/app.py

from flask import Flask, jsonify

# Import dummy data functions
from data_fetcher import fetch_price, fetch_news

# Import ML risk function
from ml.model import calculate_risk

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/api/get_price/<symbol>", methods=["GET"])
def get_price(symbol):
    data = fetch_price(symbol)
    return jsonify(data), 200


@app.route("/api/get_risk/<symbol>", methods=["GET"])
def get_risk(symbol):
    # Call ML risk logic
    risk_score, explanation = calculate_risk(symbol)

    return jsonify({
        "symbol": symbol.upper(),
        "risk_score": risk_score,
        "explanation": explanation
    }), 200


@app.route("/api/get_news/<symbol>", methods=["GET"])
def get_news(symbol):
    data = fetch_news(symbol)
    return jsonify(data), 200


if __name__ == "__main__":
    app.run(debug=True)
