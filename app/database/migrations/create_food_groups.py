from app.database.connection import Connection

class FoodGroupMigration:
    def __init__(self):
        self.conn = Connection()
        self.cursor = self.conn.cursor()
        self.up()

    def up(self):
        print("FoodGroupMi")
        with self.cursor.execute:
            self.cursor.execute(
                """ CREATE TABLE IF NOT EXISTS food_groups (
                        id              INTEGER         GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                        name            TEXT            UNIQUE NOT NULL
                    ); 
                """
            )
        self.conn.commit()

    def down(self):
        with self.cursor.execute:
            self.cursor.execute("DROP TABLE IF EXISTS food_groups;")
            self.conn.commit()
