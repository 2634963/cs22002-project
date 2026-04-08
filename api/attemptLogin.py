from api._databaseConnection import database

import flask

print(__file__ + " has nothing to do with the database and must be updated")

def call(args):
    if "username" not in args["args"]:
        return 400

    if "password" not in args["args"]:
        return 400

    return flask.Response("this is some data that is the body of the response please treat it very carefully", 200)
