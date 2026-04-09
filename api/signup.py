from api._databaseConnection import database, connection
from api._passwordHashes import hashPassword

import flask

def call(args):
    if "username" not in args["args"]:
        return flask.Response("no username", 400)

    if "password" not in args["args"]:
        return flask.Response("no password", 400)


    # usernames must be at least four characters or else it looks a bit silly
    if len(args["args"]["username"]) < 4:
        return flask.Response("username too short", 400)

    if len(args["args"]["username"]) > 30:
        return flask.Response("username too long", 400)

    # enforce usernames being lowercase alphanumeric only
    for char in args["args"]["username"]:
        if 'a' <= char <= 'z':
            continue

        if '0' <= char <= '9':
            continue

        return flask.Response("invalid character in username: > " + char, 400)

    print(database.execute("select * from users").fetchall())

    if len(args["args"]["password"]) < 8:
        return flask.Response("password too short", 400)

    if len(args["args"]["password"].encode("utf-8")) > 56:
        return flask.Response("password too long", 400)

    userList = database.execute(f"select username from users where username='{args["args"]["username"]}'").fetchall()

    if len(userList):
        return flask.Response("a user with that name already exists", status=400)

    userId = database.execute("select count(*) from users").fetchall()[0][0]

    database.execute(f"insert into users (userID, username, password, admin) values ('{userId}', '{args["args"]["username"]}', \"{hashPassword(args["args"]["password"])}\", 0)")

    connection.commit()

    return flask.Response("success", status=200)
