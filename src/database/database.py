import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

class Database:

    def __init__(self):
        with psycopg.connect(
            host=os.getenv("DB_HOST", "127.0.0.1"),
            port=5432,
            dbname="ergosum",
            user="postgres",
            password=os.environ["DB_PASSWORD"]
        ) as self.conn:
            with self.conn.cursor() as self.cursor:
                self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                id              INTEGER         GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                username        TEXT            UNIQUE NOT NULL,
                password_hash   TEXT            NOT NULL
                );
            """)
            with self.conn.cursor() as self.cursor:
                self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS food_groups (
                id              INTEGER         GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                name            TEXT            UNIQUE
                );
            """)
            with self.conn.cursor() as self.cursor:
                self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS foods (
                id              INTEGER         GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                name            TEXT            NOT NULL,
                energy          NUMERIC(2, 1)   NOT NULL,
                fat             NUMERIC(2, 1)   NOT NULL,
                saturates       NUMERIC(2, 1)   NOT NULL,
                carbohydrate    NUMERIC(2, 1)   NOT NULL,
                sugars          NUMERIC(2, 1)   NOT NULL,
                protein         NUMERIC(2, 1)   NOT NULL,
                salt            NUMERIC(2, 1)   NOT NULL,
                food_group_id   INTEGER         REFERENCES food_groups(id)
                );
            """)
            with self.conn.cursor() as self.cursor:
                self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS diets (
                id              INTEGER         GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                name            TEXT            UNIQUE,
                description     TEXT,
                created_on       TIMESTAMPTZ    NOT NULL DEFAULT NOW(),
                user_id         INTEGER         REFERENCES users(id)
                );
            """)
            with self.conn.cursor() as self.cursor:
                self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS diet_foods (
                id              INTEGER         GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                diet_id         INTEGER         REFERENCES diets(id),
                food_id         INTEGER         REFERENCES foods(id)
                );
            """)
            with self.conn.cursor() as self.cursor:
                self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS year_metrics (
                id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                energy          NUMERIC(7, 1)   NOT NULL,
                fat             NUMERIC(7, 1)   NOT NULL,
                saturates       NUMERIC(7, 1)   NOT NULL,
                carbohydrate    NUMERIC(7, 2)   NOT NULL,
                sugars          NUMERIC(7, 1)   NOT NULL,
                protein         NUMERIC(7, 1)   NOT NULL,
                salt            NUMERIC(7, 1)   NOT NULL
                );
            """)
            with self.conn.cursor() as self.cursor:
                self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS month_metrics (
                id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                energy          NUMERIC(5, 1)   NOT NULL,
                fat             NUMERIC(5, 1)   NOT NULL,
                saturates       NUMERIC(5, 1)   NOT NULL,
                carbohydrate    NUMERIC(5, 2)   NOT NULL,
                sugars          NUMERIC(5, 1)   NOT NULL,
                protein         NUMERIC(5, 1)   NOT NULL,
                salt            NUMERIC(5, 1)   NOT NULL,
                year_metrics_id  INTEGER        REFERENCES year_metrics(id)
                );
            """)
            with self.conn.cursor() as self.cursor:
                self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS daily_metrics (
                id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                energy          NUMERIC(4, 1)   NOT NULL,
                fat             NUMERIC(4, 1)   NOT NULL,
                saturates       NUMERIC(4, 1)   NOT NULL,
                carbohydrate    NUMERIC(4, 1)   NOT NULL,
                sugars          NUMERIC(4, 1)   NOT NULL,
                protein         NUMERIC(4, 1)   NOT NULL,
                salt            NUMERIC(4, 1)   NOT NULL,
                month_metrics_id  INTEGER       REFERENCES month_metrics(id)
                );
            """)