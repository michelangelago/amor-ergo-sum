import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

class Database:

    def __init__(self):
        with psycopg.connect() as self.conn:
            host=os.getenv("DB_HOST", "127.0.0.1"),
            port=5432,
            dbname="ergosum",
            user="postgres",
            password=os.environ["DB_PASSWORD"]
        
    def start(self):
        with self.conn.cursor() as self.cursor:
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
            )
            CREATE TABLE IF NOT EXISTS food_groups (
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            )
            CREATE TABLE IF NOT EXISTS foods (
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            fornecedor_id INTEGER REFERENCES fornecedores(id)
            )
            CREATE TABLE IF NOT EXISTS progress (
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            )
            CREATE TABLE IF NOT EXISTS progress (
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            )
        """)