from api._databaseConnection import database, connection
from api._getAuthToken import verifyAuthToken

import flask

def call(args):
    if "postId" not in args["args"]:
        return flask.Response("no post id", 400)

    if "content" not in args["args"]:
        return flask.Response("no content", 400)

    if not "authToken" in args["cookies"]:
        return flask.Response("please sign in", 401)

    if not verifyAuthToken(args["cookies"]["authToken"]):
        return flask.Response("please sign in again", 401)

    if not len(args["args"]["content"]):
        return flask.Response("no comment content", 422)

    commentId = database.execute("select count(*) from comments").fetchall()[0][0]

    database.execute(f"INSERT INTO comments (postID, content, approved, commentID) VALUES ('{args["args"]["postId"]}', '{args["args"]["content"]}', '0', '{commentId}')")

    connection.commit()

    return flask.Response("success", status=200)
