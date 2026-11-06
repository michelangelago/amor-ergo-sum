from app.database.connection import Connection


class UserRepository:
    def __init__(self):
        self.conn = Connection()

    def index(self):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("""
                    SELECT * FROM users;
                """)

                return cursor.fetchall()

        except Exception as e:
            self.conn.rollback()
            print(e)
            # raise

    def create(self, username: str, password_hash: str):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO users (username, password_hash)
                    VALUES (%s, %s)
                    RETURNING *;
                """, (username, password_hash))

                result = cursor.fetchone()

            self.conn.commit()

            return result

        except Exception as e:
            self.conn.rollback()
            print(e)
            # raise

    def read(self, row_id: int):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("""
                    SELECT *
                    FROM users
                    WHERE id = %s;
                """, (row_id,))

                return cursor.fetchone()

        except Exception as e:
            self.conn.rollback()
            print(e)
            # raise

    def update(self):
        pass

    def delete(self):
        pass