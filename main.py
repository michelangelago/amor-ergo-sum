from src.database import database

postgres = database.Database()

try:
    new_food = postgres.insert_foods("carne", 10.1, 10.1, 10.1, 10.1, 10.1, 10.1, 10.1, 1)
    print(new_food)
except Exception as e:
    print(f"[ERROR] {e}")
    postgres.rollback()

try:
    new_user = postgres.insert_users("vexis", "mucielagos")
    print(new_user)
except Exception as e:
    print(f"[ERROR] {e}")
    postgres.rollback()

try:
    new_diet = postgres.insert_diets("lamark diet", "A diet based in dairys and coloms", 1)
    print(new_diet)
except Exception as e:
    print(f"[ERROR] {e}")
    postgres.rollback()

try:
    new_diet_food = postgres.insert_diet_foods(1, 1, 100)
    print(new_diet_food)
except Exception as e:
    print(f"[ERROR] {e}")
    postgres.rollback()