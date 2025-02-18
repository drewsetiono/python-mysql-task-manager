# Python MySQL Task Manager

This is a simple command-line task manager application using Python and MySQL. It allows users to add, view, update, and delete tasks from a MySQL database.

## Features
- Add tasks with a title, status, due date, and priority.
- View all tasks in a structured format.
- Update task details.
- Delete tasks from the database.

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- MySQL Server
- Required Python libraries (see below)

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/drewsetiono/python-mysql-task-manager.git
   cd python-mysql-task-manager
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Create a MySQL database and import the schema:
   ```sh
   mysql -u your_username -p < task_manager.sql
   ```

4. Set up your `.env` file with database credentials:
   ```sh
   DB_HOST=localhost
   DB_USER=your_username
   DB_PASSWORD=your_password
   DB_NAME=your_database_name
   ```

## Usage
Run the task manager script:
```sh
python task_manager.py
```

## Repository Structure
```
python-mysql-task-manager/
│── task_manager.py      # Main script with menu
│── db_config.py         # Database connection setup
│── task_manager.sql     # MySQL database schema
│── .gitignore           # Git ignore file
│── README.md            # Project documentation
```

## Notes
- Ensure MySQL is running before executing the script.
- Your credentials are stored in `.env`, which should **not** be committed to GitHub.
- The `.gitignore` file includes `.env` to prevent accidental uploads.

## License
This project is licensed under the MIT License.

