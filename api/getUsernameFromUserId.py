from api._databaseConnection import database

import flask
import json

def call(args):
    if "userId" not in args["args"]:
        return flask.Response("no user id", 400)

    usernameList = database.execute("select username from users where userID=?", (args["args"]["userId"],)).fetchall()

    if not usernameList:
        return flask.Response("no such user exists", 404)

    return flask.Response(json.dumps({"0":usernameList[0][0]}), 200)
