from api._databaseConnection import database

print(__file__ + " has nothing to do with the database and must be updated")

def call(args):
    if "username" not in args:
        return 400

    if "password" not in args:
        return 400


    # usernames must be at least four characters or else it looks a bit silly
    if len(args["username"]) < 4:
        return 400

    if len(args["username"]) > 30:
        return 400

    # enforce usernames being lowercase alphanumeric only
    for char in args["username"]:
        if 'a' <= char <= 'z':
            continue

        if '0' <= char <= '9':
            continue

        return 400

    # this is required
    # for some reason
    # dont know what it does
    # dont know how it works
    # just know that it works
    while database.nextset():
        continue

    query = "SELECT * FROM user WHERE username= %s"
    database.execute(query, (args["username"],))

    for thing in database:
        print("==========================================", thing)

    return 200
