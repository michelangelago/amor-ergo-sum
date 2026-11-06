from app.database.migrations.create_users import UserMigration
from app.database.migrations.create_food_groups import FoodGroupMigration
from app.database.migrations.create_foods import FoodMigration
from app.database.migrations.create_diets import DietMigration
from app.database.migrations.create_diet_foods import DietFoodMigration
from app.database.migrations.create_daily import DailyMigration
from app.database.migrations.create_consumed import ConsumedMigration

from app.database.repositories.user_repository import UserRepository
from app.database.repositories.food_group_repository import FoodGroupRepository

UserMi = UserMigration()
UserRepo = UserRepository()
new_user = UserRepo.create("lala", "123")
print(new_user)
read_user = UserRepo.read(1)
print(read_user)

FoodGMi = FoodGroupMigration()
FoodGRepo = FoodGroupRepository()
new_group = FoodGRepo.create("Dairys")
print(new_group)
read_group = FoodGRepo.read(1)
print(read_group)

FoodMi = FoodMigration()
DietMi = DietMigration()
DietFoodMi = DietFoodMigration()
DailyMi = DailyMigration()
ConsumedMi = ConsumedMigration()