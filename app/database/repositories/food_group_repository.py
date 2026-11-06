from app.database.connection import Connection


class FoodGroupRepository:
    def __init__(self):
        self.conn = Connection()

    def index(self):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("""
                    SELECT * FROM food_groups;
                """)

                return cursor.fetchall()

        except Exception as e:
            self.conn.rollback()
            print(e)
            raise

    def create(self, name: str):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO food_groups (name)
                    VALUES (%s)
                    RETURNING *;
                """, (name,))

                result = cursor.fetchone()

            self.conn.commit()

            return result

        except Exception as e:
            self.conn.rollback()
            print(e)
            raise

    def read(self, row_id: int):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("""
                    SELECT *
                    FROM food_groups
                    WHERE id = %s;
                """, (row_id,))

                return cursor.fetchone()

        except Exception as e:
            self.conn.rollback()
            print(e)
            raise

    def update(self):
        pass

    def delete(self):
        pass