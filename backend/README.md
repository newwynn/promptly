# Prompt Analyser Backend

A FastAPI-based backend service for analyzing prompts.

## Features

- Analyze prompts for token count and complexity
- Estimate cost based on token count
- Simple RESTful API endpoints
- CORS enabled for frontend integration

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Server

```bash
uvicorn main:app --reload
```

The server will start at `http://localhost:8000`

## API Documentation

- Interactive API docs: `http://localhost:8000/docs`
- Alternative API docs: `http://localhost:8000/redoc`

## Endpoints

- `GET /`: Welcome message
- `POST /analyze`: Analyze a prompt
  - Request body: `{ "prompt": "your prompt text", "max_tokens": 100 }`
  - Response: `{ "token_count": 5, "estimated_cost": 0.0001, "complexity": "Simple" }`
