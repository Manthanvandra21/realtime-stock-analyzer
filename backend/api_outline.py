"""
File: backend/api_outline.py

Purpose:
This file contains ONLY planning notes and API outlines.
No real business logic or database code should be written here.

This file helps the team understand:
- What APIs will exist
- What each API will do
- What input/output is expected
- How frontend and backend will communicate
"""

# ==================================================
# BACKEND RESPONSIBILITIES (HIGH LEVEL)
# ==================================================

# 1. Fetch live stock prices
# 2. Store and manage user portfolio
# 3. Calculate stock risk score
# 4. Compare multiple stocks
# 5. Fetch latest stock-related news

# ==================================================
# GENERAL BACKEND FLOW
# ==================================================

# Step 1: Frontend sends request (API call)
# Step 2: Backend validates input
# Step 3: Backend fetches data from API / DB
# Step 4: Backend processes and formats data
# Step 5: Backend sends JSON response to frontend
# Step 6: Frontend displays data to user

# ==================================================
# API 1: GET LIVE STOCK PRICE
# ==================================================

# Endpoint:
# GET /api/get_price/<symbol>

# Purpose:
# Returns the current market price of a stock.

# Input:
# - symbol (string): Stock ticker symbol (example: AAPL, TSLA)

# Processing Steps:
# - Validate symbol (not empty, valid format)
# - Call external market data API
# - Extract latest price and timestamp
# - Format response

# Output (JSON):
# {
#   "symbol": "AAPL",
#   "price": 123.45,
#   "timestamp": "2025-01-01 10:30:00",
#   "status": "success"
# }

# Possible Errors:
# - Symbol missing
# - Invalid symbol
# - External API failure
# - Internal server error

# ==================================================
# API 2: GET HISTORICAL STOCK DATA
# ==================================================

# Endpoint:
# GET /api/historical/<symbol>

# Purpose:
# Returns past stock prices for charts and analysis.

# Input:
# - symbol (string)
# - optional date range

# Output:
# - List of prices with dates

# ==================================================
# API 3: PORTFOLIO MANAGEMENT
# ==================================================

# API: Add stock to portfolio
# POST /api/portfolio/add

# API: Remove stock from portfolio
# POST /api/portfolio/remove

# API: Get portfolio summary
# GET /api/portfolio

# Portfolio Data Includes:
# - Stock symbol
# - Quantity
# - Buy price
# - Current price
# - Profit / Loss

# ==================================================
# API 4: RISK SCORE CALCULATOR
# ==================================================

# Endpoint:
# GET /api/risk/<symbol>

# Purpose:
# Calculates how risky a stock is.

# Inputs Needed:
# - Stock symbol
# - Historical price data
# - Volatility
# - Moving averages
# - Trend direction

# Output (JSON):
# {
#   "symbol": "AAPL",
#   "risk_score": 7,
#   "risk_level": "High",
#   "explanation": "High volatility detected"
# }

# Risk Score Range:
# 1 = Very Low Risk
# 10 = Very High Risk

# Possible Errors:
# - Not enough data
# - Invalid symbol
# - Calculation failure

# ==================================================
# API 5: STOCK COMPARISON
# ==================================================

# Endpoint:
# POST /api/compare

# Purpose:
# Compare multiple stocks side-by-side.

# Input:
# - List of stock symbols

# Output:
# - Prices
# - Trends
# - Risk scores

# ==================================================
# API 6: LATEST STOCK NEWS
# ==================================================

# Endpoint:
# GET /api/news/<symbol>

# Purpose:
# Fetch latest news related to a stock.

# Output:
# - News headline
# - Source
# - Published time
# - Short summary

# ==================================================
# IMPORTANT NOTE FOR TEAM
# ==================================================

# This file is ONLY for planning.
# Real Flask routes and logic will be implemented
# later in actual backend files (e.g., app.py).

# Do NOT write executable code here.
