# File: ml/model.py

# Placeholder for AI trend prediction model
# Future implementation will analyze historical stock data,
# compute technical indicators, and use ML algorithms
# to predict short-term and long-term price trends.

# Placeholder: Risk Evaluation Module
# Will calculate volatility, beta, moving averages, and detect sudden
# price movements to generate stock risk ratings.

# Placeholder: Trend Prediction Module
# Will use machine learning models trained on historical market data
# to forecast upcoming stock trends and momentum shifts.


def clean_data(data):
    """
    Placeholder: Cleans raw stock market data.
    Future implementation will handle missing values, outliers,
    and normalization.
    """
    pass


def prepare_training_data(data):
    """
    Placeholder: Prepares processed data for ML model training.
    Future implementation will create feature sets and labels
    from historical stock patterns.
    """
    pass


def calculate_volatility(data):
    """
    Placeholder: Calculates stock price volatility.
    Future implementation will derive volatility metrics from
    historical price fluctuations.
    """
    pass


# --------------------------------------------------
# ML PLANNING & DESIGN NOTES
# --------------------------------------------------
# - Data will be cleaned first
# - Multiple prediction methods will be tested
# - Best method will be selected based on accuracy
# - Uses OHLC + Volume data
# - Better data → better predictions
# - Current logic is deterministic and safe
# --------------------------------------------------


def calculate_risk(symbol):
    """
    Calculates a deterministic dummy risk score for a stock symbol.

    What it does:
    - Uses rule-based logic (NO real ML, NO randomness)
    - Safe for backend integration and testing

    What it returns:
    - risk_score (int only)

    IMPORTANT:
    - Backend will handle formatting, explanation, and DB storage
    - ML → Backend → Database (future automation flow)
    """

    # Empty symbol → lowest risk to prevent crashes
    if not symbol:
        return 1

    length = len(symbol)

    # Short symbols → Low risk
    # Reason: assumed stability (dummy logic)
    if length <= 3:
        return 3

    # Medium symbols → Medium risk
    # Reason: moderate assumed volatility
    elif length <= 5:
        return 6

    # Long symbols → High risk
    # Reason: higher assumed dummy volatility
    else:
        return 8


def format_risk_output(symbol, risk_score, explanation):
    """
    Formats ML risk output into a structured dictionary.

    NOTE:
    - This function is reusable
    - Backend may call this before saving to DB
    - ML layer itself does NOT save or log anything

    Returns:
    {
        "symbol": str,
        "risk_score": int,
        "risk_level": str,
        "explanation": str
    }
    """
    if risk_score <= 3:
        risk_level = "Low"
    elif risk_score <= 6:
        risk_level = "Medium"
    else:
        risk_level = "High"

    return {
        "symbol": symbol,
        "risk_score": risk_score,
        "risk_level": risk_level,
        "explanation": explanation
    }
