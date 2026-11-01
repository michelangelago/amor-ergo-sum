from src.database import database

postgres = database.Database()


try:
    arroz = postgres.insert_foods("Arroz", 10.1, 10.1, 10.1, 10.1, 10.1, 10.1, 10.1, 1)
    print(arroz)
except:
    print("already inserted food")

try:
    new_user = postgres.create_users("kakazik", "xipxip")
except Exception as e:
    print(f"error: {e}")
