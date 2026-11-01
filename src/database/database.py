import os
import psycopg
from dotenv import load_dotenv
from decimal import Decimal

load_dotenv()

class Database:

    def __init__(self):
        self.conn = psycopg.connect(
            host=os.getenv("DB_HOST", "127.0.0.1"),
            port=5432,
            dbname="ergosum",
            user="postgres",
            password=os.environ["DB_PASSWORD"]
        )
        self.create_tables()

        try:
            self.create_food_groups()
        except:
            print("create_food_groups already executed")
            self.conn.rollback()

    def create_tables(self):
        with self.conn.cursor() as self.cursor:
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
            id              INTEGER         GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            username        TEXT            UNIQUE NOT NULL,
            password_hash   TEXT            NOT NULL
            );
            """)
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS food_groups (
            id              INTEGER         GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            name            TEXT            UNIQUE NOT NULL
            );
            """)
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS foods (
            id              INTEGER         GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            name            TEXT            NOT NULL,
            energy          NUMERIC(10, 1)   NOT NULL,
            fat             NUMERIC(10, 1)   NOT NULL,
            saturates       NUMERIC(10, 1)   NOT NULL,
            carbohydrate    NUMERIC(10, 1)   NOT NULL,
            sugars          NUMERIC(10, 1)   NOT NULL,
            protein         NUMERIC(10, 1)   NOT NULL,
            salt            NUMERIC(10, 1)   NOT NULL,
            food_group_id   INTEGER         REFERENCES food_groups(id)
            );
            """)
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS diets (
            id              INTEGER         GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            name            TEXT            UNIQUE,
            description     TEXT,
            created_on       TIMESTAMPTZ    NOT NULL DEFAULT NOW(),
            user_id         INTEGER         REFERENCES users(id)
            );
            """)
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS diet_foods (
            id              INTEGER         GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            diet_id         INTEGER         REFERENCES diets(id),
            food_id         INTEGER         REFERENCES foods(id),
            quantity        INTEGER         NOT NULL
            );
            """)
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS daily_metrics (
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            date            DATE             NOT NULL,
            energy          NUMERIC(10, 1)   NOT NULL,
            fat             NUMERIC(10, 1)   NOT NULL,
            saturates       NUMERIC(10, 1)   NOT NULL,
            carbohydrate    NUMERIC(10, 1)   NOT NULL,
            sugars          NUMERIC(10, 1)   NOT NULL,
            protein         NUMERIC(10, 1)   NOT NULL,
            salt            NUMERIC(10, 1)   NOT NULL
            );
            """)
        self.conn.commit()

    def create_users(self, username: str, password_hash: str) -> tuple[int, str, str]:
        with self.conn.cursor() as self.cursor:
            self.cursor.execute("""
                INSERT INTO users (username, password_hash)
                VALUES (%s, %s)
                RETURNING id, username, password_hash;
                """,
                (username, password_hash)
            )
            res = self.cursor.fetchone()
        self.conn.commit()
        return res

    def create_food_groups(self) -> tuple[str]:
        with self.conn.cursor() as self.cursor:
            self.cursor.execute("""
            INSERT INTO food_groups (name)
            VALUES
            ('fruits'),
            ('vegetables'),
            ('grains'),
            ('protein'),
            ('dairy'),
            ('fats')
            RETURNING *;
            """)
            res = self.cursor.fetchone()
        self.conn.commit()
        return res

    def insert_foods(self, name: str, energy: Decimal, fat: Decimal, saturates: Decimal, carbohydrate: Decimal, sugars: Decimal, protein: Decimal, salt: Decimal, food_group_id: int) -> tuple[int, str, Decimal, Decimal, Decimal, Decimal, Decimal, Decimal, Decimal, int]:
        with self.conn.cursor() as self.cursor:
            self.cursor.execute("""
                INSERT INTO foods (name, energy, fat, saturates, carbohydrate, sugars, protein, salt, food_group_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING id, name, energy, fat, saturates, carbohydrate, sugars, protein, salt, food_group_id;
                """,
                (name, energy, fat, saturates, carbohydrate, sugars, protein, salt, food_group_id)
            )
            res = self.cursor.fetchone()
        self.conn.commit()
        return res

    def rollback(self):
        self.conn.rollback()

    def commit(self):
        self.conn.commit()
            