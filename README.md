
# AI Stock Market Agent (Flask + LangChain + LLM)

An intelligent backend API agent that provides real-time stock price data and delivers AI-generated buy/sell/hold recommendations.

## Features

- Fetches latest stock price using DuckDuckGo search (can be replaced with live APIs).
- Uses OpenAI  via LangChain to analyze the stock price.
- REST API accessible via curl, Postman, or browser.
- Modular, clean Flask project structure.
- Detailed JSON responses with analysis and price.

## Project Structure

stock_market_agent/
├── app/
│   ├── __init__.py         # Flask app factory
│   ├── agent.py            # LangChain prompt & logic
│   ├── routes.py           # API routes
│   └── stock_fetcher.py    # Web search stock price fetch
├── .env                    # API key (not committed)
├── run.py                  # Start server
├── requirements.txt        # All dependencies
└── README.md               # This file

## Requirements

- Python 3.11.5
- pip
- (Optional) Virtual Environment

## Setup Instructions

### 1. Clone the repository

```bash
git clone <repo-url>
cd stock_market_agent
```

### 2. Create a virtual environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your API key

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_openai_key_here
```

### 5. Run the Flask app

```bash
python run.py
```

The app will start on `http://127.0.0.1:5000/`.

## API Endpoints

### GET /

Returns a welcome message and usage guide.

**Example Response:**
```json
{
  "message": "Welcome to the AI Stock Market Agent.",
  "usage": "POST /api/stock with JSON {'stock': '<stock name>'}",
  "example_request": {
    "method": "POST",
    "endpoint": "/api/stock",
    "headers": {
      "Content-Type": "application/json"
    },
    "body": {
      "stock": "Apple"
    }
  }
}
```

### POST /api/stock

Submit a stock name and get the price with a buy/sell/hold recommendation.

**Request:**
```json
{
  "stock": "Apple"
}
```

**Response:**
```json
{
  "stock": "Apple",
  "price": 175.6,
  "recommendation": "Hold Apple stock due to current market performance.",
  "note": "This includes a real-time stock price and an AI-generated buy/sell/hold suggestion."
}
```

## Testing the API with curl

You can test the POST endpoint using curl (Linux/macOS or Git Bash):

```bash
curl -X POST http://127.0.0.1:5000/api/stock \
     -H "Content-Type: application/json" \
     -d '{"stock": "Apple"}'
```

For Windows PowerShell, use:

```powershell
Invoke-RestMethod -Uri http://127.0.0.1:5000/api/stock `
    -Method Post `
    -Headers @{"Content-Type" = "application/json"} `
    -Body '{"stock": "Apple"}'
```

This will return a JSON response containing the stock name, current price, and AI-generated recommendation.
