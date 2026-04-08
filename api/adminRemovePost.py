from api._databaseConnection import database

import flask

print(__file__ + " has nothing to do with the database and must be updated")

# this endpoint is for admins removing a post for a reason that they may give

def call(args):
    if "postId" not in args["args"]:
        return flask.Response("no post id", 400)

    if "reason" not in args["args"]:
        return flask.Response("no reason", 400)

    return flask.Response(status=501)
