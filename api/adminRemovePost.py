from api._databaseConnection import database, connection

import flask

# this endpoint is for admins removing a post for a reason that they may give

def call(args):
    if "postId" not in args["args"]:
        return flask.Response("no post id", 400)

    if "reason" not in args["args"]:
        return flask.Response("no reason", 400)

    database.execute("delete from posts where postID=? ", (args["args"]["postId"],))

    database.execute("delete from extraInfoAccess where postID=? ", (args["args"]["postId"]))

    connection.commit()

    return flask.Response(status=200)
