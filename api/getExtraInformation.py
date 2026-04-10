from api._databaseConnection import database
from api._getAuthToken import verifyAuthToken

import flask

def call(args):
    if "postId" not in args["args"]:
        return flask.Response("no post id", 400)

    if "authToken" not in args["cookies"]:
        return flask.Response("please sign in", 401)

    if not verifyAuthToken(args["cookies"]["authToken"]):
        return flask.Response("please sign in", 401)

    userId = database.execute("select userID from authTokens where authTokenString=? ", (args["cookies"]["authToken"],)).fetchall()[0][0]

    extraInfoList = database.execute("select * from extraInfoAccess where userID=? and postID=? ", (userId, args["args"]["postId"])).fetchall()

    extraInfo = "You don't have access to the extra info for this post, but you can buy access for only £1!"

    statusCode = 402

    if len(extraInfoList):
        extraInfo = database.execute("select extraInfo from posts where postID=? ", (args["args"]["postId"],)).fetchall()[0][0]
        statusCode = 402

    return flask.Response(extraInfo, status=statusCode)
