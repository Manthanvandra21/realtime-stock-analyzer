-- File: db/schema.sql

-- -------------------------------
-- Users Table (Basic Placeholder)
-- -------------------------------

CREATE TABLE IF NOT EXISTS users (
    id INT,
    name VARCHAR(100),
    email VARCHAR(100)
);

-- -------------------------------
-- Portfolio Table (Future Ready)
-- -------------------------------
-- Stores user stock holdings

CREATE TABLE IF NOT EXISTS portfolio (
    id INT,
    stock_symbol VARCHAR(20),
    quantity INT,
    buy_price FLOAT
);

-- -------------------------------
-- Sample Portfolio Data
-- -------------------------------

INSERT INTO portfolio (id, stock_symbol, quantity, buy_price) VALUES
(1, 'AAPL', 10, 170.50),
(2, 'GOOGL', 5, 2800.00),
(3, 'MSFT', 8, 395.75);

-- -------------------------------
-- Stock Price History (Optional)
-- -------------------------------

CREATE TABLE IF NOT EXISTS stock_history (
    id INT,
    symbol VARCHAR(20),
    price FLOAT,
    timestamp DATETIME
);

-- -------------------------------
-- Sample Stock History Data
-- -------------------------------

INSERT INTO stock_history (id, symbol, price, timestamp) VALUES
(1, 'AAPL', 175.50, '2025-11-19 10:00:00'),
(2, 'AAPL', 176.20, '2025-11-19 11:00:00'),
(3, 'GOOGL', 2850.75, '2025-11-19 10:00:00'),
(4, 'MSFT', 410.30, '2025-11-19 10:00:00');

-- -------------------------------
-- Risk History Table (Future Use)
-- -------------------------------
-- Stores ML-generated risk scores over time

CREATE TABLE IF NOT EXISTS risk_history (
    id INT,
    stock_symbol VARCHAR(20),
    risk_score INT,
    checked_at DATETIME
);

-- -------------------------------
-- Sample Risk History Data
-- -------------------------------

INSERT INTO risk_history (id, stock_symbol, risk_score, checked_at) VALUES
(1, 'AAPL', 3, '2025-11-20 09:00:00'),
(2, 'GOOGL', 6, '2025-11-20 09:05:00'),
(3, 'MSFT', 5, '2025-11-20 09:10:00');
