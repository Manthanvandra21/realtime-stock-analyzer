-- File: db/schema.sql

-- =================================================
-- USERS TABLE
-- =================================================
-- Stores basic user information

CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE
);

-- Sample Users Data
INSERT INTO users (name, email) VALUES
('Test User', 'testuser@email.com');

-- =================================================
-- PORTFOLIO TABLE
-- =================================================
-- Stores user stock holdings

CREATE TABLE IF NOT EXISTS portfolio (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    stock_symbol VARCHAR(20) NOT NULL,
    quantity INT NOT NULL CHECK (quantity > 0),
    buy_price DECIMAL(10,2) NOT NULL CHECK (buy_price > 0),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Sample Portfolio Data
INSERT INTO portfolio (user_id, stock_symbol, quantity, buy_price) VALUES
(1, 'AAPL', 10, 170.50),
(1, 'GOOGL', 5, 2800.00),
(1, 'MSFT', 8, 395.75);

-- =================================================
-- STOCK PRICE HISTORY TABLE
-- =================================================
-- Stores historical stock prices for analysis & charts

CREATE TABLE IF NOT EXISTS stock_history (
    id INT PRIMARY KEY AUTO_INCREMENT,
    stock_symbol VARCHAR(20) NOT NULL,
    price DECIMAL(10,2) NOT NULL CHECK (price > 0),
    recorded_at DATETIME NOT NULL
);

-- Sample Stock History Data
INSERT INTO stock_history (stock_symbol, price, recorded_at) VALUES
('AAPL', 175.50, '2025-11-19 10:00:00'),
('AAPL', 176.20, '2025-11-19 11:00:00'),
('GOOGL', 2850.75, '2025-11-19 10:00:00'),
('MSFT', 410.30, '2025-11-19 10:00:00');

-- =================================================
-- RISK HISTORY TABLE
-- =================================================
-- Stores ML-generated risk scores over time

CREATE TABLE IF NOT EXISTS risk_history (
    id INT PRIMARY KEY AUTO_INCREMENT,
    stock_symbol VARCHAR(20) NOT NULL,
    risk_score INT NOT NULL CHECK (risk_score BETWEEN 1 AND 10),
    checked_at DATETIME NOT NULL
);

-- Sample Risk History Data
INSERT INTO risk_history (stock_symbol, risk_score, checked_at) VALUES
('AAPL', 3, '2025-11-20 09:00:00'),
('GOOGL', 6, '2025-11-20 09:05:00'),
('MSFT', 5, '2025-11-20 09:10:00');

-- =================================================
-- API LOGS TABLE
-- =================================================
-- Logs external API responses for debugging & monitoring

CREATE TABLE IF NOT EXISTS api_logs (
    id INT PRIMARY KEY AUTO_INCREMENT,
    symbol VARCHAR(20) NOT NULL,
    response TEXT NOT NULL,
    logged_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- =================================================
-- RISK LOGS TABLE
-- =================================================
-- Logs AI/ML risk engine responses for audit & tracking

CREATE TABLE IF NOT EXISTS risk_logs (
    id INT PRIMARY KEY AUTO_INCREMENT,
    symbol VARCHAR(20) NOT NULL,
    response TEXT NOT NULL,
    logged_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
