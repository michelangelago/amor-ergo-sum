from app.database.connection import Connection

class DietMigration:
    def __init__(self):
        self.conn = Connection()
        self.cursor = self.conn.cursor()
        self.up()

    def up(self):
        print("DietMI")
        with self.cursor.execute:
            self.cursor.execute(
                """ CREATE TABLE IF NOT EXISTS diets (
                        id              INTEGER         GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                        name            TEXT            UNIQUE,
                        description     TEXT,
                        created_on      TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
                        user_id         INTEGER         REFERENCES users(id)
                    );
                """
            )
        self.conn.commit()

    def down(self):
        with self.cursor.execute:
            self.cursor.execute("DROP TABLE IF EXISTS diets;")
            self.conn.commit()
