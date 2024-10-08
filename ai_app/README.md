# AI App

This is a FastAPI application designed to interact with OpenAI services. The project is managed using Poetry for dependency management and packaging.

## Project Structure

- `main.py`: The entry point of the application.
- `controller/`: Contains the API route definitions.
- `service/`: Contains the business logic and service classes.
- `utils/`: Contains utility functions for file reading.
- `pyproject.toml`: Configuration file for Poetry.

## Requirements

- Python 3.10+
- Poetry

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/ananthutkpd/ai_app.git
    cd ai-app
    ```

2. **Install dependencies:**
    ```sh
    poetry install
    ```

## Running the Application

To run the FastAPI application, use the following command:
```sh
poetry run uvicorn main:app --host 127.0.0.1 --port 8000