# Weather ETL Pipeline

A Python-based ETL (Extract, Transform, Load) pipeline that fetches live weather data from the WeatherAPI service, transforms the required information, and stores it in a PostgreSQL database.

This project was built as part of my journey toward becoming a Data Engineer to gain hands-on experience with APIs, JSON processing, PostgreSQL, and ETL pipeline development.

---

## Features

- Fetches live weather data from WeatherAPI
- Extracts relevant weather information from JSON responses
- Transforms API data into a structured format
- Stores weather records in PostgreSQL
- Uses parameterized SQL queries to prevent SQL injection
- Loads API keys and database credentials securely using environment variables
- Includes basic exception handling for API and database operations

---

## Tech Stack

- Python 3
- PostgreSQL
- Psycopg
- Requests
- Python Dotenv

---

## Project Structure

```text
weather-etl-pipeline/
│
├── src/
│   └── main.py
│
├── db/
│   └── create_weather_db.sql
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## ETL Workflow

```text
            Extract
               │
               ▼
      WeatherAPI (REST API)
               │
               ▼
         JSON Response
               │
               ▼
           Transform
               │
               ▼
     Structured Dictionary
               │
               ▼
              Load
               │
               ▼
      PostgreSQL Database
```

---

## Database Schema

| Column | Data Type |
|----------|-----------|
| id | SERIAL PRIMARY KEY |
| city | VARCHAR(30) |
| temperature | DECIMAL(5,2) |
| humidity | INT |
| weather_desc | VARCHAR(30) |
| retrieved_at | TIMESTAMP DEFAULT CURRENT_TIMESTAMP |

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/weather-etl-pipeline.git
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Configure Environment Variables

Create a `.env` file in the project root.

Example:

```env
WEATHER_API_KEY=your_weatherapi_key

host=localhost
port=5432
database=weather_db
user=postgres
password=your_password
```

---

### 4. Create the Database

Execute the SQL script located in:

```text
database_scripts/create_weather_db.sql
```

This script creates:

- PostgreSQL database
- weather_data table

---

### 5. Run the Application

```bash
python src/main.py
```

---

## Example Output

```text
Enter city name: Hyderabad

Data fetched successfully
Connection successful
Record inserted successfully
Connection closed
```

---

## Skills Demonstrated

- REST API Integration
- JSON Parsing
- ETL Pipeline Design
- PostgreSQL
- SQL
- Parameterized Queries
- Environment Variables
- Python Functions
- Error Handling
- Database Connectivity

---


## Learning Outcomes

Through this project I learned:

- How REST APIs work
- How to consume APIs using the Requests library
- Parsing nested JSON responses
- Designing a simple ETL pipeline
- Connecting Python to PostgreSQL
- Writing parameterized SQL queries
- Managing secrets using environment variables
- Organizing Python code into reusable functions

---
