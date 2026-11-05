from ..database.connection import Connection
from ..utils.path_loader import PathLoader

class MigrationLoader:
    def __init__(self):
        self.conn = Connection()
        self.cursor = self.conn.cursor()
        self.PLoader = PathLoader()


    def create_migration_loader(self):
        print