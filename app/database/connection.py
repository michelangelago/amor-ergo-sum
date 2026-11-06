import os
import psycopg
from dotenv import load_dotenv
import datetime

load_dotenv()

class Connection:
    def __init__(self):
        self.conn = self.connect()

    def connect(self):
        try:
            return psycopg.connect(
            host=os.getenv("DB_HOST", "127.0.0.1"),
            port=5432,
            dbname="data",
            user="postgres",
            password=os.environ["DB_PASSWORD"]
            )
        except Exception as e:
            print(f"[ERROR]: {e}")

    def cursor(self):
        return self.conn.cursor()

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()

    def restart(self):
        self.conn.close()
        self.conn = self.connect()

    def close(self):
        self.conn.close()