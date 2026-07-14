CREATE DATABASE weather_db

CREATE TABLE weather_data (
    id SERIAL PRIMARY KEY,
    city VARCHAR(30) NOT NULL,
    temperature DECIMAL(5,2),
    humidity INT,
    weather_desc VARCHAR(30),
    retrieved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);