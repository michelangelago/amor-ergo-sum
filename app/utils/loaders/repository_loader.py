import os
class PathLoader:
    def getMigration(self, migration):
        cwd = os.getcwd()
        os.chdir(f"{cwd}/app/database/migrations")
        import migration
        content = migration.query()
        print(content)
        return content 