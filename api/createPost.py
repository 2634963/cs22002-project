from api._databaseConnection import database, connection
from api._getAuthToken import verifyAuthToken

import flask

def call(args):
    if "title" not in args["args"]:
        return flask.Response("no title", 400)

    if len(args["args"]["title"]) < 4:
        return flask.Response("title too short", 400)

    if len(args["args"]["title"]) > 250:
        return flask.Response("title too long", 400)

    if "content" not in args["args"]:
        return flask.Response("no content", 400)

    if "extraInfo" not in args["args"]:
        return flask.Response("no extra info", 400)

    if "authToken" not in args["cookies"]:
        return flask.Response("please sign in", 401)

    if not verifyAuthToken(args["cookies"]["authToken"]):
        return flask.Response("please sign in", 401)

    postId = database.execute("select max(postID) from posts").fetchall()[0][0] + 1

    posterId = database.execute("select userID from authTokens where authTokenString=? ", (args["cookies"]["authToken"],)).fetchall()[0][0]

    database.execute("insert into posts (postID, posterID, title, content, extraInfo, approved) values (?, ?, ?, ?, ?, '0')", (postId, posterId, args["args"]["title"], args["args"]["content"], args["args"]["extraInfo"]))

    connection.commit()

    return flask.Response("success", status=200)
