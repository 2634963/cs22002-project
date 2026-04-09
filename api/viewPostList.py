from api._databaseConnection import database

import json
import flask

print(__file__ + " has nothing to do with the database and must be updated")

def call(args):
    postList = database.execute("select * from posts where approved=0").fetchall()
    print(postList)

    postDict = {}

    for post in postList:
        postDict[str(post[0])] = {"posterID":post[1], "title":post[2], "content":post[3]}

    return flask.Response(json.dumps(postDict), status=200)
