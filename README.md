# Todo CLI Application

A command-line interface (CLI) application to manage a to-do list using MongoDB for storage.

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/KatanaSword/todo_cli.git
   cd todo-cli
   ```

2. **Create a virtual environment and activate it:**

   ```sh
   pip install virtualenv
   python -m venv .venv
   .\.venv\Scripts\activate  # On Mac use `source .venv/bin/activate`
   ```

3. **Install the dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Set up MongoDB:**
   - Ensure MongoDB is installed and running on your machine or use a cloud MongoDB service.
   - Create a `.env` file with your MongoDB URL:
     ```python
     MONGODB_URL = "your_mongodb_connection_string"
     ```

## Usage

Run the Todo CLI application:

```sh
python todo.py
```

Follow the on-screen menu to manage your to-do list:

1. List all todos.
2. List complete todos.
3. List incomplete todos.
4. Add a todo.
5. Mark a todo as complete.
6. Update a todo.
7. Delete a todo.
8. Exit the application.

## License

This project is licensed under the MIT `LICENSE` - see the LICENSE file for details.
