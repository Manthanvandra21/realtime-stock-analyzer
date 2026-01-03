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

price_display_area = st.empty()
price_button_placeholder = st.empty()
price_details_placeholder = st.empty()

if price_button_placeholder.button("Fetch Price"):
    price_display_area.write("Fetching data...")
    try:
        response = requests.get(
            f"http://127.0.0.1:5000/api/get_price/{stock_search_box}"
        )
        data = response.json()

        price_display_area.subheader("Current Price")
        price_display_area.write(f"Stock: {data.get('symbol', 'N/A')}")
        price_display_area.write(f"Price: ₹ {data.get('price', 'N/A')}")
        price_display_area.write(f"Change: {data.get('change', 'N/A')}%")

    except Exception:
        price_display_area.write("Unable to fetch stock price.")

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
# RISK SCORE SECTION (CONNECTED TO BACKEND)
# -----------------------------------------
st.subheader("⚠️ Risk Score")

risk_score_placeholder = st.empty()
risk_button_placeholder = st.empty()
risk_description_placeholder = st.empty()

if risk_button_placeholder.button("Check Risk"):
    if stock_search_box.strip() == "":
        risk_score_placeholder.error("Please enter a stock symbol.")
    else:
        risk_score_placeholder.write("Fetching data...")
        try:
            response = requests.get(
                f"http://127.0.0.1:5000/api/get_risk/{stock_search_box}"
            )
            data = response.json()

            risk_score = data.get("risk_score", "N/A")
            explanation = data.get(
                "explanation",
                "No explanation available."
            )

            color = "green"
            score_text = str(risk_score).lower()

            if score_text == "medium":
                color = "orange"
            elif score_text == "high":
                color = "red"

            risk_score_placeholder.markdown(
                f"<h1 style='color:{color}'>Risk Score: {risk_score}</h1>",
                unsafe_allow_html=True
            )
            risk_description_placeholder.write(explanation)

        except Exception:
            risk_score_placeholder.error("Backend not running or unreachable.")

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

if news_button_placeholder.button("Load News"):
    news_placeholder.write("Fetching data...")
    try:
        response = requests.get(
            f"http://127.0.0.1:5000/api/get_news/{stock_search_box}"
        )
        data = response.json()

        news_placeholder.subheader("Top Headlines")
        for item in data.get("news", []):
            news_placeholder.write(f"• {item}")

    except Exception:
        news_placeholder.write("Unable to load news.")

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
