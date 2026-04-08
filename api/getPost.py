from api._databaseConnection import database

import flask

print(__file__ + " has nothing to do with the database and must be updated")

def call(args):
    if "postId" not in args["args"]:
        return flask.Response("no post id", 400)

    return flask.Response(status=501)
