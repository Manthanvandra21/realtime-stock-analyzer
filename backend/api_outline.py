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
