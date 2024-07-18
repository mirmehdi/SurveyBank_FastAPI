# Questions API Project

## Overview

This project provides a simple API for managing questions using FastAPI. It allows users to fetch questions and add new questions to a CSV file. The project includes authentication to ensure that only authorized users can access the endpoints.

## Project Structure

- `main.py`: The main application file that sets up the FastAPI server and defines the endpoints.
- `questions.csv`: The CSV file that stores the questions.
- `requirements.txt`: A file listing the dependencies needed for the project.
- `test_api.sh`: A shell script to test the API using cURL.
- `architecture.md`: This file, explaining the architecture of the project.

## Endpoints

### Healthcheck

- **URL**: `/healthcheck`
- **Method**: `GET`
- **Description**: Checks if the API is functional.
- **Response**: `{ "status": "API is functional" }`

### Get Questions

- **URL**: `/questions`
- **Method**: `GET`
- **Description**: Fetches a list of questions.
- **Parameters**:
  - `use` (optional): The type of MCQ for which the questions are used.
  - `subjects` (optional): The category of the questions.
  - `count` (default: 5): The number of questions to fetch.
- **Authentication**: Basic (required)
- **Response**: A list of questions.

### Add Question

- **URL**: `/questions`
- **Method**: `POST`
- **Description**: Adds a new question to the CSV file.
- **Request Body**: A JSON object representing the new question.
- **Authentication**: Basic (admin required)
- **Response**: `{ "message": "Question added successfully" }`

## Authentication

The API uses Basic Authentication. Users must provide a valid username and password to access the endpoints. The user credentials are hardcoded for simplicity.

- **Users**:
  - `alice`: `wonderland`
  - `bob`: `builder`
  - `clementine`: `mandarine`

- **Admin**:
  - `admin`: `4dm1N`

## Running the Project

1. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
y
