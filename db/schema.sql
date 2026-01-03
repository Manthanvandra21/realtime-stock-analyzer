-- File: db/schema.sql
-- Purpose:
-- Final database schema for Stock Price Analyzer
-- Verified for production readiness and Day 8+ backend integration

-- =================================================
-- USERS TABLE
-- =================================================
-- Purpose:
-- Stores basic user profile data.
-- Backend Auth/User Service will later:
-- - Create users
-- - Authenticate users
-- - Link portfolios to users

CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE
);

-- Sample user for backend testing
INSERT INTO users (name, email) VALUES
('Test User', 'testuser@email.com');

-- =================================================
-- PORTFOLIO TABLE
-- =================================================
-- Purpose:
-- Stores user stock holdings.
-- Backend Portfolio Service will:
-- - Insert new holdings
-- - Update quantities & prices
-- - Fetch holdings for dashboard
-- API Mapping:
-- /portfolio → portfolio

CREATE TABLE IF NOT EXISTS portfolio (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    stock_symbol VARCHAR(20) NOT NULL,
    quantity INT NOT NULL CHECK (quantity > 0),
    buy_price DECIMAL(10,2) NOT NULL CHECK (buy_price > 0),
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Sample portfolio data
INSERT INTO portfolio (user_id, stock_symbol, quantity, buy_price) VALUES
(1, 'AAPL', 10, 170.50),
(1, 'GOOGL', 5, 2800.00),
(1, 'MSFT', 8, 395.75);

-- =================================================
-- STOCK PRICE HISTORY TABLE
-- =================================================
-- Purpose:
-- Stores historical stock prices fetched from market APIs.
-- Backend Market Data Service will:
-- - Insert price snapshots
-- - Use data for charts & analysis
-- API Mapping:
-- /prices/history → stock_history

CREATE TABLE IF NOT EXISTS stock_history (
    id INT PRIMARY KEY AUTO_INCREMENT,
    stock_symbol VARCHAR(20) NOT NULL,
    price DECIMAL(10,2) NOT NULL CHECK (price > 0),
    recorded_at DATETIME NOT NULL
);

-- Sample historical prices
INSERT INTO stock_history (stock_symbol, price, recorded_at) VALUES
('AAPL', 175.50, '2025-11-19 10:00:00'),
('AAPL', 176.20, '2025-11-19 11:00:00'),
('GOOGL', 2850.75, '2025-11-19 10:00:00'),
('MSFT', 410.30, '2025-11-19 10:00:00');

-- =================================================
-- RISK HISTORY TABLE
-- =================================================
-- Purpose:
-- Stores ML-generated risk scores per stock.
-- Backend Risk Engine will later:
-- - Insert new risk evaluations
-- - Track risk changes over time
-- - Support dashboards & alerts
-- API Mapping:
-- /risk/analyze → risk_history
--
-- Note:
-- Structure supports frequent inserts without modification.

CREATE TABLE IF NOT EXISTS risk_history (
    id INT PRIMARY KEY AUTO_INCREMENT,
    stock_symbol VARCHAR(20) NOT NULL,
    risk_score INT NOT NULL CHECK (risk_score BETWEEN 1 AND 10),
    checked_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Sample risk scores
INSERT INTO risk_history (stock_symbol, risk_score, checked_at) VALUES
('AAPL', 3, '2025-11-20 09:00:00'),
('GOOGL', 6, '2025-11-20 09:05:00'),
('MSFT', 5, '2025-11-20 09:10:00');

-- =================================================
-- API LOGS TABLE
-- =================================================
-- Purpose:
-- Stores raw responses from external stock APIs.
-- Backend API Layer will:
-- - Log all API responses
-- - Help debugging & monitoring
-- API Mapping:
-- /api/fetch-price → api_logs

CREATE TABLE IF NOT EXISTS api_logs (
    id INT PRIMARY KEY AUTO_INCREMENT,
    symbol VARCHAR(20) NOT NULL,
    response TEXT NOT NULL,
    logged_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- =================================================
-- RISK LOGS TABLE
-- =================================================
-- Purpose:
-- Stores AI/ML risk engine responses.
-- Backend Risk Service will:
-- - Log model outputs
-- - Support audits and issue analysis
-- API Mapping:
-- /risk/evaluate → risk_logs

CREATE TABLE IF NOT EXISTS risk_logs (
    id INT PRIMARY KEY AUTO_INCREMENT,
    symbol VARCHAR(20) NOT NULL,
    response TEXT NOT NULL,
    logged_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

