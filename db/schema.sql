-- File: db/schema.sql

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
