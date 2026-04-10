from api._databaseConnection import database, connection

import flask

def call(args):
    if "postId" not in args["args"]:
        return flask.Response("no post id", 400)

    if "approved" not in args["args"]:
        return flask.Response("no approval", 400)

    if args["args"]["approved"] == "1":
        database.execute("update posts set approved=1 where postID=? ", (args["args"]["postId"],))
        connection.commit()

    elif args["args"]["approved"] == "0":
        database.execute("delete from posts where postID=? ", (args["args"]["postId"],))
        connection.commit()

    else:
        return flask.Response("invalid approval value", 400)

    return flask.Response(status=200)
