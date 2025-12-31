import streamlit as st
import requests

# -----------------------------------------
# PAGE CONFIG
# -----------------------------------------
st.set_page_config(
    page_title="Real-Time Stock Price Analyzer",
    layout="wide"
)

# -----------------------------------------
# MAIN TITLE
# -----------------------------------------
st.title("📈 Real-Time Stock Price Analyzer")
st.write(
    "Welcome to the Real-Time Stock Price Analyzer with AI-Powered "
    "Risk Engine & Portfolio Manager."
)

st.write("---")

# -----------------------------------------
# SIDEBAR (NAVIGATION & CONTROLS - PLACEHOLDERS)
# -----------------------------------------
with st.sidebar:
    st.header("📂 Navigation")

    st.write("• Home")
    st.write("• Portfolio")
    st.write("• Risk Engine")
    st.write("• News")
    st.write("• Compare Stocks")
    st.write("• Settings")

    st.write("---")
    st.write("Theme switch coming soon")
    st.write("Time range selector coming soon")

# -----------------------------------------
# MAIN DASHBOARD LAYOUT
# -----------------------------------------
st.subheader("🔍 Stock Search")
stock_search_box = st.text_input("Enter stock symbol (example: AAPL)")

st.write("---")

# -----------------------------------------
# PRICE DISPLAY AREA
# -----------------------------------------
st.subheader("💵 Stock Prices")

# Existing display
price_display_area = st.empty()

# Placeholder for future button
price_button_placeholder = st.empty()

# Placeholder for future extended price details
price_details_placeholder = st.empty()

# -----------------------------------------
# TREND & PREDICTION
# -----------------------------------------
st.subheader("📈 Trend & Prediction")

trend_prediction_box = st.empty()
trend_button_placeholder = st.empty()

# -----------------------------------------
# PORTFOLIO SUMMARY
# -----------------------------------------
st.subheader("🗂 Portfolio Summary")

portfolio_summary_box = st.empty()
portfolio_button_placeholder = st.empty()
portfolio_table_placeholder = st.empty()

# -----------------------------------------
# RISK SCORE SECTION
# -----------------------------------------
st.subheader("⚠️ Risk Score")

risk_score_placeholder = st.empty()
risk_button_placeholder = st.empty()
risk_description_placeholder = st.empty()

# -----------------------------------------
# CHARTS AREA
# -----------------------------------------
st.subheader("📊 Charts")

charts_area = st.empty()
charts_button_placeholder = st.empty()
charts_controls_placeholder = st.empty()

# -----------------------------------------
# NEWS SECTION
# -----------------------------------------
st.subheader("📰 Latest Stock News")

news_placeholder = st.empty()
news_button_placeholder = st.empty()
news_list_placeholder = st.empty()

st.write("---")

# -----------------------------------------
# BACKEND API TEST SECTION (EXISTING)
# -----------------------------------------
st.subheader("🧪 Test Stock Price API")

symbol = st.text_input("Enter Stock Symbol for API Test")

if st.button("Get Price"):
    if symbol.strip() == "":
        st.warning("Please enter a stock symbol.")
    else:
        try:
            response = requests.get(
                f"http://127.0.0.1:5000/api/get_price/{symbol}"
            )
            data = response.json()
            st.success("API Response:")
            st.write(data)
        except Exception as e:
            st.error("Backend not reachable or error occurred.")
            st.write(str(e))

# -----------------------------------------
# RISK ANALYSIS PLACEHOLDERS (UPCOMING)
# -----------------------------------------
st.write("---")
st.subheader("📊 Stock Risk Analysis (Coming Soon)")

risk_score_box_placeholder = st.empty()
risk_explanation_placeholder = st.empty()
risk_meter_placeholder = st.empty()

st.write(
    "This section will display the calculated risk score using "
    "volatility, trends, and moving averages."
)

# -----------------------------------------
# FOOTER NOTES
# -----------------------------------------
st.write("---")
st.write("This project is under active development.")
st.write("More features will be enabled step by step.")
