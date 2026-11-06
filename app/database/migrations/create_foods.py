from app.database.connection import Connection

class FoodMigration:
    def __init__(self):
        self.conn = Connection()
        self.up()

    def up(self):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(
                    """ CREATE TABLE IF NOT EXISTS foods (
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
                    """
                )
            self.conn.commit()
        except Exception as e:
            print(e)

    def down(self):
        with self.conn.cursor() as cursor:
            cursor.execute("DROP TABLE IF EXISTS foods;")
        self.conn.commit()
