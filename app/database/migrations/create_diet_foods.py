from app.database.connection import Connection

class DietFoodMigration:
    def __init__(self):
        self.conn = Connection()
        self.up()

    def up(self):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(
                    """ CREATE TABLE IF NOT EXISTS diet_foods (
                            id              INTEGER         GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                            diet_id         INTEGER         REFERENCES diets(id),
                            food_id         INTEGER         REFERENCES foods(id),
                            quantity        INTEGER         NOT NULL
                        ); 
                    """
                )
            self.conn.commit()
        except Exception as e:
            print(e)

    def down(self):
        with self.conn.cursor() as cursor:
            cursor.execute("DROP TABLE IF EXISTS diet_foods;")
        self.conn.commit()
