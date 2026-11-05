from app.database.connection import Connection

class DailyMigration:
    def __init__(self):
        self.conn = Connection()
        self.cursor = self.conn.cursor()
        self.up()

    def up(self):
        print("DailyMi")
        self.cursor.execute(
            """ CREATE TABLE IF NOT EXISTS daily (
                    id              INTEGER          GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                    energy          NUMERIC(10, 1)   NOT NULL,
                    fat             NUMERIC(10, 1)   NOT NULL,
                    saturates       NUMERIC(10, 1)   NOT NULL,
                    carbohydrate    NUMERIC(10, 1)   NOT NULL,
                    sugars          NUMERIC(10, 1)   NOT NULL,
                    protein         NUMERIC(10, 1)   NOT NULL,
                    salt            NUMERIC(10, 1)   NOT NULL,
                    date            DATE             NOT NULL DEFAULT NOW()
                );
            """
        )
        self.conn.commit()

    def down(self):
        self.cursor.execute("DROP TABLE IF EXISTS daily;")
        self.conn.commit()
