# FastAPI-Jobs-API
A simple CRUD (Create, Read, Update, Delete) API built with FastAPI and PostgreSQL.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/prxsss/fastapi-jobs-api.git
   ```

2. Navigate to the project folder:
   ```bash
   cd fastapi-jobs-api
   ```

3. Create and activate a virtual environment:
   - On Linux/macOS:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the `.env` file:
   - Create a `.env` file in the root directory of the project:
     ```bash
     echo $null > .env
     ```
   - Add the required environment variables. Refer to the `.env.example` file for the expected variables:
     ```
     DATABASE_URL=postgresql://username:password@hostname:port/database_name
     ```

5. Run the application:
   ```bash
   fastapi dev main.py
   ```

The application should now be running locally.

## Usage

The application can be accessed via `http://localhost:8000`.

You can test the following endpoints:

- `GET /api/jobs`: Fetch all jobs
- `GET /api/jobs/{id}`: Fetch a single job by ID
- `POST /api/jobs`: Create a new job
- `PATCH /api/jobs/{id}`: Update a job by ID
- `DELETE /api/jobs/{id}`: Delete a job by ID

## API Endpoints

### `GET /api/jobs`
- **Description**: Fetch all jobs.
- **Response**:
  ```json
  [
    {
        "title": "Frontend Developer",
        "description": "Develop and maintain user interfaces.",
        "salary": 60000.0,
        "id": 1
    },
    {
        "title": "Backend Developer",
        "description": "Develop RESTful APIs.",
        "salary": 75000.0,
        "id": 2
    }
  ]
  ```

### `GET /api/jobs/{id}`
- **Description**: Fetch a single job by its ID.
- **Parameters**:
  - `id` (path): The ID of the job to fetch.
- **Response**:
  - **200 OK**:
    ```json
      {
      "title": "Frontend Developer",
      "description": "Develop and maintain user interfaces.",
      "salary": 60000.0,
      "id": 1
    }
    ```
  - **404 Not Found**:
    ```json
    {
      "detail": "Job not found"
    }
    ```

---

### `POST /api/jobs`
- **Description**: Create a new job.
- **Request Body**:
  ```json
  {
    "title": "DevOps Engineer",
    "description": "Implement CI/CD pipelines and maintain system reliability.",
    "salary": 80000
  }
  ```
- **Response**:
  ```json
  {
    "title": "DevOps Engineer",
    "description": "Implement CI/CD pipelines and maintain system reliability.",
    "salary": 80000,
    "id": 3
  }
  ```

### `PATCH /api/jobs/{id}`
- **Description**: Update an existing job by its ID.
- **Parameters**:
  - `id` (path): The ID of the job to update.
- **Request Body**:
  ```json
  {
    "title": "Updated DevOps Engineer",
    "description": "Updated description of DevOps Engineer."
  } 
- **Response**:
  - **200 OK**:
    ```json
    {
      "title": "Updated DevOps Engineer",
      "description": "Updated description of DevOps Engineer.",
      "id": 3
    }
    ```
  - **404 Not Found**:
    ```json
    {
      "detail": "Job not found"
    }
    ```

---

### `DELETE /api/jobs/{id}`
- **Description**: Delete an existing job by its ID.
- **Parameters**:
  - `id` (path): The ID of the job to delete.
- **Response**:
  - **200 OK**:
  ```json
    {
    "ok": true
    }
  ```
  - **404 Not Found**:
    ```json
    {
      "detail": "Job not found"
    }
    ```

---
