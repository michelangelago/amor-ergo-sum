import os
class Path:
    def getMigration(self, migration):
        cwd = os.getcwd()
        os.chdir(f"{cwd}/app/database/migrations")
        f = open(f"{migration}.sql", "r", encoding="utf-8")
        content = f.readlines()
        print(content)
        return content 