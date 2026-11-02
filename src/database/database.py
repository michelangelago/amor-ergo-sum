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
            dbname="data",
            user="postgres",
            password=os.environ["DB_PASSWORD"]
        )
        self.create_tables()

        try:
            self.insert_food_groups()
        except:
            print("[ERROR] create_food_groups already executed")
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
                name            TEXT            UNIQUE NOT NULL,
                energy          NUMERIC(10, 1)  NOT NULL,
                fat             NUMERIC(10, 1)  NOT NULL,
                saturates       NUMERIC(10, 1)  NOT NULL,
                carbohydrate    NUMERIC(10, 1)  NOT NULL,
                sugars          NUMERIC(10, 1)  NOT NULL,
                protein         NUMERIC(10, 1)  NOT NULL,
                salt            NUMERIC(10, 1)  NOT NULL,
                food_group_id   INTEGER         REFERENCES food_groups(id)
                );
            """)
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS diets (
                id              INTEGER         GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                name            TEXT            UNIQUE,
                description     TEXT,
                created_on      TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
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
                CREATE TABLE IF NOT EXISTS daily (
                id              INTEGER          GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                energy          NUMERIC(10, 1)   NOT NULL,
                fat             NUMERIC(10, 1)   NOT NULL,
                saturates       NUMERIC(10, 1)   NOT NULL,
                carbohydrate    NUMERIC(10, 1)   NOT NULL,
                sugars          NUMERIC(10, 1)   NOT NULL,
                protein         NUMERIC(10, 1)   NOT NULL,
                salt            NUMERIC(10, 1)   NOT NULL,
                date            DATE             NOT NULL DEFAULT NOW()
                );
            """)
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS consumed (
                id              INTEGER          GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                food_id         INTEGER          REFERENCES foods(id),
                daily_id        INTEGER          REFERENCES daily(id),
                time            TIMESTAMPZ       NOT NULL DEFAULT NOW()
                )
            """)
        self.conn.commit()

    def insert_users(self, username: str, password_hash: str) -> tuple[int, str, str]:
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

    def insert_food_groups(self) -> tuple[str]:
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

    def insert_diets(self, name: str, description: str, user_id: int) -> tuple[int, str, str, int]:
        with self.conn.cursor() as self.cursor:
            self.cursor.execute("""
            INSERT INTO diets (name, description, user_id)
            VALUES (%s, %s, %s)
            RETURNING id, name, description, user_id;
            """,
            (name, description, user_id)
            )
            res = self.cursor.fetchone()
        self.conn.commit()
        return res

    def insert_diet_foods(self, diet_id: int, food_id: int, quantity: int):
        with self.conn.cursor() as self.cursor:
            self.cursor.execute("""
                INSERT INTO diet_foods (diet_id, food_id, quantity)
                VALUES (%s, %s, %s)
                RETURNING id, diet_id, food_id, quantity;
            """,
            (diet_id, food_id, quantity)            
            )
            res = self.cursor.fetchone()
        self.conn.commit()
        return res

    def insert_daily(self, energy: Decimal, fat: Decimal, saturates: Decimal, carbohydrate: Decimal, sugars: Decimal, protein: Decimal, salt: Decimal) -> tuple[int, str, str, str, str, str, str, str, str]:
        with self.conn.cursor() as self.cursor:
            self.cursor.execute("""
            INSERT INTO daily (energy, fat, saturates, carbohydrate, sugars, protein, salt)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            RETURNING *
            """,
            (energy, fat, saturates, carbohydrate, sugars, protein, salt)
            )
        res = self.cursor.fetchone()
        self.conn.commit()
        

    def join_foods_per_group(self) -> list[tuple[str, str]]:
        with self.conn.cursor() as self.cursor:
            self.cursor.execute("""
                SELECT foods.name, food_groups.name
                FROM foods
                INNER JOIN food_groups
                    ON foods.food_group_id = food_groups.id
            """)
            res = self.cursor.fetchall()
        return res

    def join_user_diets(self) -> list[tuple[str, str]]:
        with self.conn.cursor() as self.cursor:
            self.cursor.execute("""
                SELECT users.username, diets.name
                FROM users
                INNER JOIN diets
                    ON diets.user_id = users.id
            """)
            res = self.cursor.fetchall()
        return res

    def join_diet_foods(self) -> list[tuple[str, str]]:
        with self.conn.cursor() as self.cursor:
            self.cursor.execute("""
                SELECT d.name, f.name
                FROM diets d, foods f
                WHERE d.id IN (
                    SELECT diet_id
                    FROM diet_foods
                    WHERE f.id IN (
                        SELECT food_id
                        FROM diet_foods
                    )
                )
            """)
            self.cursor.execute
            res = self.cursor.fetchall()
        return res

    def rollback(self):
        self.conn.rollback()

    def commit(self):
        self.conn.commit()
