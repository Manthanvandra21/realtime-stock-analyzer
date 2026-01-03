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

if price_button_placeholder.button("Fetch Price"):
    price_display_area.empty()

    if stock_search_box.strip() == "":
        st.warning("Please enter a stock symbol.")
    else:
        price_display_area.info("Fetching stock price...")
        try:
            response = requests.get(
                f"http://127.0.0.1:5000/api/get_price/{stock_search_box}"
            )
            data = response.json()

            if "error" in data:
                price_display_area.error(data["error"])
            else:
                price_display_area.success("Price fetched successfully")
                price_display_area.subheader("Current Price")
                price_display_area.write(f"Stock: {data.get('symbol', 'N/A')}")
                price_display_area.write(f"Price: ₹ {data.get('price', 'N/A')}")
                price_display_area.write(f"Change: {data.get('change', 'N/A')}%")

        except Exception:
            price_display_area.error("Backend not running or unreachable.")

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
risk_description_placeholder = st.empty()
risk_button_placeholder = st.empty()

if risk_button_placeholder.button("Check Risk"):
    risk_score_placeholder.empty()
    risk_description_placeholder.empty()

    if stock_search_box.strip() == "":
        st.warning("Please enter a stock symbol.")
    else:
        risk_score_placeholder.info("Calculating risk score...")
        try:
            response = requests.get(
                f"http://127.0.0.1:5000/api/get_risk/{stock_search_box}"
            )
            data = response.json()

            if "error" in data:
                risk_score_placeholder.error(data["error"])
            else:
                risk_score = data.get("risk_score", "N/A")
                explanation = data.get("explanation", "No explanation available.")

                color = "green"
                score_text = str(risk_score).lower()
                if score_text == "medium":
                    color = "orange"
                elif score_text == "high":
                    color = "red"

                risk_score_placeholder.success("Risk analysis completed")
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

if news_button_placeholder.button("Load News"):
    news_placeholder.empty()

    if stock_search_box.strip() == "":
        st.warning("Please enter a stock symbol.")
    else:
        news_placeholder.info("Loading latest news...")
        try:
            response = requests.get(
                f"http://127.0.0.1:5000/api/get_news/{stock_search_box}"
            )
            data = response.json()

            if "error" in data:
                news_placeholder.error(data["error"])
            else:
                news_placeholder.success("News loaded successfully")
                news_placeholder.subheader("Top Headlines")
                for item in data.get("news", []):
                    news_placeholder.write(f"• {item}")

        except Exception:
            news_placeholder.error("Backend not running or unreachable.")

st.write("---")

# -----------------------------------------
# FOOTER NOTES
# -----------------------------------------
st.write("This project is under active development.")
st.write("More features will be enabled step by step.")
