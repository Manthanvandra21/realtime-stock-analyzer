# File: backend/data_fetcher.py

def fetch_price(symbol):
    """
    Dummy function to safely return fixed stock price data.
    """
    try:
        return {
            "symbol": symbol.upper(),
            "price": 123.45,
            "change": 1.25,     # dummy price change
            "currency": "USD"
        }
    except Exception:
        return {
            "symbol": symbol,
            "price": None,
            "change": None,
            "currency": "USD"
        }


def fetch_news(symbol):
    """
    Dummy function to safely return sample news list.
    """
    try:
        return {
            "symbol": symbol.upper(),
            "news": [
                f"{symbol.upper()} stock shows steady performance",
                f"Analysts remain neutral on {symbol.upper()}",
                f"{symbol.upper()} sees average trading volume"
            ]
        }
    except Exception:
        return {
            "symbol": symbol,
            "news": []
        }
