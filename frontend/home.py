import streamlit as st
import requests

st.set_page_config(page_title="Real-Time Stock Price Analyzer", layout="wide")

# title
st.title("📈 Real-Time Stock Price Analyzer")
st.write("Welcome to the Real-Time Stock Price Analyzer with AI-Powered Risk Engine & Portfolio Manager.")

# stock search input
st.subheader("🔍 Stock Search")
stock_search_box = st.empty()

# area for stock prices
st.subheader("💵 Stock Prices")
price_display_area = st.empty()

# trend prediction box
st.subheader("📈 Trend & Prediction")
trend_prediction_box = st.empty()

# portfolio summary
st.subheader("🗂 Portfolio Summary")
portfolio_summary_box = st.empty()

# risk score placeholder
st.subheader("⚠️ Risk Score")
risk_score_placeholder = st.empty()

# area for charts
st.subheader("📊 Charts")
charts_area = st.empty()

# -------------------------------
# Added on Nov 21 — Sidebar Outline
# -------------------------------
with st.sidebar:
    # Here will be the stock selection dropdown
    # Here will be the time range buttons (1 day, 1 week etc.)
    # Here will be dark/light mode switch
    # Here will be button for portfolio view
    pass

# -------------------------------
# Added Top Header Bar Placeholders
# -------------------------------

# --- TOP HEADER BAR ---
# Top Bar: Project Title
# Top Bar: Last updated time
# Top Bar: Refresh button
# Top Bar: Profile/Settings icon


# -----------------------------------------
# NEW SIDE MENU PLACEHOLDERS (as instructed)
# -----------------------------------------

# Side Menu: Home button
# Side Menu: Portfolio
# Side Menu: Risk Engine
# Side Menu: News Section
# Side Menu: Compare Stocks
# Side Menu: Settings


# -----------------------------------------
# NEW API TEST SECTION (as instructed)
# -----------------------------------------

st.subheader("Test Stock Price API")
symbol = st.text_input("Enter Stock Symbol")
if st.button("Get Price"):
    data = requests.get(f"http://127.0.0.1:5000/api/get_price/{symbol}").json()
    st.write(data)


# -----------------------------------------
# NEW UI IMPROVEMENT (as instructed)
# -----------------------------------------

st.write("---")
st.subheader("API Tester Section")

# -----------------------------------------
# NEW EXPLANATION LINES (as instructed)
# -----------------------------------------

st.write("This tool allows you to check stock prices.")
st.write("Type a stock symbol and click the button.")

# -----------------------------------------
# CONNECT TO BACKEND (TEST BOX) — PLACEHOLDERS
# -----------------------------------------

# Backend Test Box: Title
# Backend Test Box: Input field placeholder
# Backend Test Box: Button placeholder
# Backend Test Box: Output display placeholder
