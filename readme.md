# FastAPI CI Project

[![FastAPI CI](https://github.com/Kunalshinde2627/fastapi-ci-project/actions/workflows/ci.yml/badge.svg)](https://github.com/Kunalshinde2627/fastapi-ci-project/actions/workflows/ci.yml)

A simple FastAPI application demonstrating automated testing and Continuous Integration (CI) using GitHub Actions.

## Project Overview

This project demonstrates how to build a REST API using FastAPI, write automated tests using Pytest, and automatically run those tests through GitHub Actions whenever code is pushed to the repository.

## Features

- FastAPI REST API
- Health check endpoint
- Create and retrieve items
- HTTP 404 error handling
- Request data validation
- Automated testing using Pytest
- Continuous Integration using GitHub Actions

## Technologies Used

- Python
- FastAPI
- Pytest
- HTTPX
- Git and GitHub
- GitHub Actions

## Project Structure

```text
fastapi-ci-project/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── app/
│   ├── __init__.py
│   └── main.py
│
├── tests/
│   └── test_main.py
│
├── .gitignore
├── requirements.txt
└── readme.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Kunalshinde2627/fastapi-ci-project.git
```

### 2. Navigate to Project Directory

```bash
cd fastapi-ci-project
```

### 3. Create Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate Virtual Environment (Windows)

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

## Run the Application

```bash
uvicorn app.main:app --reload
```

Open the following URLs:

- API Root: http://127.0.0.1:8000/
- Health Check: http://127.0.0.1:8000/health
- Interactive API Documentation: http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Root endpoint |
| GET | `/health` | Health check |
| POST | `/items/{item_id}` | Create an item |
| GET | `/items/{item_id}` | Retrieve an item |

### Example Request

```json
{
  "name": "Laptop",
  "price": 55000
}
```

## Run Automated Tests

Run the following command:

```bash
python -m pytest -v
```

### Test Cases

- Test root endpoint
- Test health endpoint
- Test item creation and retrieval
- Test item not found (404)
- Test invalid item data (422)

**Current Test Result: 5 Passed**

## Continuous Integration (CI)

This project uses GitHub Actions to automate testing.

Whenever code is pushed to the `main` branch:

1. GitHub Actions triggers the workflow.
2. The repository code is checked out.
3. Python environment is configured.
4. Project dependencies are installed.
5. Pytest executes all automated tests.
6. The workflow reports success or failure.

## Author

**Kunal Shinde**

GitHub: https://github.com/Kunalshinde2627