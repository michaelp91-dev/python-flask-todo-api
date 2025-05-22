# Simple Flask To-Do List API

A basic backend API for managing a list of to-do tasks, built with Python and Flask. This project demonstrates fundamental concepts of RESTful API design, request handling, and in-memory data management.

## Features

-   **CRUD Operations:**
    -   `GET /tasks`: Retrieve all tasks.
    -   `GET /tasks/{id}`: Retrieve a single task by its unique ID.
    -   `POST /tasks`: Create a new task.
    -   `PUT /tasks/{id}`: Update an existing task.
    -   `DELETE /tasks/{id}`: Delete a task.
-   **Unique Task IDs:** Each task is assigned a unique UUID (Universally Unique Identifier).
-   **In-Memory Storage:** Tasks are stored in memory, resetting when the server restarts (for simplicity; a real application would use a database).
-   **JSON Payloads:** Handles JSON for request bodies and responses.
-   **HTTP Status Codes:** Returns appropriate HTTP status codes for success and error conditions (e.g., 200 OK, 201 Created, 400 Bad Request, 404 Not Found).

## Technologies Used

-   **Python:** The core programming language.
-   **Flask:** A lightweight microframework for building web applications and APIs.
-   **`uuid` module:** For generating unique identifiers.

## How to Run Locally

1.  **Prerequisites:**
    -   Python 3.x installed.
    -   `pip` (Python package installer).
    -   `curl` or a tool like Postman for making API requests.

2.  **Clone the Repository:**
    ```bash
    git clone https://github.com/michaelp91-dev/python-flask-todo-api.git
    cd python-flask-todo-api
    ```

3.  **Create and Activate a Virtual Environment:**
    It's best practice to use a virtual environment to manage dependencies.
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS/Termux
    # For Windows: .\venv\Scripts\activate
    ```

4.  **Install Dependencies:**
    ```bash
    pip install Flask
    ```

5.  **Run the Flask Application:**
    ```bash
    python app.py
    ```
    The API server will start, typically running on `http://127.0.0.1:5000` (or `http://0.0.0.0:5000`). Keep this terminal window/session open.

## API Endpoints & Usage (using `curl`)

Open a **new terminal session** to send `curl` requests to your running API.

### 1. Get All Tasks (`GET /tasks`)
```bash
curl [http://127.0.0.1:5000/tasks](http://127.0.0.1:5000/tasks)
