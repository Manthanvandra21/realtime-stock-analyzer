# File: ml/model.py
# Purpose:
# Risk scoring model for Stock Price Analyzer
# This module performs ONLY risk calculation.
# It does NOT connect to database or perform logging.

# -------------------------------------------------
# IMPORTANT FLOW (Future Automation)
# -------------------------------------------------
# ML Model → Backend API → Database (risk_history / risk_logs)
#
# The ML layer returns only the risk_score (int).
# Backend is responsible for:
# - Calling this function
# - Storing results in DB
# - Logging responses
# -------------------------------------------------


def calculate_risk(price_volatility, market_trend):
    """
    Calculate risk score based on market indicators.

    Parameters:
    price_volatility (float): Volatility value from market data
    market_trend (str): 'bullish', 'neutral', or 'bearish'

    Returns:
    int: risk_score between 1 (low risk) and 10 (high risk)
    """

    # Base risk from volatility
    if price_volatility < 1:
        risk_score = 2
    elif price_volatility < 2:
        risk_score = 4
    elif price_volatility < 3:
        risk_score = 6
    else:
        risk_score = 8

    # Adjust risk based on market trend
    if market_trend == "bearish":
        risk_score += 1
    elif market_trend == "bullish":
        risk_score -= 1

    # Ensure risk score stays within expected bounds
    risk_score = max(1, min(10, risk_score))

    return risk_score
