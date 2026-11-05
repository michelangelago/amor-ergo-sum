from app.database.connection import Connection

class DietFoodMigration:
    def __init__(self):
        self.conn = Connection()
        self.cursor = self.conn.cursor()
        self.up()

    def up(self):
        print("DietFoodsMi")
        self.cursor.execute(
            """ CREATE TABLE IF NOT EXISTS diet_foods (
                    id              INTEGER         GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                    diet_id         INTEGER         REFERENCES diets(id),
                    food_id         INTEGER         REFERENCES foods(id),
                    quantity        INTEGER         NOT NULL
                ); 
            """
        )
        self.conn.commit()

    def down(self):
        self.cursor.execute("DROP TABLE IF EXISTS diet_foods;")
        self.conn.commit()
