import os
import psycopg
from dotenv import load_dotenv
from decimal import Decimal
import datetime

load_dotenv()

class Connection:
    def __init__(self):
        try:
            self.conn = psycopg.connect(
                host=os.getenv("DB_HOST", "127.0.0.1"),
                port=5432,
                dbname=os.environ["DB_NAME"],
                user=os.environ["DB_USER"],
                password=os.environ["DB_PASSWORD"]
            )
        except Exception as e:
            print(f"[ERROR]: {e}")

    def get_connection(self):
        return self.conn