# File: backend/app.py

# This part will show stock price

# This part will manage portfolio

# This part will check risk

# This part will compare stocks

# This part will show news



# API: Get live stock price

# API: Historical data

# API: Portfolio update

# API: Add stock to portfolio

# API: Remove stock from portfolio

# API: Get risk score

# API: Compare multiple stocks

# API: Latest news for stock



# Step 1: User sends request to backend

# Step 2: Backend calls API or database

# Step 3: Backend processes the data

# Step 4: Backend sends response to frontend

# Step 5: Frontend shows updated data on screen



# REAL API for live stock price
@app.route('/api/get_price/<symbol>', methods=['GET'])
def get_price(symbol):
    return {"symbol": symbol, "price": 123.45}

# -------------------------------
# STOCK PRICE API - PLANNING NOTES
# -------------------------------

# INPUT:
# - User sends a stock symbol (e.g., "AAPL", "RELIANCE").
# - Input arrives via GET request to /api/get_price/<symbol>.
# - Backend must validate the symbol (check empty, invalid characters).

# PROCESS:
# - Backend forwards the request to a real market data provider OR mock service.
# - Backend fetches the live price, last updated time, and market status.
# - Backend formats the data in JSON structure.

# OUTPUT:
# - Returns JSON object with:
#       "symbol": given stock symbol
#       "price": current market price
#       "timestamp": last update time
#       "status": "success"

# ERRORS:
# - If symbol is missing → return error JSON with message "Symbol required".
# - If symbol is invalid → return error JSON with message "Invalid stock symbol".
# - If API provider fails → return error JSON with message "Data fetch error".
# - If unknown server issue → return error JSON with "Internal server error".
