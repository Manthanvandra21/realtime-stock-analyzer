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
