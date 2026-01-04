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

# Here we will clean data
# Here we will do prediction using linear method
# Here we will do prediction using AR method
# Here we will pick best method

# To train the model, we need old price data
# Model will learn patterns from past data
# We will check accuracy later
# Better accuracy = better predictions

# Model needs Open, High, Low, Close prices
# Model needs volume data
# More data = better prediction
# Data cleaning is important before training

# ML Model Planning Notes:
# The model will predict simple stock price trends.
# It will decide whether the price may go up, go down, or stay neutral.
# The model will use historical stock prices for learning.
# Past Open, High, Low, Close, and Volume data will be used.
# The output of the model will be a simple trend label:
# Up / Down / Neutral
# This planning helps keep the ML logic clear for future development.

def dummy_risk(symbol):
    return 5, "Moderate risk"


def calculate_risk(symbol):
    """
    Calculates a deterministic dummy risk score for a stock symbol.

    What it does:
    - Uses simple, rule-based logic to assign a risk level.
    - Does NOT use real market data or machine learning models.
    - Designed only for safe backend and frontend testing.

    What it returns:
    - risk_score (int): A number between 1 and 10.
    - explanation (str): Human-readable reason for the risk score.

    Behavior notes:
    - Same input symbol will always return the same output.
    - Empty symbol is treated as lowest risk to avoid errors.
    """
    # Handle empty symbol input safely
    if not symbol:
        return 1, "Very low risk due to empty symbol input"

    length = len(symbol)

    # Short symbols are treated as low risk
    # Reason: fewer characters → assumed stability (dummy logic)
    if length <= 3:
        return 3, "Low risk based on short symbol length"

    # Medium-length symbols are treated as medium risk
    # Reason: average length → moderate dummy volatility
    elif length <= 5:
        return 6, "Medium risk based on average symbol length"

    # Long symbols are treated as high risk
    # Reason: longer symbols → higher assumed dummy volatility
    else:
        return 8, "High risk based on long symbol length"
