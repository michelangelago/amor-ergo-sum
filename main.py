from src.database import database

postgres = database.Database()

try:
    new_food = postgres.insert_foods("carne", 10.1, 10.1, 10.1, 10.1, 10.1, 10.1, 10.1, 1)
    new_food = postgres.insert_foods("arroz", 10.1, 10.1, 10.1, 10.1, 10.1, 10.1, 10.1, 1)
    new_food = postgres.insert_foods("feijao", 10.1, 10.1, 10.1, 10.1, 10.1, 10.1, 10.1, 1)
    new_food = postgres.insert_foods("frango", 10.1, 10.1, 10.1, 10.1, 10.1, 10.1, 10.1, 1)
    new_food = postgres.insert_foods("farinha", 10.1, 10.1, 10.1, 10.1, 10.1, 10.1, 10.1, 1)
    new_food = postgres.insert_foods("oleodesoja", 10.1, 10.1, 10.1, 10.1, 10.1, 10.1, 10.1, 1)
except Exception as e:
    print(f"[ERROR] {e}")
    postgres.rollback()

try:
    new_user = postgres.insert_users("vexis", "mucielagos")
except Exception as e:
    print(f"[ERROR] {e}")
    postgres.rollback()

try:
    new_diet = postgres.insert_diets("lamark diet", "A diet based in dairys and coloms", 1)
    new_diet = postgres.insert_diets("carl jung diet", "A diet based in protein and existence", 1)
except Exception as e:
    print(f"[ERROR] {e}")
    postgres.rollback()

try:
    new_diet_food = postgres.insert_diet_foods(1, 5, 100)
    new_diet_food = postgres.insert_diet_foods(2, 2, 100)
    new_diet_food = postgres.insert_diet_foods(1, 7, 100)
    new_diet_food = postgres.insert_diet_foods(2, 6, 100)
    new_diet_food = postgres.insert_diet_foods(1, 4, 100)
    new_diet_food = postgres.insert_diet_foods(2, 3, 100)
except Exception as e:
    print(f"[ERROR] {e}")
    postgres.rollback()

try:
    print("Food     | Food Group")
    join = postgres.join_foods_per_group()
    print(join)
except Exception as e:
    print(f"[ERROR] {e}")

try:
    print("Diet     | Diet Food")
    join = postgres.join_diet_foods()
    print(join)
except Exception as e:
    print(f"[ERROR] {e}")

try:
    join = postgres.join_user_diets()
    print(join)
except Exception as e:
    print(f"[ERROR] {e}")