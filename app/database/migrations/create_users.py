from app.database.connection import Connection

class UserMigration:
    def __init__(self):
        self.conn = Connection()
        self.cursor = self.conn.cursor()
        self.up()

    def up(self):
        print("UserMi")
        with self.cursor.execute:
            self.cursor.execute(
                """ CREATE TABLE IF NOT EXISTS users (
                        id              INTEGER         GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                        username        TEXT            UNIQUE NOT NULL,
                        password_hash   TEXT            NOT NULL
                    ); 
                """
            )
        self.conn.commit()

    def down(self):
        with self.cursor.execute:
            self.cursor.execute("DROP TABLE IF EXISTS users;")
            self.conn.commit()
