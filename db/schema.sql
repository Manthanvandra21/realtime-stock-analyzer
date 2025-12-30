-- File: db/schema.sql
-- Purpose: Prepare database for future portfolio storage
-- Note: No backend integration yet

-- -------------------------------
-- Portfolio Table
-- -------------------------------
-- Stores user stock investment details

CREATE TABLE IF NOT EXISTS portfolio (
    id INT AUTO_INCREMENT PRIMARY KEY,
    stock_symbol VARCHAR(20) NOT NULL,
    quantity INT NOT NULL,
    buy_price FLOAT NOT NULL
);

-- -------------------------------
-- Sample Test Data
-- -------------------------------
-- For testing and future integration

INSERT INTO portfolio (stock_symbol, quantity, buy_price) VALUES
('AAPL', 10, 175.50),
('GOOGL', 5, 2850.75),
('MSFT', 8, 410.30);
