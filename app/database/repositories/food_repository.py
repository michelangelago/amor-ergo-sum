from app.database.connection import Connection


class FoodRepository:
    def __init__(self):
        self.conn = Connection()

    def index(self):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("""
                    SELECT * FROM foods;
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
                    INSERT INTO foods (name, energy, fat, saturates, carbohydrate, sugars, protein, salt, food_group_id)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    RETURNING *;
                """, (name, energy, fat, saturates, carbohydrate, sugars, protein, salt, food_group_id,))

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
                    FROM foods
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