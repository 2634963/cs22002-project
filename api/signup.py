from api._databaseConnection import database

import flask

print(__file__ + " has nothing to do with the database and must be updated")

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

    return flask.Response(status=501)
