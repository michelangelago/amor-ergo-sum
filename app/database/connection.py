import os
import psycopg
from dotenv import load_dotenv
import datetime

load_dotenv()

class Connection:
    def __init__(self):
        try:
            self.conn = psycopg.connect(
            host=os.getenv("DB_HOST", "127.0.0.1"),
            port=5432,
            dbname="data",
            user="postgres",
            password=os.environ["DB_PASSWORD"]
            )
        except Exception as e:
            print(f"[ERROR]: {e}")
        else:
            print("Connection connected")

    def cursor(self):
        return self.conn.cursor()