# File: frontend/home.py

import streamlit as st
import requests

st.title("Real-Time Stock Analyzer")

# Input
symbol = st.text_input("Enter Stock Symbol")

# Clear old data when symbol changes
if "last_symbol" not in st.session_state:
    st.session_state.last_symbol = ""

if symbol != st.session_state.last_symbol:
    st.session_state.price = None
    st.session_state.risk = None
    st.session_state.news = None
    st.session_state.last_symbol = symbol

# Fetch Price
if st.button("Fetch Price"):
    if not symbol:
        st.warning("Please enter a stock symbol")
    else:
        with st.spinner("Fetching price..."):
            try:
                response = requests.get(f"http://localhost:5000/price/{symbol}")
                data = response.json()
                if "error" in data:
                    st.error(data["error"])
                else:
                    st.session_state.price = data
            except Exception:
                st.error("Failed to fetch price")

if st.session_state.get("price"):
    st.success(f"Price Data: {st.session_state.price}")

# Check Risk
if st.button("Check Risk"):
    if not symbol:
        st.warning("Please enter a stock symbol")
    else:
        with st.spinner("Calculating risk..."):
            try:
                response = requests.get(f"http://localhost:5000/risk/{symbol}")
                data = response.json()
                if "error" in data:
                    st.error(data["error"])
                else:
                    st.session_state.risk = data
            except Exception:
                st.error("Failed to calculate risk")

if st.session_state.get("risk"):
    st.success(f"Risk Info: {st.session_state.risk}")

# Load News
if st.button("Load News"):
    if not symbol:
        st.warning("Please enter a stock symbol")
    else:
        with st.spinner("Loading news..."):
            try:
                response = requests.get(f"http://localhost:5000/news/{symbol}")
                data = response.json()
                if "error" in data:
                    st.error(data["error"])
                else:
                    st.session_state.news = data
            except Exception:
                st.error("Failed to load news")

if st.session_state.get("news"):
    st.success(f"News: {st.session_state.news}")
