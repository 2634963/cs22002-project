from api._databaseConnection import database

import flask

def call(args):
    if "userId" not in args["args"]:
        return flask.Response("no user id", 400)

    usernameList = database.execute(f"select username from users where userID='{args["args"]["userId"]}'").fetchall()

    if not usernameList:
        return flask.Response("no such user exists", 404)

    return flask.Response(usernameList[0][0], 200)
