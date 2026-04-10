from api._databaseConnection import database

import json
import flask

def call(args):
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    postList = database.execute("select * from posts where approved=0").fetchall()
    print(postList)

    postDict = {}

    for post in postList:
        postDict[str(post[0])] = {"postId":post[0], "posterID":post[1], "title":post[2], "content":post[3]}

    return flask.Response(json.dumps(postDict), status=200)
