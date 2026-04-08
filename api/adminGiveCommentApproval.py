from api._databaseConnection import database

import flask

print(__file__ + " has nothing to do with the database and must be updated")

def call(args):
    if "commentId" not in args["args"]:
        return flask.Response("no comment id", 400)

    if "approved" not in args["args"]:
        return flask.Response("no approval", 400)

    return flask.Response(status=501)
