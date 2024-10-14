# To-Do-List-API
The To-Do List API is a RESTful web service designed to help users efficiently manage their tasks and enhance productivity. Built using Flask and integrated with MongoDB, this API provides a straightforward interface for performing essential CRUD (Create, Read, Update, Delete) operations on a task management system.

## Features

- Create new tasks with a title and default status (incomplete).
- Retrieve a list of all tasks.
- Update the title and status of existing tasks.
- Delete tasks from the database.

## Technologies Used

- Python
- Flask
- Flask-PyMongo
- MongoDB

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- MongoDB
- pip (Python package manager)

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install the required packages:**

   Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

   Install the necessary dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up MongoDB:**

   Ensure your MongoDB server is running locally. The default port is `27017`.

   You can create a new database called `todo_db` if it doesn't exist:

   ```bash
   mongo
   use todo_db
   ```

## Running the Application

To start the Flask application, run:

```bash
python app.py
```

The API will be available at `http://127.0.0.1:5000/`.

## API Endpoints

### 1. Home

- **GET** `/`
  - Returns a welcome message.

### 2. Get All Tasks

- **GET** `/tasks`
  - Returns a list of all tasks.

### 3. Create a Task

- **POST** `/tasks`
  - Request body should include:
    - `title`: The title of the task (required).
  - Example request:

    ```json
    {
        "title": "My new task"
    }
    ```

### 4. Update a Task

- **PUT** `/tasks/<task_id>`
  - Request body can include:
    - `title`: The new title of the task (optional).
    - `status`: The new status of the task (optional).
  - Example request:

    ```json
    {
        "title": "Updated task title",
        "status": true
    }
    ```

### 5. Delete a Task

- **DELETE** `/tasks/<task_id>`
  - Deletes the specified task.

## License

This project is licensed under the MIT License.
