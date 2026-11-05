from app.database.connection import Connection

class ConsumedMigration:
    def __init__(self):
        self.conn = Connection()
        self.cursor = self.conn.cursor()
        self.up()

    def up(self):
        print("ConsumedMi")
        with self.cursor:
            self.cursor.execute(
                """ CREATE TABLE IF NOT EXISTS consumed (
                        id              INTEGER          GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                        food_id         INTEGER          REFERENCES foods(id),
                        daily_id        INTEGER          REFERENCES daily(id),
                        time            TIMESTAMPTZ       NOT NULL DEFAULT NOW()
                    );
                """
            )
        self.conn.commit()

    def down(self):
        with self.cursor:
            self.cursor.execute("DROP TABLE IF EXISTS consumed;")
            self.conn.commit()
