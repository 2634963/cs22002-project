from api._databaseConnection import database

import flask

print(__file__ + " has nothing to do with the database and must be updated")

# this endpoint is for an admin removing a comment from a post, which they may give a reason for

def call(args):
    if "commentId" not in args["args"]:
        return flask.Response("no comment id", 400)

    if "removalReason" not in args["args"]:
        return flask.Response("no reason", 400)

    database.execute(f"delete from comments where commentID='{args["args"]["commentId"]}'")

    return flask.Response(status=200)
