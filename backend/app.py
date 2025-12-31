# File: backend/app.py

from flask import Flask, jsonify

# Import ML risk function
from ml.model import calculate_risk

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


# Dummy API routes
@app.route("/api/get_price/<symbol>", methods=["GET"])
def get_price(symbol):
    return jsonify({"message": "Coming soon"}), 200


@app.route("/api/get_risk/<symbol>", methods=["GET"])
def get_risk(symbol):
    """
    Connects backend API to ML risk logic.
    """
    # Call ML risk function
    risk_score, explanation = calculate_risk(symbol)

    # Return structured JSON response
    return jsonify({
        "symbol": symbol.upper(),
        "risk_score": risk_score,
        "explanation": explanation
    }), 200


@app.route("/api/get_news/<symbol>", methods=["GET"])
def get_news(symbol):
    return jsonify({"message": "Coming soon"}), 200


if __name__ == "__main__":
    app.run(debug=True)
