from api._databaseConnection import database

import flask

def call(args):
    if "title" not in args["args"]:
        return flask.Response("no title", 400)

    if "content" not in args["args"]:
        return flask.Response("no content", 400)

    if "extraInfo" not in args["args"]:
        return flask.Response("no extra info", 400)

    if "authToken" not in args["cookies"]:
        return flask.Response("please sign in", 401)

    postId = database.execute("select count(*) from posts").fetchall()[0][0]

    posterId = database.execute(f"select userID from authTokens where authTokenString='{args["cookies"]["authToken"]}'").fetchall()[0][0]

    database.execute(f"insert into posts (postID, posterID, title, content, extraInfo, approved) values ('{postId}', '{posterId}', '{args["args"]["title"]}', '{args["args"]["content"]}', '{args["args"]["extraInfo"]}', '0')")

    return flask.Response("success", status=200)
