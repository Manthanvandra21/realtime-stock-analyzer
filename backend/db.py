# File: backend/db.py

import sqlite3

DB_PATH = "backend/database.db"


def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # enables dict-like rows
    return conn


def get_portfolio():
    """
    Reads all portfolio rows from DB
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM portfolio")
    rows = cursor.fetchall()

    conn.close()
    return [dict(row) for row in rows]


def get_risk_history(symbol):
    """
    Reads risk history for a specific stock symbol
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM risk_history WHERE symbol = ? ORDER BY created_at DESC",
        (symbol,)
    )
    rows = cursor.fetchall()

    conn.close()
    return [dict(row) for row in rows]

