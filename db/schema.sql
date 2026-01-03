-- File: db/schema.sql
-- Purpose:
-- Production-ready database schema for Stock Price Analyzer
-- Enhanced with constraints to automatically reject invalid data

-- =================================================
-- USERS TABLE
-- =================================================
-- Purpose:
-- Stores basic user profile data.
-- Constraints:
-- - PRIMARY KEY ensures unique user
-- - UNIQUE email prevents duplicate accounts

CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY AUTO_INCREMENT,        -- Unique user identifier
    name VARCHAR(100) NOT NULL,               -- User name cannot be NULL
    email VARCHAR(150) NOT NULL UNIQUE         -- Prevent duplicate emails
);

-- Sample user (must satisfy all constraints)
INSERT INTO users (name, email) VALUES
('Test User', 'testuser@email.com');

-- =================================================
-- PORTFOLIO TABLE
-- =================================================
-- Purpose:
-- Stores user stock holdings.
-- Constraints:
-- - quantity must be > 0
-- - buy_price must be > 0
-- - user_id must exist in users table

CREATE TABLE IF NOT EXISTS portfolio (
    id INT PRIMARY KEY AUTO_INCREMENT,         -- Unique portfolio row
    user_id INT NOT NULL,                      -- Links holding to a user
    stock_symbol VARCHAR(20) NOT NULL,         -- Stock ticker symbol
    quantity INT NOT NULL CHECK (quantity > 0),-- Prevent zero/negative shares
    buy_price DECIMAL(10,2) NOT NULL 
        CHECK (buy_price > 0),                 -- Prevent invalid prices
    created_at DATETIME NOT NULL 
        DEFAULT CURRENT_TIMESTAMP,             -- Auto record creation time

    FOREIGN KEY (user_id) REFERENCES users(id) -- Enforce valid user ownership
);

-- Sample portfolio data (valid as per constraints)
INSERT INTO portfolio (user_id, stock_symbol, quantity, buy_price) VALUES
(1, 'AAPL', 10, 170.50),
(1, 'GOOGL', 5, 2800.00),
(1, 'MSFT', 8, 395.75);

-- =================================================
-- STOCK PRICE HISTORY TABLE
-- =================================================
-- Purpose:
-- Stores historical stock prices.
-- Constraints:
-- - price must be > 0
-- - timestamp required for time-series accuracy

CREATE TABLE IF NOT EXISTS stock_history (
    id INT PRIMARY KEY AUTO_INCREMENT,         -- Unique price record
    stock_symbol VARCHAR(20) NOT NULL,         -- Stock identifier
    price DECIMAL(10,2) NOT NULL 
        CHECK (price > 0),                     -- Prevent invalid prices
    recorded_at DATETIME NOT NULL              -- Mandatory timestamp
);

-- Sample stock price history
INSERT INTO stock_history (stock_symbol, price, recorded_at) VALUES
('AAPL', 175.50, '2025-11-19 10:00:00'),
('AAPL', 176.20, '2025-11-19 11:00:00'),
('GOOGL', 2850.75, '2025-11-19 10:00:00'),
('MSFT', 410.30, '2025-11-19 10:00:00');

-- =================================================
-- RISK HISTORY TABLE
-- =================================================
-- Purpose:
-- Stores ML-generated risk scores.
-- Constraints:
-- - risk_score limited to range 1–10
-- - ready for frequent inserts from backend

CREATE TABLE IF NOT EXISTS risk_history (
    id INT PRIMARY KEY AUTO_INCREMENT,         -- Unique risk entry
    stock_symbol VARCHAR(20) NOT NULL,         -- Stock identifier
    risk_score INT NOT NULL 
        CHECK (risk_score BETWEEN 1 AND 10),   -- Enforce valid ML output
    checked_at DATETIME NOT NULL 
        DEFAULT CURRENT_TIMESTAMP              -- Auto timestamp for inserts
);

-- Sample ML risk scores
INSERT INTO risk_history (stock_symbol, risk_score, checked_at) VALUES
('AAPL', 3, '2025-11-20 09:00:00'),
('GOOGL', 6, '2025-11-20 09:05:00'),
('MSFT', 5, '2025-11-20 09:10:00');

-- =================================================
-- API LOGS TABLE
-- =================================================
-- Purpose:
-- Stores raw external API responses.
-- Constraints:
-- - response must always be stored
-- - timestamp auto-generated

CREATE TABLE IF NOT EXISTS api_logs (
    id INT PRIMARY KEY AUTO_INCREMENT,         -- Unique log entry
    symbol VARCHAR(20) NOT NULL,               -- API stock symbol
    response TEXT NOT NULL,                    -- Raw API response
    logged_at DATETIME NOT NULL 
        DEFAULT CURRENT_TIMESTAMP              -- Auto log time
);

-- =================================================
-- RISK LOGS TABLE
-- =================================================
-- Purpose:
-- Stores AI/ML engine responses.
-- Constraints:
-- - response mandatory
-- - auto timestamp for audit trail

CREATE TABLE IF NOT EXISTS risk_logs (
    id INT PRIMARY KEY AUTO_INCREMENT,         -- Unique log entry
    symbol VARCHAR(20) NOT NULL,               -- Stock identifier
    response TEXT NOT NULL,                    -- ML response payload
    logged_at DATETIME NOT NULL 
        DEFAULT CURRENT_TIMESTAMP              -- Auto log time
);
