# File: backend/db.py

import sqlite3
from backend.logger import logger

DB_PATH = "backend/database.db"


def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


# -------------------------
# READ OPERATIONS
# -------------------------
def get_portfolio():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM portfolio")
    rows = cursor.fetchall()

    conn.close()
    return [dict(row) for row in rows]


def get_risk_history(symbol):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM risk_history WHERE symbol = ? ORDER BY created_at DESC",
        (symbol,)
    )
    rows = cursor.fetchall()

    conn.close()
    return [dict(row) for row in rows]


# -------------------------
# WRITE OPERATIONS
# -------------------------
def add_to_portfolio(symbol, qty, price):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO portfolio (symbol, quantity, buy_price) VALUES (?, ?, ?)",
            (symbol, qty, price)
        )

        conn.commit()
        conn.close()

        logger.info(f"DB WRITE SUCCESS | portfolio | {symbol}")
        return True

    except Exception as e:
        logger.error(f"DB WRITE FAILED | portfolio | {symbol} | {e}")
        return False


def save_risk(symbol, risk_score):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO risk_history (symbol, risk_score) VALUES (?, ?)",
            (symbol, risk_score)
        )

        conn.commit()
        conn.close()

        logger.info(f"DB WRITE SUCCESS | risk_history | {symbol}")
        return True

    except Exception as e:
        logger.error(f"DB WRITE FAILED | risk_history | {symbol} | {e}")
        return False
