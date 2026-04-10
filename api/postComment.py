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
        return flask.Response("please sign in", 401)

    if not len(args["args"]["content"]):
        return flask.Response("no comment content", 400)

    if len(args["args"]["content"]) > 200:
        return flask.Response("comment too long", 400)

    commentId = database.execute("select count(*) from comments").fetchall()[0][0]

    userId = database.execute("select * from authTokens where authTokenString=? ", (args["cookies"]["authToken"],)).fetchall()[0][0]

    database.execute("INSERT INTO comments (postID, authorUserID, content, approved, commentID) VALUES (?, ?, ?, '0', ?)", (args["args"]["postId"], userId, args["args"]["content"], commentId))

    connection.commit()

    return flask.Response("success", status=200)
