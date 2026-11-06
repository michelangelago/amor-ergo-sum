from app.database.connection import Connection

class DailyMigration:
    def __init__(self):
        self.conn = Connection()
        self.up()

    def up(self):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(
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
        except Exception as e:
            print(e)

    def down(self):
        with self.conn.cursor() as cursor:
            cursor.execute("DROP TABLE IF EXISTS daily;")
        self.conn.commit()
