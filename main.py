from app.utils.path_loader import PathLoader
from app.database.migration_loader import MigrationLoader

PLoader = PathLoader()
MLoader = MigrationLoader()

MLoader.create_migration_loader()