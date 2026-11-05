from app.database.migrations.create_users import UserMigration
from app.database.migrations.create_food_groups import FoodGroupMigration
from app.database.migrations.create_foods import FoodMigration
from app.database.migrations.create_diets import DietMigration
from app.database.migrations.create_diet_foods import DietFoodMigration
from app.database.migrations.create_daily import DailyMigration
from app.database.migrations.create_consumed import ConsumedMigration

UserMi = UserMigration()

FoodGMi = FoodGroupMigration()

FoodMi = FoodMigration()

DietMi = DietMigration()

DietFoodMi = DietFoodMigration()

DailyMi = DailyMigration()

ConsumedMi = ConsumedMigration()
