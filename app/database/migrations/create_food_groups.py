from app.database.connection import Connection

class FoodGroupMigration:
    def __init__(self):
        self.conn = Connection()
        self.up()

    def up(self):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(
                    """ CREATE TABLE IF NOT EXISTS food_groups (
                            id              INTEGER         GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                            name            TEXT            UNIQUE NOT NULL
                        ); 
                    """
                )
            self.conn.commit()
        except Exception as e:
            print(e)

    def down(self):
        with self.conn.cursor() as cursor:
            cursor.execute("DROP TABLE IF EXISTS food_groups;")
        self.conn.commit()
