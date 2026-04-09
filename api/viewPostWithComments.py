from api._databaseConnection import database

import flask
import json

def call(args):
    if "postId" not in args["args"]:
        return flask.Response("no post id", 400)

    commentList = database.execute(f"select * from comments where postID='{args["args"]["postId"]}' and approved=1").fetchall()

    commentDict = {}

    for comment in commentList:
        commentDict[str(comment[0])] = {"content":comment[2]}

    return flask.Response(json.dumps(commentDict), status=200)
