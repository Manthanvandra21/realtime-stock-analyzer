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
# SESSION STATE (FOR LOADING STATES)
# -----------------------------------------
if "loading_price" not in st.session_state:
    st.session_state.loading_price = False

if "loading_risk" not in st.session_state:
    st.session_state.loading_risk = False

if "loading_news" not in st.session_state:
    st.session_state.loading_news = False

if "loading_portfolio" not in st.session_state:
    st.session_state.loading_portfolio = False

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
# SIDEBAR
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
# STOCK SEARCH
# -----------------------------------------
st.subheader("🔍 Stock Search")
stock_search_box = st.text_input("Enter stock symbol (example: AAPL)")

st.write("---")

# -----------------------------------------
# STOCK PRICES
# -----------------------------------------
st.subheader("💵 Stock Prices")

price_display_area = st.empty()

if st.button(
    "Fetch Price",
    disabled=st.session_state.loading_price
):
    price_display_area.empty()

    if stock_search_box.strip() == "":
        st.warning("⚠️ Please enter a stock symbol before fetching price.")
    else:
        st.session_state.loading_price = True
        with st.spinner("Fetching stock price..."):
            try:
                response = requests.get(
                    f"http://127.0.0.1:5000/api/get_price/{stock_search_box}"
                )
                data = response.json()

                if "error" in data:
                    price_display_area.error(f"❌ {data['error']}")
                else:
                    price_display_area.success("✅ Price fetched successfully")
                    price_display_area.subheader("Current Price")
                    price_display_area.write(f"Stock: {data.get('symbol', 'N/A')}")
                    price_display_area.write(f"Price: ₹ {data.get('price', 'N/A')}")
                    price_display_area.write(f"Change: {data.get('change', 'N/A')}%")

            except Exception:
                price_display_area.error(
                    "❌ Unable to connect to backend. Please try again later."
                )

        st.session_state.loading_price = False

# -----------------------------------------
# RISK SCORE
# -----------------------------------------
st.subheader("⚠️ Risk Score")

risk_score_placeholder = st.empty()
risk_description_placeholder = st.empty()

if st.button(
    "Check Risk",
    disabled=st.session_state.loading_risk
):
    risk_score_placeholder.empty()
    risk_description_placeholder.empty()

    if stock_search_box.strip() == "":
        st.warning("⚠️ Please enter a stock symbol before checking risk.")
    else:
        st.session_state.loading_risk = True
        with st.spinner("Calculating risk score..."):
            try:
                response = requests.get(
                    f"http://127.0.0.1:5000/api/get_risk/{stock_search_box}"
                )
                data = response.json()

                if "error" in data:
                    risk_score_placeholder.error(f"❌ {data['error']}")
                else:
                    risk_score = data.get("risk_score", "N/A")
                    explanation = data.get(
                        "explanation", "No explanation available."
                    )

                    color = "green"
                    if str(risk_score).lower() == "medium":
                        color = "orange"
                    elif str(risk_score).lower() == "high":
                        color = "red"

                    risk_score_placeholder.success("✅ Risk analysis completed")
                    risk_score_placeholder.markdown(
                        f"<h1 style='color:{color}'>Risk Score: {risk_score}</h1>",
                        unsafe_allow_html=True
                    )
                    risk_description_placeholder.write(explanation)

            except Exception:
                risk_score_placeholder.error(
                    "❌ Unable to connect to backend. Please try again later."
                )

        st.session_state.loading_risk = False

# -----------------------------------------
# PORTFOLIO (FROM DB)
# -----------------------------------------
st.subheader("🗂 Portfolio (From DB)")

portfolio_placeholder = st.empty()

col1, col2, col3 = st.columns(3)

with col1:
    portfolio_symbol = st.text_input("Stock Symbol")

with col2:
    portfolio_quantity = st.number_input(
        "Quantity", min_value=1, step=1
    )

with col3:
    portfolio_buy_price = st.number_input(
        "Buy Price", min_value=0.0, step=0.01
    )

if st.button(
    "Add to Portfolio",
    disabled=st.session_state.loading_portfolio
):
    if portfolio_symbol.strip() == "":
        st.warning("⚠️ Stock symbol is required to add to portfolio.")
    else:
        st.session_state.loading_portfolio = True
        with st.spinner("Saving stock to portfolio..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:5000/api/portfolio/add",
                    json={
                        "symbol": portfolio_symbol,
                        "quantity": portfolio_quantity,
                        "buy_price": portfolio_buy_price
                    }
                )
                data = response.json()

                if "error" in data:
                    st.error(f"❌ {data['error']}")
                else:
                    st.success("✅ Stock added to portfolio successfully")

            except Exception:
                st.error(
                    "❌ Unable to connect to backend. Please try again later."
                )

        st.session_state.loading_portfolio = False

if st.button(
    "Load Portfolio",
    disabled=st.session_state.loading_portfolio
):
    portfolio_placeholder.empty()
    st.session_state.loading_portfolio = True

    with st.spinner("Loading portfolio data..."):
        try:
            response = requests.get(
                "http://127.0.0.1:5000/api/portfolio"
            )
            data = response.json()

            if "error" in data:
                portfolio_placeholder.error(f"❌ {data['error']}")
            elif not data:
                portfolio_placeholder.warning("ℹ️ Portfolio is empty.")
            else:
                portfolio_placeholder.success("✅ Portfolio loaded")
                portfolio_placeholder.dataframe(data)

        except Exception:
            portfolio_placeholder.error(
                "❌ Unable to connect to backend. Please try again later."
            )

    st.session_state.loading_portfolio = False

# -----------------------------------------
# NEWS
# -----------------------------------------
st.subheader("📰 Latest Stock News")

news_placeholder = st.empty()

if st.button(
    "Load News",
    disabled=st.session_state.loading_news
):
    news_placeholder.empty()

    if stock_search_box.strip() == "":
        st.warning("⚠️ Please enter a stock symbol to load news.")
    else:
        st.session_state.loading_news = True
        with st.spinner("Loading latest news..."):
            try:
                response = requests.get(
                    f"http://127.0.0.1:5000/api/get_news/{stock_search_box}"
                )
                data = response.json()

                if "error" in data:
                    news_placeholder.error(f"❌ {data['error']}")
                else:
                    news_placeholder.success("✅ News loaded successfully")
                    news_placeholder.subheader("Top Headlines")
                    for item in data.get("news", []):
                        news_placeholder.write(f"• {item}")

            except Exception:
                news_placeholder.error(
                    "❌ Unable to connect to backend. Please try again later."
                )

        st.session_state.loading_news = False

st.write("---")

# -----------------------------------------
# FOOTER
# -----------------------------------------
st.write("This project is under active development.")
st.write("More features will be enabled step by step.")
