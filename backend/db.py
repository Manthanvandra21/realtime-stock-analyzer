# File: backend/db.py

import sqlite3
from logger import logger

DB_PATH = "backend/database.db"


def get_db_connection():
    return sqlite3.connect(DB_PATH)


def get_portfolio():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT symbol, quantity, buy_price FROM portfolio")
    rows = cursor.fetchall()
    conn.close()
    return rows


def get_risk_history(symbol):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT symbol, risk_score, checked_at FROM risk_history WHERE symbol = ?",
        (symbol,)
    )
    rows = cursor.fetchall()
    conn.close()
    return rows


def add_to_portfolio(symbol, qty, price):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO portfolio (symbol, quantity, buy_price) VALUES (?, ?, ?)",
        (symbol, qty, price)
    )
    conn.commit()
    conn.close()
    logger.info("Portfolio updated")


def save_risk(symbol, risk_score):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO risk_history (symbol, risk_score) VALUES (?, ?)",
        (symbol, risk_score)
    )
    conn.commit()
    conn.close()
    logger.info("Risk saved")
