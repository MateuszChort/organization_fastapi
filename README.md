# organization_fastapi

## Purpose
The Organization App is a FastAPI-based application that allows users to retrieve organizational data using a NIP (Polish Tax Identification Number) by integrating with the RegonAPI.
This project was created to compare the implementation of the same business logic in Django/DRF and FastAPI.

## Getting Started

### ✅Prerequisites
- Docker and Docker Compose installed on your machine.
- An API key from the RegonAPI service. You can obtain your API key by visiting [RegonAPI](https://api.stat.gov.pl/Home/RegonApi).


### 🐳 Running the Application
To start the application, run the following command in your terminal:
```
docker-compose up --build
```
This command will build the Docker containers and start the application. You can access the application at `http://localhost:8000`.

## 📜 API Documentation
Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

### ✅ Running Tests
To run the tests for the application, use the following command:
```
docker-compose run --rm app pytest
```
Pytest will discover and run all tests (including mocks for RegonAPI).

## 🧪 Features
NIP lookup via RegonAPI.
SQLModel for data modeling.
SQLite (in-memory) for test isolation.
FastAPI dependency injection and routing.
Separation of concerns via routers, schemas, and services

## 📮 License

MIT – free to use, modify and distribute.