from api._databaseConnection import database

import flask

print(__file__ + " has nothing to do with the database and must be updated")

def call(args):
    if "title" not in args["args"]:
        return flask.Response("no title", 400)

    if "content" not in args["args"]:
        return flask.Response("no content", 400)

    return flask.Response(status=200)
