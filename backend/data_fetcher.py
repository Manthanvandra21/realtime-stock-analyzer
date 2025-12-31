# File: backend/data_fetcher.py

def fetch_price(symbol):
    """
    Dummy function to return a fixed stock price.
    """
    return {
        "symbol": symbol.upper(),
        "price": 123.45,
        "currency": "USD"
    }


def fetch_news(symbol):
    """
    Dummy function to return sample news data.
    """
    return {
        "symbol": symbol.upper(),
        "news": [
            f"{symbol.upper()} stock shows steady performance",
            f"Analysts remain neutral on {symbol.upper()}",
            f"{symbol.upper()} sees average trading volume"
        ]
    }


def fetch_risk(symbol):
    """
    Dummy function to return a sample risk score.
    """
    return {
        "symbol": symbol.upper(),
        "risk_score": 5,
        "explanation": "Moderate risk based on dummy evaluation"
    }
