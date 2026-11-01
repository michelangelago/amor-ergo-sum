from src.database import database

postgres = database()

postgres.start()