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
# Placeholder Functions for APIs
# ==================================================

def get_price(symbol):
    """
    Placeholder for future API to fetch live stock price.
    Input:
    - symbol: Stock ticker symbol (string)
    
    Output:
    - JSON with current price, timestamp, status
    """
    pass  # To be implemented later


def get_risk(symbol):
    """
    Placeholder for future API to calculate stock risk.
    Input:
    - symbol: Stock ticker symbol (string)
    
    Output:
    - JSON with risk score, risk level, explanation
    """
    pass  # To be implemented later


def add_to_portfolio(symbol):
    """
    Placeholder for API to add a stock to the user's portfolio.
    Input:
    - symbol: Stock ticker symbol (string)
    
    Output:
    - JSON with success/failure message
    """
    pass  # To be implemented later


def remove_from_portfolio(symbol):
    """
    Placeholder for API to remove a stock from the user's portfolio.
    Input:
    - symbol: Stock ticker symbol (string)
    
    Output:
    - JSON with success/failure message
    """
    pass  # To be implemented later


def get_news(symbol):
    """
    Placeholder for API to fetch latest stock-related news.
    Input:
    - symbol: Stock ticker symbol (string)
    
    Output:
    - JSON list of news articles with headline, source, time, summary
    """
    pass  # To be implemented later
