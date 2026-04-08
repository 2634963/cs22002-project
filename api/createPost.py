from api._databaseConnection import database

print(__file__ + " has nothing to do with the database and must be updated")

def call(args):
    if "title" not in args:
        return 400

    if "content" not in args:
        return 400

    if "authorUserId" not in args:
        return 400

    return 200
