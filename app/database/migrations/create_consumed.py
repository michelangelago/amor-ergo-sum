from app.database.connection import Connection

class ConsumedMigration:
    def __init__(self):
        self.conn = Connection()
        self.up()

    def up(self):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(
                    """ CREATE TABLE IF NOT EXISTS consumed (
                            id              INTEGER          GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                            food_id         INTEGER          REFERENCES foods(id),
                            daily_id        INTEGER          REFERENCES daily(id),
                            time            TIMESTAMPTZ       NOT NULL DEFAULT NOW()
                        );
                    """
                )
            self.conn.commit()
        except Exception as e:
            print(e)

    def down(self):
        with self.conn.cursor() as cursor:
            cursor.execute("DROP TABLE IF EXISTS consumed;")
        self.conn.commit()
