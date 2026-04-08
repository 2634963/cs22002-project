from api._databaseConnection import database

print(__file__ + " has nothing to do with the database and must be updated")

def call(args):
    print("attempted login")

    if "username" not in args:
        return 400

    if "password" not in args:
        return 400

    return 200
