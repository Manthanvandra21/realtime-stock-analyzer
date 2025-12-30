-- File: db/schema.sql

-- Placeholder: Users table structure
-- user_id
-- username
-- email
-- password (placeholder, will be hashed later)
-- created_at

-- Placeholder: Users table
CREATE TABLE IF NOT EXISTS users_placeholder (
    id INT,
    username VARCHAR(100),
    email VARCHAR(100)
);

-- Placeholder: Portfolio table
CREATE TABLE IF NOT EXISTS portfolio_placeholder (
    id INT,
    user_id INT,
    stock_symbol VARCHAR(20),
    quantity INT,
    buy_price FLOAT
);

-- Placeholder: Activity Logs table
CREATE TABLE IF NOT EXISTS activity_logs_placeholder (
    id INT,
    user_id INT,
    action VARCHAR(255),
    timestamp DATETIME
);

-- User table will store id, name, email, password
-- Portfolio table will store user stock details
-- Watchlist table will store saved stocks
-- Logs table will store user actions and time

-- User table connects to portfolio table
-- One user can have many stocks
-- Watchlist belongs to a user
-- Logs belong to a user and store actions

-- -------------------------------
-- Simple Table Structure Planning
-- -------------------------------

-- Users Table
-- id
-- username
-- email
-- password
-- created_at

-- Portfolio Table
-- id
-- user_id
-- stock_symbol
-- quantity
-- buy_price

-- Stock Prices Table
-- id
-- stock_symbol
-- price
-- timestamp

-- -------------------------------
-- Initial Tables for Testing
-- -------------------------------

CREATE TABLE IF NOT EXISTS users (
    id INT,
    name VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS portfolio (
    id INT,
    user_id INT,
    stock_symbol VARCHAR(20),
    quantity INT
);

CREATE TABLE IF NOT EXISTS stock_history (
    id INT,
    symbol VARCHAR(20),
    price FLOAT,
    timestamp DATETIME
);
