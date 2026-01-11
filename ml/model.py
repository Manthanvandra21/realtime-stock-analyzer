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


# File: ml/model.py

def calculate_risk(symbol):
    if not symbol or not isinstance(symbol, str):
        return 1

    length = len(symbol.strip())

    if length <= 3:
        return 3
    elif length <= 5:
        return 6
    else:
        return 8


    # -------------------------------
    # Input validation (critical)
    # -------------------------------
    # If symbol is None, empty, or not a string,
    # return lowest safe risk to protect backend
    if not symbol or not isinstance(symbol, str):
        return 1  # Default low risk for invalid input

    symbol = symbol.strip()

    if symbol == "":
        return 1  # Empty after trimming → safe default

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

    Safety:
    - Assumes backend may pass validated or fallback values
    - No side effects (no DB, no logging)

    Returns:
    {
        "symbol": str,
        "risk_score": int,
        "risk_level": str,
        "explanation": str
    }
    """

    # Risk level mapping kept deterministic
    if risk_score <= 3:
        risk_level = "Low"
    elif risk_score <= 6:
        risk_level = "Medium"
    else:
        risk_level = "High"

    return {
        "symbol": symbol or "",
        "risk_score": risk_score,
        "risk_level": risk_level,
        "explanation": explanation
    }
