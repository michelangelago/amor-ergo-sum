from app.database.connection import Connection

class UserMigration:
    def __init__(self):
        self.conn = Connection()
        self.up()

    def up(self):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(
                    """ CREATE TABLE IF NOT EXISTS users (
                            id              INTEGER         GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                            username        TEXT            UNIQUE NOT NULL,
                            password_hash   TEXT            NOT NULL
                        ); 
                    """
                )
                self.conn.commit()
        except Exception as e:
                print(e)

    def down(self):
        with self.conn.cursor() as cursor:
            cursor.execute("DROP TABLE IF EXISTS users;")
        self.conn.commit()
