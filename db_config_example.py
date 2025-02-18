import os
from dotenv import load_dotenv
import mysql.connector

# Load the .env file to get environment variables
load_dotenv()

def create_connection():
    """Connect to the MySQL database using environment variables."""
    host = os.getenv("DB_HOST")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    database = os.getenv("DB_NAME")

    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        print("Successfully connected to the database!")
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
